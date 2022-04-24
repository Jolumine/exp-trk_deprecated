from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from ...vars import log_file, Stats_Logo
from .Calc_Stats import get_expenses_sum, get_income_sum, get_sum_passive

import os
import json

class Statistic_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active
        self.active_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}"

        self.balance_label = QLabel(self)
        self.balance_label.setText("Account balance: ")

        self.balance = QLineEdit(self)
        self.balance.setReadOnly(True)
        self.balance.setAlignment(Qt.AlignCenter)
        self.balance.setText(str((get_income_sum(self.active_path)-get_expenses_sum(self.active_path)))+self.get_currency())

        self.balance_exp_label = QLabel(self)
        self.balance_exp_label.setText("Sum of expenses: ")
        
        self.sum_exp = QLineEdit(self)
        self.sum_exp.setReadOnly(True)
        self.sum_exp.setAlignment(Qt.AlignCenter)
        self.sum_exp.setText(str(get_expenses_sum(self.active_path))+self.get_currency())

        self.balance_in_label = QLabel(self)
        self.balance_in_label.setText("Sum of income: ")

        self.sum_in = QLineEdit(self)
        self.sum_in.setReadOnly(True)
        self.sum_in.setAlignment(Qt.AlignCenter)
        self.sum_in.setText(str(get_income_sum(self.active_path))+self.get_currency())

        self.passive_label = QLabel(self)
        self.passive_label.setText("Sum of passive income: ")

        self.passive = QLineEdit(self)
        self.passive.setReadOnly(True)
        self.passive.setAlignment(Qt.AlignCenter)
        self.passive.setText(str(get_sum_passive(self.active_path))+self.get_currency())

        balance_layout = QHBoxLayout()
        balance_layout.addWidget(self.balance_label)
        balance_layout.addWidget(self.balance)

        balance_exp_layout = QHBoxLayout()
        balance_exp_layout.addWidget(self.balance_exp_label)
        balance_exp_layout.addWidget(self.sum_exp)

        balance_in_layout = QHBoxLayout()
        balance_in_layout.addWidget(self.balance_in_label)
        balance_in_layout.addWidget(self.sum_in)

        passive_layout = QHBoxLayout()
        passive_layout.addWidget(self.passive_label)
        passive_layout.addWidget(self.passive)

        root = QVBoxLayout()
        root.addLayout(balance_layout)
        root.addLayout(balance_exp_layout)
        root.addLayout(balance_in_layout)
        root.addLayout(passive_layout)

        self.setWindowTitle("Profile Statistic")
        self.setGeometry(400, 400, 450, 550)
        self.setLayout(root)
        self.setWindowIcon(QIcon(Stats_Logo))
        self.exec_()

    def get_currency(self):
        with open(self.active_path+"\\settings.json", "r") as f:
            parsed = json.load(f)
            f.close()

        return f" {parsed['currency']}"
