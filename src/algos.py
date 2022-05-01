import os 
import json 

from .Templates.Login.security import get_hash

def get_all_user() -> list: 
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    details = []

    for i in all: 
        path = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{i}/data.json"

        file = open(path, "r")
            
        data = json.load(file)
             
        parsed = [data["Username"], data["Firstname"], data["Lastname"]]

        details.append(parsed)
        
    return details 
 
def get_new_number() -> str:
    path = f"C:/Users/{os.getlogin()}/AppData\\local/Expense_Tracker/users"

    all = []

    for i in os.listdir(path):
        all.append(i)

    
    return str(len(all)+1)


def get_folder_number(username, password) -> str: 
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    for i in all: 
        file = path + f"\\{i}\\data.json"

        with open(file, "r") as f: 
            parsed = json.load(f)

            if parsed["Username"] == username and parsed["Password"] == get_hash(password): 
                return i
            else:
                pass

def get_username_from_number(number) -> str:
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    for i in all: 
        if i == number:
            file = path + f"\\{i}\\data.json"

            with open(file, "r") as f: 
                parsed = json.load(f)
                
                return parsed["Username"]
                

def get_number_from_username(username) -> str: 
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    for i in all: 
        file = path + f"\\{i}\\data.json"

        with open(file, "r") as f: 
            parsed = json.load(f)

            if parsed["Username"] == username: 
                return i
            else: 
                pass 