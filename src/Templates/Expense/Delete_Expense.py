from PyQt5.QtWidgets import QDialog, QComboBox, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import Delete_Logo, field_names

import csv 
import os 


class Delete_Expense(QDialog):
    def __init__(self, active_user,parent=None): 
        super().__init__(parent)

        self.active = active_user

        all = []
        self.file = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\expenses.csv"

        with open(self.file, "r") as f: 
            reader = csv.DictReader(f, fieldnames=field_names)

            for row in reader: 
                output = row["Amount"] + "€-" + row["Day"] + "-" + row["Month"] + "-" + row["Year"]
                if output == "Amount€-Day-Month-Year":
                    pass 
                else: 
                    all.append(output)
                
            

        self.all = QComboBox(self)
        self.all.setToolTip("Select the Expense you want to delete")
        self.all.addItems(all)

        self.delete = QPushButton("Delete", self)
        self.delete.setToolTip("Click to delete the Expense")
        self.delete.clicked.connect(self.DeleteExp)
        
        layout = QVBoxLayout()
        layout.addWidget(self.all)
        layout.addWidget(self.delete)

        self.setWindowIcon(QIcon(Delete_Logo))
        self.setWindowTitle("Delete Expense")
        self.setGeometry(500, 500, 400, 550)
        self.setLayout(layout)
        self.exec_()


    def DeleteExp(self):
        selected = self.all.currentText()
        splitted = selected.split("-")
        update = []

        with open(self.file, "r", newline='') as file: 
            reader = csv.DictReader(file)
            for row in reader: 
                if row["Amount"] + "€" == splitted[0] and row["Day"] == splitted[1] and row["Month"] == splitted[2] and row["Year"] == splitted[3]:
                    pass 
                else: 
                    update.append(row)

        with open(self.file, "w", newline="") as f: 
            f.close()


        with open(self.file, "a", newline="") as f: 
            f.write("Amount,Day,Month,Year,Type,Description\n")

            writer = csv.DictWriter(f, fieldnames=field_names, delimiter=",")

            for i in range(len(update)):
                amount = update[i]["Amount"]
                day = update[i]["Day"]
                month = update[i]["Month"]
                year = update[i]["Year"]
                typ = update[i]["Type"]
                descr = update[i]["Description"]

                row = {"Amount": amount, "Day" : day, "Month" : month, "Year": year, "Type" : typ, "Description": descr}
                writer.writerow(row)

        self.close() 