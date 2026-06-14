# f=open("test.txt",'w')
# f.write(" Hello Megshyam \n")
# f.write("This is day 4 \n")
# f.close()
# print("File created successfully")
# # if this code fails before close it will never run
# with open("test.test","w")as f :
#     f.write("Hello Megshyam \n")
#     f.write("This is Day 4 \n")
# print("Done")

# with open("day04/test.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("day04/test.txt","r") as f:
#     for line in f:
#         print(line.strip())
# with open ("day04/test.txt","r") as f:
#     lines=f.readlines()
#     print(lines)


# with open("test.txt","r")as f:
#     print("before append ")
#     print(f.read())
# with open("test.txt","a")as f:
#     f.write("This was added in this file .\n")
# with open("test.txt",'r')as f:
#     print("After adding data \n")
#     print(f.read())

# # ---json files---
import json
# user={
#     "name":"Megshyam",
#     "age":23,
#     "city":"Nagpur"

#     }
# #save dictionary to json file
# with open ("day04/users.json","w")as f:
#     json.dump(users,f,indent=4)
# print("Json file created")

# #read json file as dictionary
# with open("day04/users.json",'r')as f:
#     data=json.load(f)
# print(data)
# print(data['name'])
# print(data['city'])




users=[
    {"name":"Megshyam","age":22,"city":"Nagpur"},
    {"name":"Rahul","age":23,"city":"Mumbai"},
    {"name":"Priya","age":21,"city":"Pune"}
]
with open("users.json",'w')as f:
    json.dump(users,f,indent=4)
print("USERS json created successfully")
with open("users.json","r")as f:
    print("trying ot load json")
    data=json.load(f)
for user in data:
    print(f"{user['name']} from {user['city']}")
