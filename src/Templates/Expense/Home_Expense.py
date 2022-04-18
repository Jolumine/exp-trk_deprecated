from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...vars import Money_Logo
from .Add_Expense import Add_Expense
from .Delete_Expense import Delete_Expense

import csv 
import os 

class Home_Expense(QDialog): 
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)

        self.active = active_user

        self.add = QPushButton("Add Expense", self)
        self.add.setToolTip("Click to open the Add Menu")
        self.add.clicked.connect(self.Add)

        self.delete = QPushButton("Delete Expense")
        self.delete.setToolTip("Click to open the Delete Menu")
        self.delete.clicked.connect(self.Delete)

        self.plot = QPushButton("Show Expenses", self)
        self.plot.setToolTip("Click to show every Expense in a Graph")
        self.plot.clicked.connect(self.Show)

        layout = QVBoxLayout()
        layout.addWidget(self.add)
        layout.addWidget(self.delete)
        layout.addWidget(self.plot)

        self.setWindowTitle("Expenses")
        self.setWindowIcon(QIcon(Money_Logo))
        self.setLayout(layout)
        self.setGeometry(400, 400, 500, 750)
        self.exec_()


    def Add(self): 
        add = Add_Expense(self.active) 

    def Delete(self): 
        delete = Delete_Expense(self.active)

    def Show(self):
        pass 