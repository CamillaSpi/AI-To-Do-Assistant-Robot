import sqlite3
import hashlib

global conn 
global cur
global toReturn

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
              id_possession VARCHAR(256) NOT NULL,
              ID INTEGER NOT NULL,
              category VARCHAR(50) NOT NULL,
              FOREIGN KEY (ID) REFERENCES users(ID) ON DELETE CASCADE ON UPDATE CASCADE,
              FOREIGN KEY (category) REFERENCES categories(name) ON DELETE CASCADE ON UPDATE CASCADE,
              PRIMARY KEY (id_possession),
              UNIQUE(ID,category)
          );
      ''')
      actual_conn.execute('''
          CREATE TRIGGER IF NOT EXISTS delete_activities_for_category AFTER DELETE ON possessions FOR EACH ROW 
          BEGIN
            DELETE FROM unfoldings WHERE ID = OLD.id AND category = OLD.category;
          END
      ''')
      actual_conn.commit()

  @staticmethod
  def initDb(selectedDataBase):
    global conn 
    global cur
    global toReturn
    if selectedDataBase == 0:
      toReturn = 0
      conn = sqlite3.connect('data.db')
      cur = conn.cursor()
      conn.execute('''PRAGMA foreign_keys = 1''')
      conn.commit() #users table
      conn.execute('''
          CREATE TABLE IF NOT EXISTS users (
              ID INTEGER PRIMARY KEY,
              name VARCHAR(50)
          );
        ''')
      conn.commit()
    else:
      toReturn=1
      conn = sqlite3.connect('data2.db')
      cur = conn.cursor()
      conn.execute('''PRAGMA foreign_keys = 1''')
      conn.commit()
    
      #users table
      conn.execute('''
          CREATE TABLE IF NOT EXISTS users (
              ID VARCHAR(256) PRIMARY KEY,
              name VARCHAR(50)
          );
      ''')
      conn.commit()
    Database.initTable(conn)


  @staticmethod
  def doesPossessionExists(ID,category):
    if category != None and ID != None:
      cur.execute('''
        SELECT * FROM possessions WHERE ID == ? AND category == ?
      ''', (ID, category))
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
  def doesUnfoldingsExists(ID,category,activity,deadline=None):
    m = hashlib.sha256()
    m.update(str(ID).encode())
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
  def createUser(ID,name):
    try:
      conn.execute('''
        INSERT INTO users (ID,name) VALUES (?,?);
      ''', (ID,name))
      conn.commit()
      return True
    except sqlite3.IntegrityError as e:
        print('expcetion add users ' , e)
        return False

  @staticmethod
  def insertItem(ID, activity ,category, reminder,deadline=None):
    try:
      m = hashlib.sha256()
      m.update(str(ID).encode())
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
        INSERT INTO unfoldings (id_unfolding, ID, activity, category, deadline, completed, reminder) VALUES (?, ?, ?, ?, ?, ?, ?);
      ''', (id_unfolding,ID, activity ,category,deadline,False,reminder))
      conn.commit()
      return True
    except sqlite3.IntegrityError as e :
      print(e)
      return False

  @staticmethod
  def selectItems(ID, category=None, activity_status=None, deadline=None):
    global toReturn
    if ID == None: return None
    if(activity_status == "completata"):
      completed = True
    elif(activity_status == "incompleta"):
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
    base_query = base_query + " ORDER BY category;"
    final_query = base_query
    for elem in base_list:
      if (isinstance(elem,str)):
        final_query = final_query.replace("?","'" + str(elem) + "'",1)
      else:
        final_query = final_query.replace("?",str(elem),1)
    query_dict = {"query": final_query}
    cur.execute(base_query,base_list)
    rows = cur.fetchall()
    if(toReturn == 0):
      query_dict['query'] = query_dict['query'].replace("activity,category,deadline,completed,reminder","*")
      return len(rows),query_dict
    else:
      toprint = None
      if(len(rows)>0):  
        category = ["Attivita","Categoria","DeadLine","Completata"]
        number = [i for i in range(1,len(rows)+1)]
        row_format ="{:>20}" * (len(category) + 1)
        toprint = ""
        toprint += (row_format.format("", *category)) + "\n"
        for team, row in zip(number, rows):
            if (row[2]):
              row = (row[0],row[1],row[2][:10]+ " "+row[2][11:16],row[3])
            else:
              row = (row[0],row[1],"None",row[3])
            toprint += (row_format.format(team, *row)) + "\n"
      return toprint,None
      

  @staticmethod
  def deleteItem(ID, activity ,category,deadline):
    m = hashlib.sha256()
    m.update(str(ID).encode())
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
      Database.checkActivitiesTable(activity)
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
  def insertCategoryAndPossession(ID, category):
    if ID != None and category != None:
      m = hashlib.sha256()
      m.update(str(ID).encode())
      m.update(str(category).encode())
      m.digest()
      id_possession = m.hexdigest()
      try:
        if(not Database.doesCategoryExists(category)):
          conn.execute('''
            INSERT INTO categories (name) VALUES (?);
          ''', (category,))
        conn.execute('''
          INSERT INTO possessions (id_possession, ID, category) VALUES (?,?,?);
        ''', (id_possession,ID,category))
        conn.commit()
        return True
      except sqlite3.IntegrityError:
        pass
    return False

  @staticmethod
  def selectPossessions(ID):
    global toReturn
    if ID != None:
      query="SELECT * FROM possessions WHERE ID == ? ORDER BY category;"
      cur.execute(query,(ID,)) 
    rows = cur.fetchall()
    query = query.replace("?",str(ID))
    query_dict = {"query":query}
    if(toReturn==0):
      return len(rows),query_dict
    else:
      categories_list = None
      if len(rows) > 0:
        categories_list = ""
        for category in rows:
          if category is not None:
            categories_list +=  str(category[2]) + ", "
        categories_list = categories_list[:-2]
      return categories_list,None

  @staticmethod
  def deleteCategory(ID, category):
    if ID!= None and category != None:
      cur.execute('''
        SELECT * FROM possessions WHERE ID == ? AND category == ? 
      ''', (ID, category))
      
      if(len(cur.fetchall()) > 0 ):
        conn.execute('''
        DELETE FROM possessions WHERE ID == ? AND category == ? 
      ''', (ID, category))
        conn.commit()
        Database.checkCategoriesTable(category)
        return True
    return False

  @staticmethod
  def checkActivitiesTable(activity):
    cur.execute('''
        SELECT * FROM unfoldings WHERE activity == ? 
      ''', (activity,))
    if(len(cur.fetchall()) > 0 ):
      print("ci sono altri con questa activity")
      return
    else:
      conn.execute('''
        DELETE FROM activities WHERE name == ? 
      ''', (activity,))
      conn.commit()

  @staticmethod 
  def checkCategoriesTable(category):
    cur.execute('''
        SELECT * FROM possessions WHERE category == ? 
      ''', (category,))
    if(len(cur.fetchall()) > 0 ):
      print("ci sono altri con questa category")
      return
    else:
      conn.execute('''
        DELETE FROM categories WHERE name == ? 
      ''', (category,))
      conn.commit()

  @staticmethod
  def setItemStatus(ID, activity ,category,deadline,completed):
    m = hashlib.sha256()
    m.update(str(ID).encode())
    m.update(str(activity).encode())
    m.update(str(category).encode())
    m.update(str(deadline).encode())
    m.digest()
    id_unfolding = m.hexdigest()
    cur.execute('''
      SELECT * FROM unfoldings WHERE id_unfolding == ? 
    ''', (id_unfolding, ))
    rows= cur.fetchall()
    if(len(rows) > 0 ):
      if(deadline == None):
        conn.execute('''UPDATE unfoldings SET completed = ? WHERE ID == ? AND activity == ? AND category == ?
      ''', (completed, ID, activity ,category))
      else:
        conn.execute('''UPDATE unfoldings SET completed = ? WHERE ID == ? AND activity == ? AND category == ? AND deadline == ?
        ''', (completed, ID, activity ,category,deadline))
      conn.commit()
      return True
    else:
      return False

