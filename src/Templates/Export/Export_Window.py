from PyQt5.QtWidgets import QPushButton, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout, QComboBox, QFileDialog, QDialog
from PyQt5.QtGui import QIcon

import json
import os
import logging
import csv

from ...vars import log_file, months_all, Export_Logo


class Export_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)
        self.root_folder = f"C://Users//{os.getlogin()}//AppData//local//Expense_Tracker//users"

        self.active_user = active
        self.file_path = ""

        self.month_label = QLabel(self)
        self.month_label.setText("Month")

        self.month = QComboBox(self)
        self.month.addItems(months_all)

        self.file_label = QLabel(self)
        self.file_label.setText("File: ")

        self.file = QPushButton("Select", self)
        self.file.setToolTip(
            "Click to select a file where the data is written")
        self.file.clicked.connect(self.getFile)

        self.doc_check = QCheckBox(self)
        self.doc_check.setText("Personel Documents")
        self.doc_check.setToolTip(
            "Check to export the data into your Document Section")
        self.doc_check.setChecked(False)
        self.doc_check.stateChanged.connect(self.value_changed)

        self.desk_check = QCheckBox(self)
        self.desk_check.setText("Personel Desktop")
        self.desk_check.setToolTip(
            "Check to export the data on to your Desktop")
        self.desk_check.setChecked(False)
        self.desk_check.stateChanged.connect(self.value_changed)

        self.export_btn = QPushButton("Export", self)
        self.export_btn.setToolTip("Click to export the data")
        self.export_btn.clicked.connect(self.export)

        month_layout = QHBoxLayout()
        month_layout.addWidget(self.month_label)
        month_layout.addWidget(self.month)

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file)

        root = QVBoxLayout()
        root.addLayout(month_layout)
        root.addLayout(file_layout)
        root.addWidget(self.doc_check)
        root.addWidget(self.desk_check)
        root.addWidget(self.export_btn)

        self.setGeometry(400, 400, 500, 750)
        self.setWindowIcon(QIcon(Export_Logo))
        self.setWindowTitle("Export")
        self.setLayout(root)
        self.exec_()

    def export(self) -> None:
        if self.doc_check.isChecked() and self.file_path == "":
            exp_file = f"{self.root_folder}//{self.active_user}//expenses.csv"
            rev_file = f"{self.root_folder}//{self.active_user}//income.csv"

            data = {"Expenses": [], "Revenue": []}

            with open(exp_file, "r") as f_exp:
                reader = csv.DictReader(f_exp)

                for row in reader:
                    data["Expenses"].append(row)

                f_exp.close()

            with open(rev_file, "r") as f_rev:
                reader = csv.DictReader(f_rev)

                for row in reader:
                    data["Revenue"].append(row)

                f_rev.close()

            parsed = json.dumps(data, indent=4, sort_keys=False)

            with open(f"C://Users//{os.getlogin()}//Documents//export.json", "w") as export_file:
                export_file.write(parsed)
                export_file.close()

            self.close()

        elif self.desk_check.isChecked() and self.file_path == "":
            exp_file = f"{self.root_folder}//{self.active_user}//expenses.csv"
            rev_file = f"{self.root_folder}//{self.active_user}//income.csv"

            data = {"Expenses": [], "Revenue": []}

            with open(exp_file, "r") as f_exp:
                reader = csv.DictReader(f_exp)

                for row in reader:
                    data["Expenses"].append(row)

                f_exp.close()

            with open(rev_file, "r") as f_rev:
                reader = csv.DictReader(f_rev)

                for row in reader:
                    data["Revenue"].append(row)

                f_rev.close()

            parsed = json.dumps(data, indent=4, sort_keys=False)

            with open(f"C://Users//{os.getlogin()}//Desktop//export.json", "w") as export_file:
                export_file.write(parsed)
                export_file.close()

            self.close()

        else:
            print("else")

    def getFile(self):
        dialog = QFileDialog.getSaveFileName(self, "Select File", f"C:/Users/{os.getlogin()}/Desktop", "*.json")

        self.file_path = dialog[0]

        exp_file = f"{self.root_folder}//{self.active_user}//expenses.csv"
        rev_file = f"{self.root_folder}//{self.active_user}//income.csv"
        data = {"Expenses": [], "Revenue": []}

        with open(exp_file, "r") as f_exp:
            reader = csv.DictReader(f_exp)

            for row in reader:
                data["Expenses"].append(row)
            f_exp.close()

        with open(rev_file, "r") as f_rev: 
            reader = csv.DictReader(f_rev)

            for row in reader: 
                data["Revenue"].append(row)
            f_rev.close()

        parsed = json.dumps(data, indent=4, sort_keys=False)

        with open(self.file_path, "w") as export_file: 
            export_file.write(parsed)
            export_file.close()
        self.close() 



    def value_changed(self):
        if self.doc_check.isChecked() and self.desk_check.isChecked():
            self.doc_check.setChecked(False)
            self.desk_check.setChecked(False)
        elif self.doc_check.isChecked():
            self.desk_check.setChecked(False)
        elif self.desk_check.isChecked():
            self.doc_check.setChecked(False) 
        else: 
            self.doc_check.setChecked(False)
            self.desk_check.setChecked(False)