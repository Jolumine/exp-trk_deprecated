from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

from ...algos import get_folder_number, get_password 
from ...vars import Wrong_Logo, log_file, Mod_Icon

import os
import json
import logging 

class Change_Window(QDialog):
    def __init__(self, selected, parent=None):
        super().__init__(parent)

        self.selected = selected

        global root
        root = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{get_folder_number(self.selected[0], get_password(self.selected[0]))}/data.json"

        file = open(root, "r")

        global parsed
        parsed = json.load(file)

        self.username = QLineEdit(self)
        self.username.setText(selected[0])
    
        self.Firstname = QLineEdit(self)
        self.Firstname.setText(selected[1])

        self.Lastname = QLineEdit(self)
        self.Lastname.setText(selected[2])

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

        if username == self.selected[0] and firstname == self.selected[1] and lastname == self.selected[2] and password == parsed["Password"]:
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setWindowIcon(QIcon(Wrong_Logo))
            msg.setText("Do you want to close the Window?")
            msg.setInformativeText("You changed nothing...")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.Cancel)
            rep = msg.exec_()

            if rep == QMessageBox.Cancel: 
                pass
            else: 
                msg.close()
                self.close()
        else:
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
            logging.error(f"{username} has been modified.")
            