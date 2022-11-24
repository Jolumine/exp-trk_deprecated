import matplotlib.pyplot as plt 
import numpy as np 

from ...const import wo_month, show_dict

import csv 
import os

class Math: 

    @classmethod
    def get_data(self, selected, active, year="", type=""): 
        all_amounts = []

        if year != "" and type != "":   
            if selected == "Expenses": 
                exp_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/expenses.csv"
                with open(exp_file, "r") as file: 
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Year"] == year and row["Type"] == type: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)
                    
                return all_amounts

            else: 
                rev_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/income.csv"
                with open(rev_file, "r") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Year"] == year and row["Type"] == type: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)


                return all_amounts

        elif year != "" and type == "":
            if selected == "Expenses": 
                exp_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/expenses.csv"
                with open(exp_file, "r") as file: 
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Year"] == year: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)

                return all_amounts
            else: 
                rev_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/income.csv"
                with open(rev_file, "r") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Year"] == year: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)

                return all_amounts

        elif year == "" and type != "":
            if selected == "Expenses": 
                exp_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/expenses.csv"
                with open(exp_file, "r") as file: 
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Type"] == type: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)

                return all_amounts

            else: 
                rev_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/income.csv"
                with open(rev_file, "r") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i and row["Type"] == type: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

            for v in show_dict.values():
                all_amounts.append(v)

            return all_amounts
        
        elif year == "" and type == "":
            if selected == "Expenses": 
                exp_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/expenses.csv"
                with open(exp_file, "r") as file: 
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)

                return all_amounts
            else: 
                rev_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/income.csv"
                with open(rev_file, "r") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        for i in wo_month: 
                            if row["Month"] == i: 
                                show_dict[i] += float(row["Amount"])
                            else: 
                                pass

                for v in show_dict.values():
                    all_amounts.append(v)

                return all_amounts
        else:
            pass 
        


    @classmethod
    def difference(self, active):
        x = np.arange(12)
        width = 0.2
        all_amounts_exp = []
        all_amounts_rev = []

        dict_exp = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

        dict_rev = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

        rev_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/income.csv"
        with open(rev_file, "r") as file_rev:
            reader_rev = csv.DictReader(file_rev)

            for row in reader_rev:
                for i in wo_month: 
                    if row["Month"] == i: 
                        dict_rev[i] += float(row["Amount"])
                    else: 
                        pass

        exp_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{active}/expenses.csv"
        with open(exp_file, "r") as file_exp: 
            reader_exp = csv.DictReader(file_exp)

            for row in reader_exp:
                for i in wo_month: 
                    if row["Month"] == i: 
                        dict_exp[i] += float(row["Amount"])
                    else: 
                        pass

        for v_exp in dict_exp.values():
            all_amounts_exp.append(v_exp)

        for v_rev in dict_rev.values():
            all_amounts_rev.append(v_rev)

        plt.figure(figsize=(13, 6))
        plt.bar(x-0.1, all_amounts_rev, width,color='black')
        plt.bar(x+0.1, all_amounts_exp, width,color="red")
        plt.legend(["Total Income", "Total Expenses"])
        plt.xticks(x, wo_month)
        plt.title("Difference beetween Revenue and Expenses")
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.show() 

    
    @classmethod
    def clean_data(self): 
        for key in show_dict.keys(): 
            show_dict[key] = 0

