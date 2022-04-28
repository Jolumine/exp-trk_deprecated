from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import log_file, Mod_Icon

import os
import json
import logging 

class Change_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active

        global root
        root = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{self.active}/data.json"

        file = open(root, "r")

        global parsed
        parsed = json.load(file)

        self.username = QLineEdit(self)
        self.username.setText(parsed["Username"])
    
        self.Firstname = QLineEdit(self)
        self.Firstname.setText(parsed["Firstname"])

        self.Lastname = QLineEdit(self)
        self.Lastname.setText(parsed["Lastname"])

        self.Password = QLineEdit(self)
        self.Password.setText(parsed["Password"])

        self.mod = QPushButton("Apply changes")
        self.mod.setToolTip("Click to apply the changes on this user")
        self.mod.clicked.connect(self.modify)

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.Firstname)
        layout.addWidget(self.Lastname)
        layout.addWidget(self.Password)
        layout.addWidget(self.mod)

        self.setWindowTitle("Modify Menu")
        self.setWindowIcon(QIcon(Mod_Icon))
        self.setGeometry(500, 500, 550, 650)
        self.setLayout(layout)
        self.exec_()

    def modify(self):
        username = self.username.text()
        firstname = self.Firstname.text()
        lastname = self.Lastname.text()
        password = self.Password.text()

        with open(root, "r") as file: 
            data = json.load(file)

            data["Username"] = username
            data["Firstname"] = firstname
            data["Lastname"] = lastname
            data["Password"] = password
            file.close()

        with open(root, "w") as file:
            file.close()


        with open(root, "r+") as file: 
            json.dump(data, file, indent=4, sort_keys=False)
            file.close()

            self.close()

        logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
        logging.info(f"{username} has been modified.")


