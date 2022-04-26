import json 
import os 
import csv
from datetime import date, datetime

from ...const import field_names

def get_passive_sources(active) -> list:
    main_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{active}\\data.json"

    all_infos = []

    with open(main_path, "r") as file:
        parsed_data = json.load(file)
        file.close()

    for k in parsed_data["passive income"]:
        all_infos.append((k, parsed_data["passive income"][k]["Amount"], parsed_data["passive income"][k]["Repeated"]))

    return all_infos



def is_existing(tuple, active) -> bool:
    date = datetime.now()

    income_csv_file = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{active}\\income.csv"

    routine = tuple[2]

    if routine == "daily":
        with open(income_csv_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)

            erg = False

            for row in reader: 
                if row["Amount"] == "Amount":
                    pass 
                else: 
                    if row["Amount"] == str(tuple[1]) and row["Day"] == str(date.today().day) and row["Type"] == "Passive Income" and row["Description"] == tuple[0]: 
                        erg = True 
                    else: 
                        pass
        
        return erg 
    
    elif routine == "weekly":
        with open(income_csv_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)

            erg = False

            for row in reader: 
                if row["Amount"] == "Amount":
                    pass 
                else: 
                    if row["Amount"] == str(tuple[1]) and row["Day"] > str(date.today().day-7) and row["Type"] == "Passive Income" and row["Description"] == tuple[0]: 
                        erg = True 
                    else: 
                        pass

        return erg 

    elif routine == "monthly":
        with open(income_csv_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)

            erg = False

            for row in reader: 
                if row["Amount"] == "Amount":
                    pass 
                else: 
                    if row["Amount"] == str(tuple[1]) and row["Month"] == str(date.strftime("%B")) and row["Type"] == "Passive Income" and row["Description"] == tuple[0]: 
                        erg = True 
                    else: 
                        pass
        
        return erg 

    else: 
        with open(income_csv_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)

            erg = False

            for row in reader: 
                if row["Amount"] == "Amount":
                    pass 
                else: 
                    if row["Amount"] == str(tuple[1]) and row["Year"] == str(date.today().year) and row["Type"] == "Passive Income" and row["Description"] == tuple[0]: 
                        erg = True 
                    else: 
                        pass
        
        return erg 

     

def check_transfer_income(active) -> bool:
    datetime_object = datetime.strptime(str(datetime.today().month), "%m")
    all = get_passive_sources(active)
    
    income_csv_file = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{active}\\income.csv"

    for tuple in all: 
        if is_existing(tuple, active):
            pass
        else: 
            with open(income_csv_file, "a") as file: 
                writer = csv.DictWriter(file, fieldnames=field_names, delimiter=",", lineterminator="\n")

                day = date.today().day
                month = datetime_object.strftime("%B")
                year = date.today().year

                writer.writerow({"Amount": tuple[1], "Day": day, "Month": month, "Year": year, "Type": "Passive Income", "Description": tuple[0]})

