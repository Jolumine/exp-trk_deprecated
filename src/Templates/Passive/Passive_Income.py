from PyQt5.QtWidgets import QDialog, QPushButton, QComboBox, QLineEdit, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QSpinBox
from PyQt5.QtGui import QIcon

from ...vars import Money_Logo, routines, types, Information_Logo

import json
import os


class Passive_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active
        self.active_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\data.json"

        self.name_label = QLabel(self)
        self.name_label.setText("Name: ")

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Name")
        self.name.setToolTip("Enter the name of the income source")

        self.amount_label = QLabel(self)
        self.amount_label.setText("Amount")

        self.amount = QSpinBox(self)
        self.amount.setMinimum(1)
        self.amount.setMaximum(100000)
        self.amount.setToolTip("Enter the amount which will be automatically added to your income")

        self.repeat_label = QLabel(self)
        self.repeat_label.setText("Repeat: ")

        self.repeat = QComboBox(self)
        self.repeat.addItems(routines)

        self.type_label = QLabel(self)
        self.type_label.setText("Type of income: ")

        self.type = QComboBox(self)
        self.type.addItems(types)

        self.descr_label = QLabel(self)
        self.descr_label.setText("More Information: ")

        self.descr = QTextEdit(self)
        self.descr.setPlaceholderText("More information")
        self.descr.setFixedHeight(60)
        self.descr.setFixedWidth(200)

        self.addbtn = QPushButton("Add", self)
        self.addbtn.setToolTip("Click to add this source to your profile")
        self.addbtn.clicked.connect(self.add)

        name_layout = QHBoxLayout()
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount)

        rep_layout = QHBoxLayout()
        rep_layout.addWidget(self.repeat_label)
        rep_layout.addWidget(self.repeat)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type)

        descr_layout = QHBoxLayout()
        descr_layout.addWidget(self.descr_label)
        descr_layout.addWidget(self.descr)

        root = QVBoxLayout()
        root.addLayout(name_layout)
        root.addLayout(amount_layout)
        root.addLayout(rep_layout)
        root.addLayout(type_layout)
        root.addLayout(descr_layout)
        root.addWidget(self.addbtn)

        self.setWindowTitle("Passive Income Configuration")
        self.setWindowIcon(QIcon(Money_Logo))
        self.setGeometry(400, 400, 550, 850)
        self.setLayout(root)
        self.exec_()

    def add(self):
        name = self.name.text()
        amount = self.amount.value()
        repeat = self.repeat.currentText()
        selected_type = self.type.currentText()
        description = self.descr.toPlainText()

        with open(self.active_path, "r") as main_file: 
            parsed = json.load(main_file)
            main_file.close()

        if name in parsed["passive income"]: 
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setWindowIcon(QIcon(Information_Logo))
            msg.setText("The name already exists!")
            msg.setInformativeText("Do you want to overwrite it?")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.Cancel)
            rep = msg.exec_()

            if rep == QMessageBox.Cancel: 
                pass
            else: 
                with open(self.active_path, "w") as file: 
                    parsed["passive income"][name] = {"Name": name, "Amount": amount, "Repeated" : repeat,"Type": selected_type, "Description": description}

                    json.dump(parsed, file, indent=4, sort_keys=False)

                msg.close()
                self.close() 
        else: 
            with open(self.active_path, "w") as file: 
                parsed["passive income"][name] = {"Name": name, "Amount": amount, "Repeated" : repeat,"Type": selected_type, "Description": description}

                json.dump(parsed, file, indent=4, sort_keys=False)

            self.close()