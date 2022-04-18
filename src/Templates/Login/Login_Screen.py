from PyQt5.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QDialog, QLabel
from PyQt5.QtGui import QIcon

from ..Admin.Admin_Login import Admin_Login 
from .New_User import New_User
from ..Home import Root_Window

from ...vars import Login_Icon, Eye_Logo, Wrong_Logo, log_file

from .security import check_login
from ...algos import get_folder_number

import logging 

class Login_Page(QDialog): 
    def __init__(self): 
        super().__init__()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.setToolTip("Enter your username")
        
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setToolTip("Enter your password")

        self.showPassword = QPushButton(self)
        self.showPassword.setIcon(QIcon(Eye_Logo))
        self.showPassword.setToolTip("Click to show or hide your password")
        self.showPassword.setFixedHeight(38)
        self.showPassword.clicked.connect(self.showPassFunc)

        self.login = QPushButton("Login", self)
        self.login.setToolTip("Click to login")
        self.login.clicked.connect(self.loginFunction)

        self.admin = QPushButton("Admin", self)
        self.admin.setToolTip("Click to get access to the Admin Window")
        self.admin.clicked.connect(self.Admin)

        self.new = QPushButton("New User", self)
        self.new.setToolTip("Click to create a new User")
        self.new.clicked.connect(self.newUser)
        
        self.exit = QPushButton("Exit", self)
        self.exit.setToolTip("Click to exit")
        self.exit.clicked.connect(self.close)

        password = QHBoxLayout()
        password.addWidget(self.password)
        password.addWidget(self.showPassword)

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addLayout(password)
        layout.addWidget(self.login)
        layout.addWidget(self.admin)
        layout.addWidget(self.new)
        layout.addWidget(self.exit)

        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 400, 700)
        self.setWindowIcon(QIcon(Login_Icon))
        self.setLayout(layout)
        self.show()

    def loginFunction(self) -> None: 
        username = self.username.text()
        password = self.password.text()
        folder_number = get_folder_number(username, password)
        if check_login(username, password): 
            self.close()
            root = Root_Window(folder_number)
            logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info(f"{username} is logged in.")
        else: 
            info = QDialog()
            info.setWindowTitle("Login failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(300, 300, 320, 100)
            infotext = QLabel(info)
            infotext.setText("The Username or password is incorrect, please retry...")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
            
            info.exec_() 

            logging.basicConfig(filename=log_file, encoding="utf-8", format='%(asctime)s %(message)s', level=logging.DEBUG)
            logging.info(f"Login failed.")

    def newUser(self): 
        interface = New_User()

    def Admin(self): 
        dial = Admin_Login()


    def showPassFunc(self):
        if self.password.echoMode() == 0:
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.password.setEchoMode(QLineEdit.Normal)