import sqlite3
import hashlib

conn = sqlite3.connect('data.db')
cur = conn.cursor()

print("connected")

class Database:

  @staticmethod
  def initDb():
    conn.execute('''PRAGMA foreign_keys = 1''')
    conn.commit()
    #users table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(50) PRIMARY KEY
        );
    ''')
    #categories table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            name VARCHAR(50) PRIMARY KEY
        );
    ''')
    #activities table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            name VARCHAR(50) PRIMARY KEY
        );
    ''')
    #unfoldings table relate users, activities, categories
    conn.execute('''
        CREATE TABLE IF NOT EXISTS unfoldings (
            id_unfolding VARCHAR(256) NOT NULL,
            username VARCHAR(50) NOT NULL,
            activity VARCHAR(50) NOT NULL,
            category VARCHAR(50) NOT NULL,
            deadline DATETIME,
            completed BOOLEAN NOT NULL,
            reminder BOOLEAN NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (activity) REFERENCES activities(name) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (category) REFERENCES categories(name) ON DELETE CASCADE ON UPDATE CASCADE,
            PRIMARY KEY (id_unfolding) 
        );
    ''')
    #categories table relate users to possessions
    conn.execute('''
        CREATE TABLE IF NOT EXISTS possessions (
            username VARCHAR(50) NOT NULL,
            category VARCHAR(50) NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (category) REFERENCES categories(name) ON DELETE CASCADE ON UPDATE CASCADE,
            PRIMARY KEY (username,category)
        );
    ''')
    conn.commit()

  @staticmethod
  def doesPossessionExists(username,category):
    if category != None and username != None:
      cur.execute('''
        SELECT * FROM possessions WHERE username == ? AND category == ?
      ''', (username, category))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False
    
  @staticmethod
  def doesCategoryExists(category):
    if category != None:
      cur.execute('''
        SELECT * FROM categories WHERE name == ?
      ''', (category,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def doesUnfoldingsExists(username,category,activity,deadline=None):
    m = hashlib.sha256()
    m.update(str(username).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ?
    ''', (id_unfolding,))
    if(len( cur.fetchall()) > 0 ):
      return True
    return False

  @staticmethod
  def doesActivityExists(activity):
    if activity != None:
      cur.execute('''
        SELECT * FROM activities WHERE name == ?
      ''', (activity,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def createUser(username):
    try:
      conn.execute('''
        INSERT INTO users (username) VALUES (?);
      ''', (username,))
      conn.commit()
      return True
    except sqlite3.IntegrityError as e:
        print(e)
        return False

  @staticmethod
  def insertItem(username, activity ,category, reminder,deadline=None):
    try:
      m = hashlib.sha256()
      m.update(str(username).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      if not Database.doesActivityExists(activity):
        conn.execute('''
        INSERT INTO activities (name) VALUES (?);
        ''', (activity,))
      conn.execute('''
        INSERT INTO unfoldings (id_unfolding, username, activity, category, deadline, completed, reminder) VALUES (?, ?, ?, ?, ?, ?, ?);
      ''', (id_unfolding,username, activity ,category,deadline,False,reminder))
      conn.commit()
      return True
    except sqlite3.IntegrityError as e :
      return False

  @staticmethod
  def selectItems(username, category=None, activity_status=None):
    if username == None: return None
    if(activity_status == "completed"):
      completed = True
    elif(activity_status == "uncompleted"):
      completed = False
    base_query = "SELECT activity,category,deadline,completed FROM unfoldings WHERE username == ?"
    base_list = [username,]
    if(category != None):
      base_query = base_query + " AND category == ?"
      base_list.append(category)
    if(activity_status != None):
      base_query = base_query + " AND completed == ?"
      base_list.append(completed)
    base_query = base_query + ";"
    cur.execute(base_query,base_list)
    
    rows = cur.fetchall()
    if(len(rows)>0):
      category = ["Activities","Category","DeadLine","Completed"]
      number = [i for i in range(1,len(rows)+1)]
      row_format ="{:>20}" * (len(category) + 1)
      toPrint = ""
      toPrint += (row_format.format("", *category)) + "\n"
      for team, row in zip(number, rows):
          if (row[2]):
            row = (row[0],row[1],row[2][:10]+ " "+row[2][11:16],row[3])
          else:
            row = (row[0],row[1],"None",row[3])
          toPrint += (row_format.format(team, *row)) + "\n"


    return toPrint if len(rows) > 0 else None

  @staticmethod
  def deleteItem(username, activity ,category,deadline):
    m = hashlib.sha256()
    m.update(str(username).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    
    cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ?
    ''', (id_unfolding,))

    if(len(cur.fetchall()) > 0 ):
      conn.execute('''
        DELETE FROM unfoldings WHERE id_unfolding == ?
      ''', (id_unfolding,))
      conn.commit()
      return True
    else:
      return False

  @staticmethod
  def insertCategory(category):
    if category != None:
      cur.execute('''
        INSERT INTO categories (name) VALUES (?);
      ''', (category,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def insertActivity(activity):
    if activity != None:
      cur.execute('''
        INSERT INTO activities (name) VALUES (?);
      ''', (activity,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def insertCategoryAndPossession(username, category):
    if username != None and category != None:
      try:
        if(not Database.doesCategoryExists(category)):
          conn.execute('''
            INSERT INTO categories (name) VALUES (?);
          ''', (category,))
        conn.execute('''
          INSERT INTO possessions (username, category) VALUES (?,?);
        ''', (username,category))
        conn.commit()
        return True
      except sqlite3.IntegrityError:
        pass
    return False

  @staticmethod
  def selectPossessions(username):
    if username != None:
      cur.execute('''
      SELECT * FROM possessions WHERE username == (?);
      ''',(username,)) 

      rows = cur.fetchall()
      if len(rows) > 0:
        categories_list = ""
        for category in rows:
          if category is not None:
            categories_list +=  str(category[1]) + ", "
        categories_list = categories_list[:-2]
      else:
        categories_list = "No activity found"
      
      return categories_list
    return "No activity found"

  @staticmethod
  def deleteCategory(username, category):
    if username!= None and category != None:
      cur.execute('''
        SELECT * FROM possessions WHERE username == ? AND category == ? 
      ''', (username, category))
      
      if(len(cur.fetchall()) > 0 ):
        conn.execute('''
        DELETE FROM possessions WHERE username == ? AND category == ? 
      ''', (username, category))
        conn.commit()
        return True
    return False

  @staticmethod
  def setItemStatus(username, activity ,category,deadline,completed):
    m = hashlib.sha256()
    m.update(str(username).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ? 
    ''', (id_unfolding, ))

    if(len(cur.fetchall()) > 0 ):
      conn.execute('''UPDATE unfoldings SET completed = ? WHERE username == ? AND activity == ? AND category == ? AND deadline == ?
      ''', (completed, username, activity ,category,deadline))
      conn.commit()
      return True
    else:
      return False

  @staticmethod
  def modifyCategory(username, category, category_new):
    cur.execute('''
      SELECT * FROM possessions WHERE username == ? AND category == ?
    ''', (username, category))
    if(len(cur.fetchall()) > 0 ):
      if category_new != None:
        if not Database.doesCategoryExists(category_new):
          #Andrebbe comunicato che è stata creata tale categoria
          Database.insertCategory(category_new)
      conn.execute('''
        UPDATE possessions SET category = ? WHERE username == ? AND category == ?;
      ''', (category_new,username,category))
      conn.execute('''
        UPDATE unfoldings SET category = ? WHERE username == ? AND category == ?;
      ''', (category_new,username,category))
      conn.commit()
      return True
    else:
      return False

  @staticmethod
  def modifyActivity(username, category, activity, deadline, newcategory = None, newactivity = None, newdeadline = None):
    try:
      m = hashlib.sha256()
      m.update(str(username).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      cur.execute('''
        SELECT * FROM unfoldings WHERE id_unfolding == ?
      ''', (id_unfolding,))
      if(len(cur.fetchall()) > 0 ):
        if newcategory != None:
          if newcategory!=None and not Database.doesPossessionExists(username,newcategory):
            #Andrebbe comunicato che è stata creata tale categoria
            Database.insertCategoryAndPossession(username, newcategory)
          if newactivity!=None and not Database.doesActivityExists(newactivity):
            #Andrebbe comunicato che è stata creata tale activity
            Database.insertActivity(newactivity)
        paramList = list()
        paramList.append(("activity", newactivity))
        paramList.append(("category", newcategory))
        paramList.append(("deadline",newdeadline))
        queryParam=""
        tupleParam = ()
        p = hashlib.sha256()
        p.update(str(username).encode())
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
        conn.execute(query, tupleParam)
        conn.commit()
        return True
      else:
        return False
    except sqlite3.IntegrityError as e:
      print(e)
      return False

  @staticmethod
  def updateReminder(username, category, activity, deadline,reminder):
      m = hashlib.sha256()
      m.update(str(username).encode())
      m.update(str(activity).encode())
      m.update(str(category).encode())
      m.update(str(deadline).encode())
      m.digest()
      id_unfolding = m.hexdigest()
      try: 
        conn.execute('''
        UPDATE unfoldings SET reminder = ? WHERE id_unfolding == ?
        ''', (reminder,id_unfolding))
        conn.commit()
        return True
      except sqlite3.IntegrityError:
        return False


  @staticmethod
  def doesUserExists(username):
    if username != None:
      cur.execute('''
        SELECT * FROM users WHERE username == ?
      ''', (username, ))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