###ERRORI QUI DENTRO 
  @staticmethod
  def modifyCategory(ID, category, category_new):
    print("query eseguita:", ID, category)
    cur.execute('''
      SELECT * FROM possessions WHERE ID == ? AND category == ?
    ''', (ID, category))
    if(len(cur.fetchall()) > 0 ):
      if category_new != None:
        if not Database.doesCategoryExists(category_new):
          #Andrebbe comunicato che è stata creata tale category
          Database.insertCategory(category_new)
        m = hashlib.sha256()
        m.update(str(ID).encode())
        m.update(str(category_new).encode())
        m.digest()
        id_possession = m.hexdigest()
        print(category_new)
        conn.execute('''
          UPDATE possessions SET id_possession = ?, category = ? WHERE ID == ? AND category == ?;
        ''', (id_possession,category_new,ID,category))
        ##NON VIENE AGGIORNATO l'ID
        conn.execute('''
          UPDATE unfoldings SET category = ? WHERE ID == ? AND category == ?;
        ''', (category_new,ID,category))
        Database.checkCategoriesTable(category)
        conn.commit()
        return True
    else:
      return False

  @staticmethod
  def modifyActivity(ID, category, activity, deadline, newcategory = None, newactivity = None, newdeadline = None):
    try:
      m = hashlib.sha256()
      m.update(str(ID).encode())
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
          if newcategory!=None and not Database.doesPossessionExists(ID,newcategory):
            #Andrebbe comunicato che è stata creata tale category
            Database.insertCategoryAndPossession(ID, newcategory)
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
        conn.execute(query, tupleParam)
        conn.commit()
        Database.checkActivitiesTable(activity)
        return True
      else:
        return False
    except sqlite3.IntegrityError as e:
      print(e)
      return False

  @staticmethod
  def updateReminder(ID, category, activity, deadline,reminder):
      m = hashlib.sha256()
      m.update(str(ID).encode())
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
  def doesUserExists(ID):
    if ID != None:
      cur.execute('''
        SELECT * FROM users WHERE ID == ?
      ''', (ID, ))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

  @staticmethod
  def getName(ID):
    if ID != None:
      cur.execute('''
        SELECT name FROM users WHERE ID == ?
      ''', (ID, ))
      toReturn = cur.fetchall()
      if(len( toReturn) > 0 ):
        return toReturn[0][0]
    return None
    
  @staticmethod
  def cleanCompletedActivities(ID):
    if ID != None:
      conn.execute('''
        DELETE FROM unfoldings WHERE ID == ? and completed == True
      ''', (ID,))
      conn.commit()
      return True
    return None   


  @staticmethod
  def getAllReminder():
    cur.execute('''
          SELECT ID,activity,category,deadline FROM unfoldings WHERE reminder == True
        ''')
    toReturn = cur.fetchall()
    return toReturn