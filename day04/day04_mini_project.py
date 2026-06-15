import json
import os
def register_user(name,email,password):
    if os.path.exists("users.json"):
        with open("users.json","r")as f:
            users=json.load(f)
    else:
        users=[]
    
    
    for user in users:
        if user['email']==email:
            print("email already exists")
            return
    #since users is empty we add new users
    users.append({
        "name":name,
        "email":email,
        "password":password
    })
    with open("users.json","w")as f:
        json.dump(users,f,indent=4)   
    print(f"{name} registered successfully") 
def get_all_users():
    if os.path.exists("users.json"):
        with open("users.json",'r')as f:
            users=json.load(f)
        for user in users:
            print(f"Name:{user['name']}|Email:{user['email']}")   
    else:
        print("No users found")
def find_user(email):
    if os.path.exists("users.json"):
        with open ("users.json",'r')as f:
            users=json.load(f)
        found=False
        for user in users:
            if user['email']==email:
                print(f"Name:{user["name"]}|Email:{user['email']}")
                found=True
                break
        if not found:
            print("User not found")

register_user("Megshyam","meg@gmail.com","M123")
register_user("Rahul","rahul@gmail.com","R456")
register_user("Megshyam","meg@gmail.com","M123")
get_all_users()

find_user("meg@gmail.com")
find_user("wer@gmail.com")