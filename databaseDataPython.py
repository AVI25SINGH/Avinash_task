import mysql.connector
from mysql.connector import Error
print("start")
connection=None
try:
    connection=mysql.connector.connect(host="localhost",user='root',password="AVInash12@#" ,database="fastapidatabase")
    if connection.is_connected():
        mycursor=connection.cursor()
        query="select * from users;"
        mycursor.execute(query)
        RESULT=mycursor.fetchall()
        
        for i in RESULT:
            
            print(i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print("====================================================")
    else:
        print("some issue")
        
except Error as e:
    print("some issue in sql",e)


finally:
    if  connection.is_connected():
        mycursor.close()
        connection.close()
        print("close")

# import mysql.connector
# from mysql.connector import Error

# connection = None

# try:
    
#     connection = mysql.connector.connect(
#         host="localhost",
#         user='root',
#         password="AVInash12@#",
#         database="fastapidatabase"
#     )
    
#     if connection.is_connected():
#         mycursor = connection.cursor()
#         query = "SELECT * FROM users;"  
#         mycursor.execute(query)
#         RESULT = mycursor.fetchall()  
        
#         for i in RESULT:
#             print(i[0])  
#             print(i[1])  #
#             print(i[2])  # 
#             print(i[3])  # 
#     else:
#         print("Connection issue")

# except Error as e:
#     print("Some issue in SQL:", e)

# finally:
    
#     if connection and connection.is_connected():
#         mycursor.close()  # Close the cursor
#         connection.close()  # Close the connection
#         print("MySQL connection is closed")
