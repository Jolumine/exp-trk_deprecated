from PyQt5.QtWidgets import QLineEdit, QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon

from ..vars import welcome_logo, log_file, Wrong_Logo, Eye_Logo

import logging 
import json 
import os 

class Welcome_Interface(QDialog):
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.click = False

        self.root_folder = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker"

        self.main_label = QLabel(self)
        self.main_label.setText("Before you go ahead and start You need to fill the Admin Login, \nwith which you can access the admin settings.")

        self.admin_username_label = QLabel(self)
        self.admin_username_label.setText("Admin Username: ")

        self.admin_username = QLineEdit(self)
        self.admin_username.setPlaceholderText("Admin Username")
        self.admin_username.setToolTip("Set the Admin Username")

        self.admin_password_label = QLabel(self)
        self.admin_password_label.setText("Admin Password: ")

        self.admin_password = QLineEdit(self)
        self.admin_password.setEchoMode(QLineEdit.Password)
        self.admin_password.setPlaceholderText("Admin Password")
        self.admin_password.setToolTip("Set the Admin Password")

        self.show_password = QPushButton(self)
        self.show_password.setFixedWidth(70)
        self.show_password.setIcon(QIcon(Eye_Logo))
        self.show_password.clicked.connect(self.show_pass_func)

        self.cont = QPushButton("Continue", self)
        self.cont.setToolTip("Click to continue")
        self.cont.clicked.connect(self.next)

        username = QHBoxLayout()
        username.addWidget(self.admin_username_label)
        username.addWidget(self.admin_username)

        password = QHBoxLayout()
        password.addWidget(self.admin_password_label)
        password.addWidget(self.admin_password)
        password.addWidget(self.show_password)

        root = QVBoxLayout()
        root.addWidget(self.main_label)
        root.addLayout(username)
        root.addLayout(password)
        root.addWidget(self.cont)

        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon(welcome_logo))
        self.setGeometry(300, 300, 450, 500)
        self.setLayout(root)
        self.exec_()

    def closeEvent(self, e) -> None:
        if self.click:
            e.accept()
        else: 
            e.ignore()

    def next(self):
        username = self.admin_username.text()
        password = self.admin_password.text()

        if username == "" or password == "":
            info = QDialog()
            info.setWindowTitle("Installation failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(50, 80, 320, 100)
            infotext = QLabel(info)
            infotext.setText("Please fill the Admin Username and the Admin Password")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
            
            info.exec_()
            logging.basicConfig(filename=log_file, level=logging.DEBUG, encoding="utf-8", format='%(asctime)s %(message)s')
            logging.info("Initilization failed")
        else:
            self.click = True
            data = {
                "Admin Username": self.admin_username.text(),
                "Admin Password": self.admin_password.text()
            }

            file = self.root_folder+"\\admin\\admindata.json"
            with open(file, "w") as f:
                parsed = json.dumps(data, indent=4, sort_keys=False)
                f.write(parsed)
                f.close()

            self.close()

            logging.basicConfig(filename=log_file, level=logging.DEBUG, encoding="utf-8", format='%(asctime)s %(message)s')
            logging.info("Initilization")


    def show_pass_func(self):
        if self.admin_password.echoMode() == 0:
            self.admin_password.setEchoMode(QLineEdit.Password)
        else:
            self.admin_password.setEchoMode(QLineEdit.Normal)