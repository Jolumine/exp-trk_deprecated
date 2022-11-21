from PyQt5.QtWidgets import QComboBox, QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import Delete_Logo

import json 
import os

class Delete_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active
        self.active_user_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\data.json"
        self.all = []

        with open(self.active_user_path, "r") as file: 
            self.parsed = json.load(file)
            
            for k in self.parsed["passive income"]: 
                self.all.append(f"{k}-{self.parsed['passive income'][k]['Amount']}-{self.parsed['passive income'][k]['Repeated']}-Income")

            for k in self.parsed["passive expense"]:
                self.all.append(f"{k}-{self.parsed['passive expense'][k]['Amount']}-{self.parsed['passive expense'][k]['Repeated']}-Expense")

        self.sources = QComboBox(self)
        self.sources.setToolTip("List of every listed passive income")
        self.sources.addItems(self.all)

        self.deletebtn = QPushButton("Delete", self)
        self.deletebtn.setToolTip("Click to delete the selected")
        self.deletebtn.clicked.connect(self.delete)

        root = QVBoxLayout()
        root.addWidget(self.sources)
        root.addWidget(self.deletebtn)

        self.setWindowTitle("Delete Passive Income")
        self.setWindowIcon(QIcon(Delete_Logo))
        self.setGeometry(500, 500, 500, 400)
        self.setLayout(root)
        self.exec_()

    def delete(self):
        selected = self.sources.currentText()
        splitted = selected.split("-")

        if splitted[0] in self.parsed["passive income"] and splitted[0] == "income":
            del self.parsed["passive income"][splitted[0]]

            with open(self.active_user_path, "w") as f: 
                json.dump(self.parsed, f, indent=4, sort_keys=False)
                f.close()
            
            self.close()

        elif splitted[0] in self.parsed["passive expense"] and splitted[3] == "expense":
            del self.parsed["passive expense"][splitted[0]]

            with open(self.active_user_path, "w") as f: 
                json.dump(self.parsed, f, indent=4, sort_keys=False)
                f.close()
            
            self.close()
        else: 
            pass 

        