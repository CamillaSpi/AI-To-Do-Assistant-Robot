import sqlite3
import hashlib

conn = sqlite3.connect('data.db')
cur = conn.cursor()

conn2 = sqlite3.connect('data2.db')
cur2 = conn2.cursor()

print("connected")

class Database:

  @staticmethod
  def initTable(actual_conn): 
      #categories table
      actual_conn.execute('''
          CREATE TABLE IF NOT EXISTS categories (
              name VARCHAR(50) PRIMARY KEY
          );
      ''')
      #activities table
      actual_conn.execute('''
          CREATE TABLE IF NOT EXISTS activities (
              name VARCHAR(50) PRIMARY KEY
          );
      ''')
      #unfoldings table relate users, activities, categories
      actual_conn.execute('''
          CREATE TABLE IF NOT EXISTS unfoldings (
              id_unfolding VARCHAR(256) NOT NULL,
              ID INTEGER NOT NULL,
              activity VARCHAR(50) NOT NULL,
              category VARCHAR(50) NOT NULL,
              deadline DATETIME,
              completed BOOLEAN NOT NULL,
              reminder BOOLEAN NOT NULL,
              FOREIGN KEY (ID) REFERENCES users(ID) ON DELETE CASCADE ON UPDATE CASCADE,
              FOREIGN KEY (activity) REFERENCES activities(name) ON DELETE CASCADE ON UPDATE CASCADE,
              FOREIGN KEY (category) REFERENCES categories(name) ON DELETE CASCADE ON UPDATE CASCADE,
              PRIMARY KEY (id_unfolding) 
          );
      ''')
      #categories table relate users to possessions
      actual_conn.execute('''
          CREATE TABLE IF NOT EXISTS possessions (
              ID INTEGER NOT NULL,
              category VARCHAR(50) NOT NULL,
              FOREIGN KEY (ID) REFERENCES users(ID) ON DELETE CASCADE ON UPDATE CASCADE,
              FOREIGN KEY (category) REFERENCES categories(name) ON DELETE CASCADE ON UPDATE CASCADE,
              PRIMARY KEY (ID,category)
          );
      ''')
      actual_conn.commit()

  @staticmethod
  def initDb():
    conn.execute('''PRAGMA foreign_keys = 1''')
    conn.commit()
    conn2.execute('''PRAGMA foreign_keys = 1''')
    conn2.commit()
    #users table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY,
            name VARCHAR(50)
        );
    ''')
    conn.commit()
    #users table
    conn2.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID VARCHAR(256) PRIMARY KEY,
            name VARCHAR(50)
        );
    ''')
    conn2.commit()
    Database.initTable(conn)
    Database.initTable(conn2)

  @staticmethod
  def returnConnection():
    return conn,cur, conn2, cur2

  @staticmethod
  def doesPossessionExists(ID,category,actual_cur):
    if category != None and ID != None:
      actual_cur.execute('''
        SELECT * FROM possessions WHERE ID == ? AND category == ?
      ''', (ID, category))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False
    
  @staticmethod
  def doesCategoryExists(category,actual_cur):
    if category != None:
      actual_cur.execute('''
        SELECT * FROM categories WHERE name == ?
      ''', (category,))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def doesUnfoldingsExists(ID,category,activity,actual_cur,deadline=None):
    m = hashlib.sha256()
    m.update(str(ID).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    actual_cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ?
    ''', (id_unfolding,))
    if(len( actual_cur.fetchall()) > 0 ):
      return True
    return False

  @staticmethod
  def doesActivityExists(activity,actual_cur):
    if activity != None:
      actual_cur.execute('''
        SELECT * FROM activities WHERE name == ?
      ''', (activity,))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def createUser(ID,name,actual_conn):
    try:
      actual_conn.execute('''
        INSERT INTO users (ID,name) VALUES (?,?);
      ''', (ID,name))
      actual_conn.commit()
      return True
    except sqlite3.IntegrityError as e:
        print(e)
        return False

  @staticmethod
  def insertItem(ID, activity ,category, reminder,actual_cur,actual_conn,deadline=None):
    try:
      m = hashlib.sha256()
      m.update(str(ID).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      if not Database.doesActivityExists(activity,actual_cur):
        actual_conn.execute('''
        INSERT INTO activities (name) VALUES (?);
        ''', (activity,))
      actual_conn.execute('''
        INSERT INTO unfoldings (id_unfolding, ID, activity, category, deadline, completed, reminder) VALUES (?, ?, ?, ?, ?, ?, ?);
      ''', (id_unfolding,ID, activity ,category,deadline,False,reminder))
      actual_conn.commit()
      return True
    except sqlite3.IntegrityError as e :
      return False

  @staticmethod
  def selectItems(ID, actual_cur,category=None, activity_status=None, deadline=None):
    if ID == None: return None
    if(activity_status == "completed"):
      completed = True
    elif(activity_status == "uncompleted"):
      completed = False
    base_query = "SELECT activity,category,deadline,completed,reminder FROM unfoldings WHERE ID == ?"
    base_list = [ID,]
    if(category != None):
      base_query = base_query + " AND category == ?"
      base_list.append(category)
    if(activity_status != None):
      base_query = base_query + " AND completed == ?"
      base_list.append(completed)
    if(deadline != None):
      if(isinstance(deadline,dict)):
        first_date = list(deadline.values())[1]
        second_date = list(deadline.values())[0]
        base_query = base_query + " AND deadline BETWEEN ? AND ?"
        base_list.append(first_date)
        base_list.append(second_date)
      else:
        first_date = deadline
        second_date = deadline[:11] + "23:59:59" + deadline[19:]
        base_query = base_query + " AND deadline BETWEEN ? AND ?"
        base_list.append(first_date)
        base_list.append(second_date)
    base_query = base_query + ";"
    actual_cur.execute(base_query,base_list)
    rows = actual_cur.fetchall()

    return len(rows) if len(rows) > 0 else None

  @staticmethod
  def deleteItem(ID, activity ,category,deadline,actual_cur,actual_conn):
    m = hashlib.sha256()
    m.update(str(ID).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    
    actual_cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ?
    ''', (id_unfolding,))

    if(len(actual_cur.fetchall()) > 0 ):
      actual_conn.execute('''
        DELETE FROM unfoldings WHERE id_unfolding == ?
      ''', (id_unfolding,))
      actual_conn.commit()
      return True
    else:
      return False

  @staticmethod
  def insertCategory(category,actual_cur):
    if category != None:
      actual_cur.execute('''
        INSERT INTO categories (name) VALUES (?);
      ''', (category,))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def insertActivity(activity,actual_cur):
    if activity != None:
      actual_cur.execute('''
        INSERT INTO activities (name) VALUES (?);
      ''', (activity,))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def insertCategoryAndPossession(ID, category,actual_cur,actual_conn):
    if ID != None and category != None:
      try:
        if(not Database.doesCategoryExists(category,actual_cur)):
          actual_conn.execute('''
            INSERT INTO categories (name) VALUES (?);
          ''', (category,))
        actual_conn.execute('''
          INSERT INTO possessions (ID, category) VALUES (?,?);
        ''', (ID,category))
        actual_conn.commit()
        return True
      except sqlite3.IntegrityError:
        pass
    return False

  @staticmethod
  def selectPossessions(ID,actual_cur):
    if ID != None:
      actual_cur.execute('''
      SELECT * FROM possessions WHERE ID == (?);
      ''',(ID,)) 
      
    rows = actual_cur.fetchall()
    
    return len(rows) if len(rows) > 0 else None

  @staticmethod
  def deleteCategory(ID, category,actual_cur,actual_conn):
    if ID!= None and category != None:
      actual_cur.execute('''
        SELECT * FROM possessions WHERE ID == ? AND category == ? 
      ''', (ID, category))
      
      if(len(actual_cur.fetchall()) > 0 ):
        actual_conn.execute('''
        DELETE FROM possessions WHERE ID == ? AND category == ? 
      ''', (ID, category))
        actual_conn.commit()
        return True
    return False

  @staticmethod
  def setItemStatus(ID, activity ,category,deadline,completed,actual_cur,actual_conn):
    m = hashlib.sha256()
    m.update(str(ID).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    actual_cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ? 
    ''', (id_unfolding, ))
    rows= actual_cur.fetchall()
    if(len(rows) > 0 ):
      if(deadline == None):
        actual_conn.execute('''UPDATE unfoldings SET completed = ? WHERE ID == ? AND activity == ? AND category == ?
      ''', (completed, ID, activity ,category))
      else:
        actual_conn.execute('''UPDATE unfoldings SET completed = ? WHERE ID == ? AND activity == ? AND category == ? AND deadline == ?
        ''', (completed, ID, activity ,category,deadline))
      actual_conn.commit()
      return True
    else:
      return False

  @staticmethod
  def modifyCategory(ID, category, category_new,actual_cur,actual_conn):
    actual_cur.execute('''
      SELECT * FROM possessions WHERE ID == ? AND category == ?
    ''', (ID, category))
    if(len(actual_cur.fetchall()) > 0 ):
      if category_new != None:
        if not Database.doesCategoryExists(category_new,actual_cur):
          #Andrebbe comunicato che è stata creata tale categoria
          Database.insertCategory(category_new,actual_cur)
      actual_conn.execute('''
        UPDATE possessions SET category = ? WHERE ID == ? AND category == ?;
      ''', (category_new,ID,category))
      actual_conn.execute('''
        UPDATE unfoldings SET category = ? WHERE ID == ? AND category == ?;
      ''', (category_new,ID,category))
      actual_conn.commit()
      return True
    else:
      return False

  @staticmethod
  def modifyActivity(ID, category, activity, deadline, actual_cur,actual_conn,newcategory = None, newactivity = None, newdeadline = None):
    try:
      m = hashlib.sha256()
      m.update(str(ID).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      actual_cur.execute('''
        SELECT * FROM unfoldings WHERE id_unfolding == ?
      ''', (id_unfolding,))
      if(len(actual_cur.fetchall()) > 0 ):
        if newcategory != None:
          if newcategory!=None and not Database.doesPossessionExists(ID,newcategory,actual_cur):
            #Andrebbe comunicato che è stata creata tale categoria
            Database.insertCategoryAndPossession(ID, newcategory,actual_conn)
          if newactivity!=None and not Database.doesActivityExists(newactivity,actual_cur):
            #Andrebbe comunicato che è stata creata tale activity
            Database.insertActivity(newactivity,actual_cur)
        paramList = list()
        paramList.append(("activity", newactivity))
        paramList.append(("category", newcategory))
        paramList.append(("deadline",newdeadline))
        queryParam=""
        tupleParam = ()
        p = hashlib.sha256()
        p.update(str(ID).encode())
        for param in paramList:
          if param[1] is not None:
            tupleParam += (param[1],)
            queryParam += ", " + str(param[0]) + " = ?"
          else:
            param = (param[0],exec(param[0]))
          p.update(str(param[1]).encode())
        p.digest()
        id_unfolding_new = p.hexdigest()
        queryParam += ", id_unfolding = ?"
        tupleParam += (id_unfolding_new, id_unfolding,)
        query = "UPDATE unfoldings SET" + queryParam[1:] + " WHERE id_unfolding == ?"
        actual_conn.execute(query, tupleParam)
        actual_conn.commit()
        return True
      else:
        return False
    except sqlite3.IntegrityError as e:
      print(e)
      return False

  @staticmethod
  def updateReminder(ID, category, activity, deadline,reminder,actual_conn):
      m = hashlib.sha256()
      m.update(str(ID).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      try: 
        actual_conn.execute('''
        UPDATE unfoldings SET reminder = ? WHERE id_unfolding == ?
        ''', (reminder,id_unfolding))
        actual_conn.commit()
        return True
      except sqlite3.IntegrityError:
        return False


  @staticmethod
  def doesUserExists(ID,actual_cur):
    if ID != None:
      actual_cur.execute('''
        SELECT * FROM users WHERE ID == ?
      ''', (ID, ))
      if(len( actual_cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def getName(ID,actual_cur):
    if ID != None:
      actual_cur.execute('''
        SELECT name FROM users WHERE ID == ?
      ''', (ID, ))
      toReturn = actual_cur.fetchall()
      if(len( toReturn) > 0 ):
        return toReturn[0][0]
    return None
    
  @staticmethod
  def cleanCompletedActivities(ID,actual_conn):
    if ID != None:
      actual_conn.execute('''
        DELETE FROM unfoldings WHERE ID == ? and completed == True
      ''', (ID,))
      actual_conn.commit()
      return True
    return None   


  @staticmethod
  def getAllReminder(actual_cur):
    actual_cur.execute('''
          SELECT ID,activity,category,deadline FROM unfoldings WHERE reminder == True
        ''')
    toReturn = actual_cur.fetchall()
    return toReturn