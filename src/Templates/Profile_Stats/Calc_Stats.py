import csv 
import json
import os

field_names = ["Amount", "Day", "Month", "Year", "Type", "Description"]

path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\1"

def get_income_sum(path) -> int:
    sum = 0
    with open(path+"\\income.csv", "r") as f:
        reader = csv.DictReader(f, fieldnames=field_names)

        for row in reader: 
            if row["Amount"] == "Amount":
                pass 
            else:
                sum+=int(row["Amount"])

        f.close()

    return sum

def get_expenses_sum(path) -> int:
    sum = 0
    with open(path+"\\expenses.csv", "r") as f:
        reader = csv.DictReader(f, fieldnames=field_names)

        for row in reader: 
            if row["Amount"] == "Amount":
                pass 
            else:
                sum+=int(row["Amount"])

        f.close()

    return sum

def get_sum_passive(path) -> int:
    data = path + "\\data.json"
    sum = 0

    with open(data, "r") as f:
        parsed = json.load(f)
        f.close()

    for k in parsed["passive income"]:
        sum+=int(parsed["passive income"][k]["Amount"])

    return sum

