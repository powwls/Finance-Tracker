import mysql.connector 

try:
      
      db = mysql.connector.connect(
            
            host = "localhost",
            user = "root",
            password = "password",
            database = "snoopy_iptc"
      
      )
      
      if db.is_connected():
            db_info = db.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = db.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            print("\n")
      
      mycursor = db.cursor()
      
except mysql.connector.Error as err:
      print(err)