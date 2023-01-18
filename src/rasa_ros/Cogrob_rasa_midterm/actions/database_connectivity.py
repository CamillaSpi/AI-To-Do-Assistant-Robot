import sqlite3
import hashlib

global conn 
global cur
global toReturn

class Database:

# This script is initializing tables in a SQLite database. 
# The script first creates a table called "categories" with a column "name" of type VARCHAR with a maximum length of 50, 
# and sets it as the primary key. Then, it creates a table called "activities" with a similar structure. Next, it creates a table called 
# "unfoldings" which relates users, activities and categories together. The table has columns "id_unfolding" and "ID" of type INTEGER, 
# "activity" and "category" of type VARCHAR, "deadline" of type DATETIME, "completed" and "reminder" of type BOOLEAN. 
# It also sets up foreign key constraints between "ID" and "users" table, "activity" and "activities" table, "category" and "categories" 
# table, and sets "id_unfolding" as primary key. After that, it creates another table called "possessions" which relates users and categories 
# together. It has similar structure as unfoldings table, also creates a unique constraint for (ID,category) . Finally, it creates a trigger 
# called "delete_activities_for_category" which deletes rows from unfoldings table when corresponding rows from possessions table are deleted.

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

# This script is initializing a SQLite database.
# It starts by connecting to either 'data.db' or 'data2.db', depending on the value of the selectedDataBase parameter passed to the function.
# Then it sets up a cursor object "cur" to perform SQL commands on the database.
# Next, it sets the 'foreign_keys' pragma to 1, which enables foreign key constraints.
# It then creates a table named 'users' with two columns: ID and name. 
# The ID column is set as the primary key and its type is INTEGER for the first database and VARCHAR(256) for the second database.
# It then calls the initTable method with the database connection as a parameter, which creates several tables within the database.
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

# This script is a python method that check if a possession for a specific user and category exists in the database.
# The method takes in two parameters, ID and category, representing the user and the category of possession respectively.
# It first checks if the category and ID are not None.
# Then it runs a SELECT query on the 'possessions' table in the database, looking for a record where the ID and category 
# match the passed in parameters.
# It returns True if a record is found, indicating that the possession exists, otherwise it returns False.
  @staticmethod
  def doesPossessionExists(ID,category):
    if category != None and ID != None:
      cur.execute('''
        SELECT * FROM possessions WHERE ID == ? AND category == ?
      ''', (ID, category))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

