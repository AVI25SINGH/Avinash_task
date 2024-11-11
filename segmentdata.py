import re

with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
    data = file.read()  # Reads the entire file content
    
    data_value=data.split("~")
    match=[]
    for i in data_value:
 
       pattern =r"^([A-Za-z]+)"
       matches = re.findall(pattern, i)

       match.extend(matches)
print(match)


# with normally
# import re

# with open("C:\\Users\\Avinash singh\\Downloads\\dataencrepted.txt", 'r') as file:
#     data = file.read()  # Reads the entire file content
#     # print(data) # data show
#     data_value=data.split("~")
#     match=[]
#     for i in data_value:
#        print(i)# show all data in line
#        dataa=(i.split('*')[0])
#        match.append(dataa)
# print(match)


       


