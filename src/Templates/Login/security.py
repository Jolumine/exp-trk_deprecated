import json 
import os 


def check_login(username, password) -> bool: 
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    for i in all: 
        file = path + f"\\{i}\\data.json"

        with open(file, "r") as f: 
            parsed = json.load(f)

            if parsed["Username"] == username and parsed["Password"] == password: 
                return True
            else:
                pass
