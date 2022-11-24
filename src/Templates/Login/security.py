import json 
import os 
import hashlib


def check_login(username, password) -> bool: 
    path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users" 

    all = os.listdir(path)

    for i in all: 
        file = path + f"\\{i}\\data.json"

        with open(file, "r") as f: 
            parsed = json.load(f)

            if parsed["Username"] == username and parsed["Password"] == get_hash(password): 
                return True
            else:
                pass


def get_hash(message: str):
    return hashlib.sha3_512(message.encode("utf-8")).hexdigest()

