from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from .Expense.Home_Expense import Home_Expense
from .Revenue.Home_Income import Home_Income
from .Plot.Plot_Window import Plot_Window

from .Transfer.Transfer_Window import Transfer_Window
from .Passive_Income.Passive_Income import Passive_Income_Window
from .Passive_Expense.Passive_Expense import Passive_Expense_Window

from .Export.Export_Window import Export_Window
from .Profile_Stats.Statisitic_Window import Statistic_Window
from .Settings.Settings_Window import Settings_Window

from ..const import Main_Logo

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

        self.pass_label = QLabel(self)
        self.pass_label.setText("Passive income: ")

        self.pass_btn_income = QPushButton("Passive Income", self)
        self.pass_btn_income.setToolTip("Click to add a source of passive income")
        self.pass_btn_income.clicked.connect(self.passive_income)

        self.pass_label_exp = QLabel(self)
        self.pass_label_exp.setText("Passive Expense: ")

        self.pass_btn_exp = QPushButton("Passive Expense", self)
        self.pass_btn_exp.setToolTip("Click to add a source of passive expense")
        self.pass_btn_exp.clicked.connect(self.passive_expense)

        self.plot_label = QLabel(self)
        self.plot_label.setText("Plot Menu: ")

        self.Plot = QPushButton("Plot", self)
        self.Plot.setToolTip("Click to open the Plot Menu")
        self.Plot.clicked.connect(self.plot)

        self.transfer_label = QLabel(self)
        self.transfer_label.setText("Transfer Menu: ")

        self.transfer_btn = QPushButton("Transfer", self)
        self.transfer_btn.setToolTip("Click to open the transfer menu")
        self.transfer_btn.clicked.connect(self.transfer)

        self.stats_label = QLabel(self)
        self.stats_label.setText("Statistics: ")

        self.stats_btn = QPushButton("Statistics", self)
        self.stats_btn.setToolTip("Click to open the profile statistics")
        self.stats_btn.clicked.connect(self.stats)

        self.export_label = QLabel(self)
        self.export_label.setText("Export: ")

        self.exportbtn = QPushButton("Export", self)
        self.exportbtn.setToolTip("Click to open the Export Menu")
        self.exportbtn.clicked.connect(self.export)

        self.settings_label = QLabel(self)
        self.settings_label.setText("Settings: ")

        self.settingsbtn = QPushButton("Settings", self)
        self.settingsbtn.setToolTip("Click to open the Settings")
        self.settingsbtn.clicked.connect(self.settings)

        expense_layout = QHBoxLayout()
        expense_layout.addWidget(self.exp_label)
        expense_layout.addWidget(self.Expense)

        rev_layout = QHBoxLayout()
        rev_layout.addWidget(self.rev_label)
        rev_layout.addWidget(self.Revenue)

        pass_layout = QHBoxLayout()
        pass_layout.addWidget(self.pass_label)
        pass_layout.addWidget(self.pass_btn_income)

        pass_layout_exp = QHBoxLayout()
        pass_layout_exp.addWidget(self.pass_label_exp)
        pass_layout_exp.addWidget(self.pass_btn_exp)

        plt_layout = QHBoxLayout()
        plt_layout.addWidget(self.plot_label)
        plt_layout.addWidget(self.Plot)

        stats_layout = QHBoxLayout()
        stats_layout.addWidget(self.stats_label)
        stats_layout.addWidget(self.stats_btn)

        trans_layout = QHBoxLayout()
        trans_layout.addWidget(self.transfer_label)
        trans_layout.addWidget(self.transfer_btn)

        export_layout = QHBoxLayout()
        export_layout.addWidget(self.export_label)
        export_layout.addWidget(self.exportbtn)

        settings_layout = QHBoxLayout()
        settings_layout.addWidget(self.settings_label)
        settings_layout.addWidget(self.settingsbtn)

        root = QVBoxLayout()
        root.addLayout(expense_layout)
        root.addLayout(rev_layout)
        root.addLayout(pass_layout)
        root.addLayout(pass_layout_exp)
        root.addLayout(plt_layout)
        root.addLayout(trans_layout)
        root.addLayout(stats_layout)
        root.addLayout(export_layout)
        root.addLayout(settings_layout)

        self.setWindowTitle("Home")
        self.setLayout(root)
        self.setGeometry(300, 300, 500, 750)
        self.setWindowIcon(QIcon(Main_Logo))
        self.exec_()


    def expense(self): 
        dialog = Home_Expense(self.active_user) 

    def revenue(self): 
        dialog = Home_Income(self.active_user)

    def passive_income(self):
        dialog = Passive_Income_Window(self.active_user)

    def passive_expense(self):
        dialog = Passive_Expense_Window(self.active_user)

    def plot(self): 
        dialog = Plot_Window(self.active_user) 

    def transfer(self):
        dialog = Transfer_Window(self.active_user)

    def stats(self):
        dialog = Statistic_Window(self.active_user)

    def export(self):
        dialog = Export_Window(self.active_user)

    def settings(self):
        dialog = Settings_Window(self.active_user)
