# import re

# with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
#     data = file.read()  # Reads the entire file content
    
#     data_value=data.split("~")
#     match=[]
#     for i in data_value:
#     #    print(i)
#        pattern =r"^([A-Za-z]+)"
       
#        matches = re.findall(pattern, i)

#        match.extend(matches)
# print(match)


# with normally
import re
import mysql.connector

with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
    data = file.read()  # Reads the entire file content
    # print(data) # data show
    data_value=data.split("~")
    match=[]
    mat=[]
    for i in data_value:
       print(i)# show all data in line
       dataa=(i.split('*')[0])
       match.append(dataa)
       
    for i in data_value:
        # print(i)  # Show all data in line
        daa = i.split('*')  # Split each line by '*'
        
        if len(daa) > 1:  
            mat.append(daa[1])  
        else:
            mat.append(None) 
    
# print(mat)
# print("............................................")

# print(match)
# database related code 
connection = mysql.connector.connect(
    host='localhost',          # Replace with your host, e.g., 'localhost'
    user='root',       # Replace with your MySQL username
    password='AVInash12@#',   # Replace with your MySQL password
    database='filedataindatbase'    # Replace with your database name
)

cursor = connection.cursor()
# table create
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_table (
        segment VARCHAR(255),
        firstvalue VARCHAR(255)
    )
''') 
# end
# insert data in database
for seg, val in zip(match, mat):
    cursor.execute("INSERT INTO data_table (segment, firstvalue) VALUES (%s, %s)", (seg, val))
# end data


# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print("Data has been successfully inserted into the database.")











# this code for check which code take less time
# import re
# import time  # Import time module to calculate execution time

# # Start the timer
# start_time = time.time()

# First block of code
# with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
#     data = file.read()  # Reads the entire file content
#     data_value = data.split("~")
#     match = []
#     for i in data_value:
#         dataa = (i.split('*'))
#         match.append(dataa)
# print(match)


# Second block of code
# with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
#     data = file.read()  # Reads the entire file content
#     data_value = data.split("~")
#     match = []
#     for i in data_value:
#         pattern = r"^([A-Za-z]+)"
#         matches = re.findall(pattern, i)
#         match.extend(matches)
# print(match)

# # Stop the timer and calculate the time taken
# end_time = time.time()

# # Calculate and print the time taken by the program
# execution_time = end_time - start_time
# print(f"Time taken by the program: {execution_time} seconds")
