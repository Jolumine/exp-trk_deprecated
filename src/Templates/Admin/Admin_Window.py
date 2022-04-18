from PyQt5.QtWidgets import QDialog, QPushButton, QComboBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon

from ...vars import Admin_Logo, Wrong_Logo
from .Change_User_Infos import Change_Window
from ...algos import get_all_user, get_folder_number, get_password

import os

class Admin_Window(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.all = []
        self.all.append("Username-Firstname-Lastname")
        
        for i in get_all_user(): 
            output = f"{i[0]}-{i[1]}-{i[2]}"
            self.all.append(output)

        self.combo = QComboBox(self)
        self.combo.setToolTip("Select the user")
        self.combo.addItems(self.all)

        self.deleteButton = QPushButton("Delete", self)
        self.deleteButton.setToolTip("Click to finally delete the selected User")
        self.deleteButton.clicked.connect(self.delete)

        self.modify = QPushButton("Modify", self)
        self.modify.setToolTip("Click to modify the selected User")
        self.modify.clicked.connect(self.mod)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.modify)
        
        self.setGeometry(400, 400, 450, 600)
        self.setWindowTitle("Administrator")
        self.setWindowIcon(QIcon(Admin_Logo))
        self.setLayout(layout)
        self.exec_()


    def delete(self):
        root = f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users"
        selected = self.combo.currentText()
        splitted = selected.split("-")

        if selected == "Username-Firstname-Lastname":
            info = QDialog()
            info.setWindowTitle("Deletion failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(500, 500, 320, 100)
            infotext = QLabel(info)
            infotext.setText("This isn't a real user, select an exisiting User...")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
                
            info.exec_()  
        else:
            os.remove(f"C:/Users/{os.getlogin()}/AppData/local/Expense_Tracker/users/{get_folder_number(splitted[0], get_password(splitted[0]))}")


    def mod(self):
        selected = self.combo.currentText()
        splitted = selected.split("-")
        if selected == "Username-Firstname-Lastname":
            info = QDialog()
            info.setWindowTitle("Modification failed")
            info.setWindowIcon(QIcon(Wrong_Logo))
            info.setGeometry(500, 500, 320, 100)
            infotext = QLabel(info)
            infotext.setText("This isn't a real user, select an exisiting User...")
            info_layout = QVBoxLayout()
            info_layout.addWidget(infotext)
            info.setLayout(info_layout)
                
            info.exec_()  
        else:
            self.close()
            dial = Change_Window(splitted)
        
        