from PyQt5.QtWidgets import QLineEdit, QDialog, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from Crypto.PublicKey import RSA

from ...algos import get_new_number
from ...vars import New_User_Logo, Wrong_Logo, log_file, std_settings

import os 
import json 
import logging 

class New_User(QDialog): 
    def __init__(self): 
        super().__init__()

        self.root_folder = "C:\\Users\\Leonard Becker\\AppData/local\\Expense_Tracker"

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")

        self.fname = QLineEdit(self)
        self.fname.setPlaceholderText("Firstname")
        
        self.lname = QLineEdit(self)
        self.lname.setPlaceholderText("Lastname")

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")

        self.confirm = QLineEdit(self)
        self.confirm.setPlaceholderText("Confirm Password")

        self.create = QPushButton("Create", self)
        self.create.setToolTip("Click to create your user")
        self.create.clicked.connect(self.add)

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.fname)
        layout.addWidget(self.lname)
        layout.addWidget(self.password)
        layout.addWidget(self.confirm)
        layout.addWidget(self.create)

        self.setWindowTitle("New User")
        self.setGeometry(400, 400, 550, 750)
        self.setWindowIcon(QIcon(New_User_Logo))
        self.setLayout(layout)
        self.exec_()

    def add(self): 
        username = self.username.text()
        firstname = self.fname.text()
        lastname = self.lname.text()
        password = self.password.text()
        confirm = self.confirm.text()

        if password != confirm: 
            info = QDialog()
            info.setWindowTitle("Creation failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(50, 80, 320, 100)
            infotext = QLabel(info)
            infotext.setText("The passwords aren't the same, please retry")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
            
            info.exec_()

        elif username == "" or firstname == "" or lastname == "" or password == "" or confirm == "": 
            info = QDialog()
            info.setWindowTitle("Creation failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(50, 80, 320, 100)
            infotext = QLabel(info)
            infotext.setText("The Data isn't fully completed, please fill every part.")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
            
            info.exec_()

        else: 
            folder_name = get_new_number()

            os.chdir(self.root_folder+"/users")

            os.mkdir(folder_name) 

            os.chdir(self.root_folder+"/users/"+folder_name)

            os.mkdir("keys")

            with open(self.root_folder+"\\users\\"+folder_name+"\\settings.json", "w") as sett: 
                parsed = json.dumps(std_settings, indent=4, sort_keys=False)
                sett.write(parsed)
                sett.close()

            exp_file = open(self.root_folder+"\\users\\"+folder_name+"\\expenses.csv", "w")
            exp_file.write("Amount,Day,Month,Year,Type,Description\n")
            exp_file.close()

            in_file = open(self.root_folder+"\\users\\"+folder_name+"\\income.csv", "w")
            in_file.write("Amount,Day,Month,Year,Type,Description\n")
            in_file.close()

            seckey = RSA.generate(1024)
            with open(f"{self.root_folder}/users/{folder_name}/keys/seckey.pem", "wb") as file: 
                file.write(seckey.export_key(format="PEM"))
                file.close()

            pblkey = seckey.publickey()
            with open(f"{self.root_folder}/users/{folder_name}/keys/pblkey.pem", "wb") as file: 
                file.write(pblkey.export_key(format="PEM"))
                file.close()


            dict = {
                "Username": username, 
                "Password": password, 
                "Firstname": firstname, 
                "Lastname": lastname,
                "passive income": {},
                "passive expense": {}
            }


            with open(self.root_folder+"\\users\\"+folder_name+"\\data.json", "w") as f: 
                parsed = json.dumps(dict, indent=4, sort_keys=False)

                f.write(parsed)

                f.close()

            self.close()

        logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
        logging.info(f"User with the username {username} has been created.")
            

            

        