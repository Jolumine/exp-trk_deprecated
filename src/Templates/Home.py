from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from ..vars import * 
from .Plot.Plot_Window import Plot_Window
from .Expense.Home_Expense import * 
from .Revenue.Home_Income import * 


class Root_Window(QDialog): 
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)
        self.active_user = active_user

        self.exp_label = QLabel(self)
        self.exp_label.setText("Expenses Menu: ")

        self.Expense = QPushButton("Expenses", self)
        self.Expense.setToolTip("Click to open the Menu for Expenses")
        self.Expense.clicked.connect(self.expense)

        self.rev_label = QLabel(self)
        self.rev_label.setText("Revenue Menu: ")

        self.Revenue = QPushButton("Revenues", self)
        self.Revenue.setToolTip("Click to open the Menu for your Revenues")
        self.Revenue.clicked.connect(self.revenue)

        self.plot_label = QLabel(self)
        self.plot_label.setText("Plot Menu: ")

        self.Plot = QPushButton("Plot", self)
        self.Plot.setToolTip("Click to open the Plot Menu")
        self.Plot.clicked.connect(self.plot)

        expense_layout = QHBoxLayout()
        expense_layout.addWidget(self.exp_label)
        expense_layout.addWidget(self.Expense)

        rev_layout = QHBoxLayout()
        rev_layout.addWidget(self.rev_label)
        rev_layout.addWidget(self.Revenue)

        plt_layout = QHBoxLayout()
        plt_layout.addWidget(self.plot_label)
        plt_layout.addWidget(self.Plot)

        root = QVBoxLayout()
        root.addLayout(expense_layout)
        root.addLayout(rev_layout)
        root.addLayout(plt_layout)

        self.setWindowTitle("Home")
        self.setLayout(root)
        self.setGeometry(300, 300, 500, 750)
        self.setWindowIcon(QIcon(Main_Logo))
        self.exec_()


    def expense(self): 
        dialog = Home_Expense(self.active_user) 

    def revenue(self): 
        dialog = Home_Income(self.active_user)

    def plot(self): 
        dialog = Plot_Window(self.active_user) 
    