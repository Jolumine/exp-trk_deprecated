from PyQt5.QtWidgets import QPushButton, QDialog, QLineEdit, QComboBox, QCommandLinkButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...vars import Settings_Logo

import json
import os


class Settings(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active

        self.currency_label = QLabel(self)
        self.currency_label.setText("Currency")

        self.currencys = QComboBox(self)
        self.currencys.addItems(["USD", "Euro"])
        self.currencys.setCurrentText("Euro")
        self.currencys.setToolTip("Select to currency you want your money to be shown in")

        self.reset_label = QLabel(self)
        self.reset_label.setText("Reset Settings: ")
        
        self.reset = QPushButton("Reset", self)
        self.reset.setToolTip("Click to reset your settings")
        self.reset.clicked.connect(self.resetfunc)

        currency_layout = QHBoxLayout()
        currency_layout.addWidget(self.currency_label)
        currency_layout.addWidget(self.currencys)

        reset_layout = QHBoxLayout()
        reset_layout.addWidget(self.reset_label)
        reset_layout.addWidget(self.reset)

        root = QVBoxLayout()
        root.addLayout(currency_layout)
        root.addLayout(reset_layout)

        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon(Settings_Logo))
        self.setGeometry(400, 400, 500, 750)
        self.setLayout(root)
        self.exec_()

    def resetfunc(self):
        path_user = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\settings.json"

        with open(path_user, "w") as f_user: 
            std = json.dumps({"Language": "EN", "Darkmode": False, "currency": "USD"}, indent=4, sort_keys=False)
            f_user.write(std)

        self.close()
    