# This script defines a static method called doesPossessionExists that takes in two arguments: ID and category. 
# The method first checks if both arguments are not None, and if so, it queries the possessions table for any 
# rows where the ID and category match the given arguments. If the query returns any rows, the method returns True. 
# Otherwise, the method returns False. This method is likely used to check if a specific possession already exists 
# in the database for a given user.  
  @staticmethod
  def doesCategoryExists(category):
    if category != None:
      cur.execute('''
        SELECT * FROM categories WHERE name == ?
      ''', (category,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

# This script defines a method called doesUnfoldingsExists which takes in four parameters: ID, category, activity, and deadline. 
# The method first creates a sha256 hash of the four inputs, which is then used as the id_unfolding. 
# It then queries the unfoldings table for a row where the id_unfolding matches the one created above. 
# If the query returns any rows, the method returns True, otherwise it returns False. 
# This method is likely used to check if a specific unfolding already exists in the unfoldings table before inserting it.

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

# This script defines a method called "doesActivityExists" which takes in a parameter "activity".
# It uses the cursor object "cur" to query the "activities" table for a record where the "name" column is equal to the "activity" 
# parameter passed in.
# It then checks the length of the rows returned by the query and if greater than 0, it returns True, indicating that the activity 
# exists in the table.
# Otherwise, it returns False, indicating that the activity does not exist in the table.

  @staticmethod
  def doesActivityExists(activity):
    if activity != None:
      cur.execute('''
        SELECT * FROM activities WHERE name == ?
      ''', (activity,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

# The script defines a function called createUser that takes in two parameters, ID and name. 
# Inside the function, it uses SQLite3 to insert the provided ID and name into the users table. 
# The function uses a try-except block to catch any sqlite3.IntegrityError exceptions that may occur. 
# If an exception is caught, the error message is printed and the function returns False. If the insertion is successful, 
# the function commits the changes to the database and returns True.
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
# This script defines a method called "insertItem" which is used to insert new items into the "unfoldings" table in a SQLite database. 
# It takes in several arguments: ID, activity, category, reminder, and deadline. It first checks if the activity already exists in the 
# "activities" table and if not, it inserts it. Then it creates a unique identifier for the new item by using the SHA-256 hashing algorithm on the 
# ID, activity, category and deadline values, and uses this id to insert the item into the "unfoldings" table. The item is inserted with the default 
# value of "completed" being False and with the reminder value passed in. It also uses a try-except block to catch a "sqlite3.IntegrityError" 
# exception in case there is any issue with the insertion and returns a boolean value indicating the success of the operation.
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

# This script defines a method called selectItems() which is used to retrieve and return information from the 'unfoldings' table in the database. 
# The method takes in four parameters: ID, category, activity_status, and deadline. It then constructs a SQL query based on the provided parameters 
# and the values of global variable toReturn. The query is executed and the results are returned. If toReturn is 0, the length of the result set 
# is returned, otherwise, the result set is formatted into a string and returned. Additionally, the method also has a try-except block for handling 
# any sqlite3.IntegrityError exceptions that may occur.
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

# This script defines a static method deleteItem that takes in four parameters: ID, activity, category, and deadline. 
# It starts by creating a SHA-256 hash of the four parameters using the hashlib library, and assigns the resulting digest to 
# the variable id_unfolding.
# Next, it uses a SELECT statement to check if there is an existing entry in the unfoldings table with the specified id_unfolding. 
# If there is such an entry, it uses a DELETE statement to delete the entry from the unfoldings table. 
# The method commits the deletion to the database and returns True. If there is no such entry, it returns False.
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

# This script is a function that is used to insert a new category into the "categories" table in the database. 
# The function takes one parameter, "category", which is the name of the category to be inserted. 
# The function checks if the category is not None and then it uses an SQL statement to insert the category into the "categories" table. 
# It then checks the number of rows that were affected by the insertion query, if the number of rows is greater than 0, it returns true, 
# otherwise it returns False.
  @staticmethod
  def insertCategory(category):
    if category != None:
      cur.execute('''
        INSERT INTO categories (name) VALUES (?);
      ''', (category,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False
# This python script defines a static method called insertActivity that takes in a single parameter activity. 
# It checks if the activity parameter is not None. If activity is not None, it inserts the value of activity into the 'activities' table. 
# The method then checks if there are any rows returned from the query, and if there are, it returns True. 
# If activity is None or there are no rows returned from the query, it returns False.
  @staticmethod
  def insertActivity(activity):
    if activity != None:
      cur.execute('''
        INSERT INTO activities (name) VALUES (?);
      ''', (activity,))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

# This script defines a static method insertCategoryAndPossession that takes in two parameters, ID and category. 
# The method first checks if both the ID and category are not None before proceeding. 
# The method then creates a unique id for the possession by using the hashlib.sha256 library and adding the ID and category as input. 
# It then tries to insert the category and possession into their respective tables, categories and possessions, 
# only if the category does not already exist in the categories table. If a sqlite3.IntegrityError is raised, the method will 
# return False and will not insert the possession into the possessions table. If the insertion is successful, the method will return True.
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

# This script defines a static method selectPossessions(ID) that takes in an ID as an argument. 
# It creates a query to select all rows from the "possessions" table where the ID equals the input ID. 
# The method then executes this query using the ID as a parameter. It also keeps track of the original query for later use.
# The result rows are stored in the variable "rows". If the global variable "toReturn" is 0, it 
# returns the number of rows in the query result and the original query in the form of a dictionary. 
# If the global variable is not 0, it returns a string of all the categories in the table and None.
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

# This script defines a static method deleteCategory that takes in two parameters, ID and category. 
# It first checks if both ID and category are not None. Then, it runs a SQL query to select from the "possessions" 
# table all the rows where the ID and category match the provided parameters. If this query returns any rows, 
# the script proceeds to execute a SQL query to delete the possession from the "possessions" table that matches the provided ID and category. 
# Finally, it calls another static method checkCategoriesTable(category) and returns True if it was successful, otherwise it returns False.
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

# This script defines a static method checkActivitiesTable that takes one parameter activity.
# The method first checks if there are any other rows in the unfoldings table with the same activity by executing a SELECT statement. 
# If there are no other rows, it means that the activity is not being used in any other rows and it can be safely deleted.
# It then deletes the activity from the activities table by executing a DELETE statement. The changes are then committed to the database. 
# If there are other rows with the same activity, the method prints "ci sono altri con questa activity" and returns nothing.
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

# This script is a static method named checkCategoriesTable and is used to check if there are any other 
# items in the 'possessions' table that have the same category as the one passed as an argument to the method, before attempting to delete that 
# category from the 'categories' table.
# It starts by using an sql query to select all rows from the 'possessions' table where the category column matches the passed in category argument.
# Then, it checks the number of rows returned from the query by counting the number of elements in the result set.
# If the number of rows returned is greater than 0, it prints a message indicating that other items have that category and it returns immediately, 
# otherwise it proceeds to execute another sql query to delete the row in the 'categories' table that has the same category as the passed in
# category argument, and commit the changes to the database.
  @staticmethod 
  def checkCategoriesTable(category):
    cur.execute('''
        SELECT * FROM possessions WHERE category == ? 
      ''', (category,))
    if(len(cur.fetchall()) > 0 ):
      print("Altri elementi hanno questa categoria, non la posso rimuovere")
      return
    else:
      conn.execute('''
        DELETE FROM categories WHERE name == ? 
      ''', (category,))
      conn.commit()

# This script defines a static method called setItemStatus which takes in four required arguments: ID, activity, category, and deadline 
# and one optional argument (completed) and changes the status of a given item in the 'unfoldings' table in the database.
# It starts by creating a sha256 hash of the given ID, activity, category, and deadline and assigns it to the variable 'id_unfolding'. 
# Then it uses this variable to search the 'unfoldings' table for a matching row and assigns the result to the variable 'rows'.
# If there is a match, it will then update the 'completed' column of that row in the table with the value passed in for 'completed' 
# and commit the changes to the database. If no match is found, it will return false.
# It also handles cases where the deadline is None by updating the row accordingly.
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

# This script defines a static method modifyCategory that takes three arguments: ID, category, and category_new. 
# The method first checks if there is a possession of the given category associated with the given ID in the database. 
# If such a possession exists, the method checks if the category_new is not None. If category_new is not None, the method checks 
# if the category_new already exists in the database. If it does not, it inserts it.
# Then the method calculates the id_possession by creating a SHA256 hash of ID and category_new and updates the possession 
# in the database by setting the id_possession and category to the new values.
# It also updates the unfoldings table with the new category, and if the old category is not used in any other unfoldings, 
# it is deleted from the categories table. Finally, the method returns True if the update was successful, and False otherwise.
  @staticmethod
  def modifyCategory(ID, category, category_new):
    cur.execute('''
      SELECT * FROM possessions WHERE ID == ? AND category == ?
    ''', (ID, category))
    if(len(cur.fetchall()) > 0 ):
      if category_new != None:
        if not Database.doesCategoryExists(category_new):
          Database.insertCategory(category_new)
        m = hashlib.sha256()
        m.update(str(ID).encode())
        m.update(str(category_new).encode())
        m.digest()
        id_possession = m.hexdigest()

        conn.execute('''
          UPDATE possessions SET id_possession = ?, category = ? WHERE ID == ? AND category == ?;
        ''', (id_possession,category_new,ID,category))
        
        cur.execute('''
          SELECT id_unfolding,ID,activity,category,deadline FROM unfoldings WHERE category = ? AND ID == ? AND category == ?;
        ''', (category,ID,category))
        tmp = cur.fetchall()
        for x in tmp:
          print(x[1],x[2],x[3],category_new,x[4])
          m = hashlib.sha256()
          m.update(str(x[1]).encode())
          m.update(str(x[2]).encode())
          m.update(str(category_new).encode())
          m.update(str(x[4]).encode())
          m.digest()
          id_unfolding = m.hexdigest()
          conn.execute('''
            UPDATE unfoldings SET id_unfolding = ?, category = ? WHERE id_unfolding == ?;
          ''', (id_unfolding,category_new,x[0]))
        Database.checkCategoriesTable(category)
        conn.commit()
        return True
    else:
      return False

# This script defines a method called modifyActivity. It modifies an activity in the database according to the provided parameters. 
# The method first creates a unique identifier for the activity by hashing the provided ID, activity, category, and deadline values.
# It then queries the database to check if the activity with the matching identifier exists. If it does exist, the method creates a new 
# identifier for the new activity by hashing the modified values. It then creates a query string that updates the corresponding fields in 
# the database with the new values and updates the activity's identifier. The method also checks whether the activity table is empty after 
# the update and removes the activity if it is. The method returns True if the update was successful, False otherwise. 
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

# This script defines a static method updateReminder which updates the reminder of an item in the unfoldings table of a database.
# The method first creates a sha256 hash of the passed ID, activity, category, and deadline, which is used as the primary key 
# for the item in the table. Then it updates the reminder column of the item with the passed reminder parameter, using the primary key. 
# If the update is successful, the method returns True. If an exception is raised by the update statement, the method returns False.
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

# This is a static method called "doesUserExists" that takes in an argument "ID" and checks if a user with that ID exists in the "users" 
# table of the database. The method uses the SELECT statement to query the database and retrieve all rows where the ID column matches the 
# provided ID. If there are any rows returned, it means that a user with that ID exists and the method returns True. Otherwise, 
# it returns False indicating that the user does not exist in the table.
  @staticmethod
  def doesUserExists(ID):
    if ID != None:
      cur.execute('''
        SELECT * FROM users WHERE ID == ?
      ''', (ID, ))
      if(len( cur.fetchall()) > 0 ):
        return True
    return False

# This script is a static method called "getName" which takes in a parameter called "ID". 
# It first checks if the ID is not None. If it is not, it queries the "users" table in the database and selects the "name" 
# column where the "ID" is equal to the provided ID. The result of the query is saved in a variable called "toReturn". 
# If there are any rows returned from the query, it returns the first element of the first row (which is the name column) otherwise it returns None.
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

# This script is a static method called "cleanCompletedActivities" which takes in a parameter called "ID". 
# It first checks if the ID is not None. If it is not, it delete inside the unfoldings table all the row with that match with the ID and 
# with the completed value set to true 
# If the value of ID is not None it return True otherwise it returns None.
  @staticmethod
  def cleanCompletedActivities(ID):
    if ID != None:
      conn.execute('''
        DELETE FROM unfoldings WHERE ID == ? and completed == True
      ''', (ID,))
      conn.commit()
      return True
    return None   

# This script is a static method called "getAllReminder".
# It select from the table unfoldings all the rows with the reminder column set to True and return its value.
  @staticmethod
  def getAllReminder():
    cur.execute('''
          SELECT ID,activity,category,deadline FROM unfoldings WHERE reminder == True
        ''')
    toReturn = cur.fetchall()
    return toReturn