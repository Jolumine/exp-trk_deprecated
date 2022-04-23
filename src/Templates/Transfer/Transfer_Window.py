from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QMessageBox
from PyQt5.QtGui import QIcon

from ...vars import Transfer_Logo, Warning_Logo, field_names
from ...algos import get_username_from_number, get_all_user, get_number_from_username

import csv 
import os 
import logging
import datetime

class Transfer_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active

        self.userlist = []

        for i in get_all_user(): 
            if i[0] == get_username_from_number(self.active):
                pass
            else: 
                self.userlist.append(i[0]) 

        self.from_label = QLabel(self)
        self.from_label.setText("From: ")

        self.from_user = QLineEdit(self)
        self.from_user.setText(get_username_from_number(self.active))
        self.from_user.setReadOnly(True)

        self.to_label = QLabel(self)
        self.to_label.setText("To: ")

        self.to = QComboBox(self)
        self.to.addItems(self.userlist)

        self.amount_label = QLabel(self)
        self.amount_label.setText("Amount: ")

        self.amount = QSpinBox(self)
        self.amount.setMaximum(3000)
        self.amount.setMinimum(1)
        self.amount.setToolTip("Enter the amount you want to transfer")

        self.transfer_btn = QPushButton("Transfer", self)
        self.transfer_btn.setToolTip("Click to transfer the amount")
        self.transfer_btn.clicked.connect(self.transfer) 

        from_layout = QHBoxLayout()
        from_layout.addWidget(self.from_label)
        from_layout.addWidget(self.from_user)

        to_layout = QHBoxLayout()
        to_layout.addWidget(self.to_label)
        to_layout.addWidget(self.to)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount)

        root = QVBoxLayout()
        root.addLayout(from_layout)
        root.addLayout(to_layout)
        root.addLayout(amount_layout)
        root.addWidget(self.transfer_btn)

        self.setWindowTitle("Transfer")
        self.setGeometry(500, 500, 500, 550)
        self.setWindowIcon(QIcon(Transfer_Logo))
        self.setLayout(root)
        self.exec_()

    def transfer(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setWindowIcon(QIcon(Warning_Logo))
        msg.setText("The name already exists!")
        msg.setInformativeText("Do you want to overwrite it?")
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Cancel)
        rep = msg.exec_()

        if rep == QMessageBox.Cancel: 
            msg.close()
            pass 
        else: 
            datetime_object = datetime.datetime.strptime(str(datetime.datetime.today().month), "%m")

            from_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\expenses.csv"
            to_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{get_number_from_username(self.to.currentText())}\\income.csv"
            amount = self.amount.value()
            day = datetime.datetime.now().day
            month = datetime_object.strftime("%B")
            year = datetime.datetime.now().month


            with open(from_path, "a") as from_f: 
                writer = csv.DictWriter(from_f, fieldnames=field_names, lineterminator="\n", delimiter=",")
                
                writer.writerow({"Amount": amount, "Day": day, "Month": month, "Year": year, "Type": "Transaction", "Description": f"Send to {self.to.currentText()}"})

                from_f.close()

            with open(to_path, "a") as to_f:
                writer = csv.DictWriter(to_f, fieldnames=field_names, lineterminator="\n", delimiter=",")

                writer.writerow({"Amount": amount, "Day": day, "Month": month, "Year": year, "Type": "Transaction", "Description": f"Send from {get_username_from_number(self.active)}"})

                to_f.close()

            self.close()

