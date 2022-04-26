from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon

from ...const import Login_Icon, Wrong_Logo, log_file, Eye_Logo
from .Admin_Window import Admin_Window

import os 
import json 
import logging

class Admin_Login(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.show_password = QPushButton(self)
        self.show_password.setFixedHeight(38)
        self.show_password.setIcon(QIcon(Eye_Logo))
        self.show_password.clicked.connect(self.show_pass_func)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.setToolTip("Click to login as Admin")
        self.loginButton.clicked.connect(self.login)

        password = QHBoxLayout()
        password.addWidget(self.password)
        password.addWidget(self.show_password)

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addLayout(password)
        layout.addWidget(self.loginButton)

        self.setGeometry(400, 400, 400, 700)
        self.setWindowTitle("Admin Login")
        self.setWindowIcon(QIcon(Login_Icon))
        self.setLayout(layout)
        self.exec_()


    def login(self): 
        username = self.username.text()
        password = self.password.text()

        admin_file = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/admin/admindata.json"

        file = open(admin_file, "r")

        parsed = json.load(file)

        if username == parsed["Admin Username"] and password == parsed["Admin Password"]: 
            self.close()
            dial = Admin_Window()
            
            logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info("Admin logged in.")
        else: 
            info = QDialog()
            info.setWindowTitle("Login failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(500, 500, 320, 100)
            infotext = QLabel(info)
            infotext.setText("The Username or password is incorrect, please retry...")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
            
            info.exec_()  

            logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info("Admin Login failed")


    def show_pass_func(self):
        if self.password.echoMode() == 0:
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.password.setEchoMode(QLineEdit.Normal)