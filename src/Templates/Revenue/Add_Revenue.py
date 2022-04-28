from PyQt5.QtWidgets import QComboBox, QLabel, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QDoubleSpinBox
from PyQt5.QtGui import QIcon

from ...const import Add_Logo, months, years, types, days, field_names
import csv 

class Add_Income(QDialog):
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)

        self.active = active_user

        self.amount_label = QLabel(self)
        self.amount_label.setText("Amount: ")

        self.amount = QDoubleSpinBox(self)
        self.amount.setToolTip("Enter the amount")
        self.amount.setMaximum(10000)

        self.day_label = QLabel(self)
        self.day_label.setText("Day: ")

        self.day = QComboBox(self)
        self.day.setToolTip("Enter the number of the day")
        self.day.addItems(days)
        
        self.month_label = QLabel(self)
        self.month_label.setText("Month: ")

        self.month = QComboBox(self)
        self.month.setToolTip("Enter the actual month")
        self.month.addItems(months)

        self.year_label = QLabel(self)
        self.year_label.setText("Year: ")

        self.year = QComboBox(self)
        self.year.setToolTip("Set the actual year")
        self.year.addItems(years)

        self.type_label = QLabel(self)
        self.type_label.setText("Type: ")

        self.type = QComboBox(self)
        self.type.addItems(types)

        self.descr_label = QLabel(self)
        self.descr_label.setText("Description: ")

        self.descr = QTextEdit(self)
        self.descr.setFixedHeight(60)
        self.descr.setFixedWidth(200)

        self.add = QPushButton("Add", self)
        self.add.setToolTip("Click to add the Expense")
        self.add.clicked.connect(self.AddRev)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount)

        day_layout = QHBoxLayout()
        day_layout.addWidget(self.day_label)
        day_layout.addWidget(self.day)

        month_layout = QHBoxLayout()
        month_layout.addWidget(self.month_label)
        month_layout.addWidget(self.month)

        year_layout = QHBoxLayout()
        year_layout.addWidget(self.year_label)
        year_layout.addWidget(self.year)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type)

        descr_layout = QHBoxLayout()
        descr_layout.addWidget(self.descr_label)
        descr_layout.addWidget(self.descr)

        root = QVBoxLayout()
        root.addLayout(amount_layout)
        root.addLayout(day_layout)
        root.addLayout(month_layout)
        root.addLayout(year_layout)
        root.addLayout(type_layout)
        root.addLayout(descr_layout)
        root.addWidget(self.add)

        self.setWindowIcon(QIcon(Add_Logo))
        self.setWindowTitle("Add Revenue")
        self.setGeometry(500, 500, 400, 550)
        self.setLayout(root)
        self.exec_()

    def AddRev(self): 
        amount = self.amount.value()
        day = self.day.currentText()
        month = self.month.currentText()
        year = self.year.currentText()
        typ = self.type.currentText()
        descr = self.descr.toPlainText()

        file = f"C:\\Users\\Leonard Becker\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\income.csv"

        with open(file, "a") as f: 
            writer = csv.DictWriter(f, fieldnames=field_names, lineterminator="\n")

            data = {
                "Amount": amount, 
                "Day": day, 
                "Month": month, 
                "Year": year,
                "Type":typ,
                "Description": descr
            }

            writer.writerow(data)
            f.close()

        self.close()