from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QFrame
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

from ..const import Main_Logo, Menu_Logo, Transfer_Logo, Stats_Logo, Export_Logo, Money_Logo, Graph_Icon, Settings_Logo

class Root_Window(QWidget): 
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)
        self.active_user = active_user

        self.exp_label = QLabel(self)
        self.exp_label.setText("Expenses Menu: ")

        self.Expense = QPushButton("Expenses", self)
        self.Expense.setToolTip("Click to open the Menu for Expenses")
        self.Expense.setIcon(QIcon(Menu_Logo))
        self.Expense.clicked.connect(self.expense)

        self.rev_label = QLabel(self)
        self.rev_label.setText("Revenue Menu: ")

        self.Revenue = QPushButton("Revenues", self)
        self.Revenue.setToolTip("Click to open the Menu for your Revenues")
        self.Revenue.setIcon(QIcon(Menu_Logo))
        self.Revenue.clicked.connect(self.revenue)

        self.pass_label = QLabel(self)
        self.pass_label.setText("Passive income: ")

        self.pass_btn_income = QPushButton("Passive Income", self)
        self.pass_btn_income.setToolTip("Click to add a source of passive income")
        self.pass_btn_income.setIcon(QIcon(Money_Logo))
        self.pass_btn_income.clicked.connect(self.passive_income)

        self.pass_label_exp = QLabel(self)
        self.pass_label_exp.setText("Passive Expense: ")

        self.pass_btn_exp = QPushButton("Passive Expense", self)
        self.pass_btn_exp.setToolTip("Click to add a source of passive expense")
        self.pass_btn_exp.setIcon(QIcon(Money_Logo))
        self.pass_btn_exp.clicked.connect(self.passive_expense)

        self.plot_label = QLabel(self)
        self.plot_label.setText("Plot Menu: ")

        self.Plot = QPushButton("Plot", self)
        self.Plot.setToolTip("Click to open the Plot Menu")
        self.Plot.setIcon(QIcon(Graph_Icon))
        self.Plot.clicked.connect(self.plot)

        self.transfer_label = QLabel(self)
        self.transfer_label.setText("Transfer Menu: ")

        self.transfer_btn = QPushButton("Transfer", self)
        self.transfer_btn.setToolTip("Click to open the transfer menu")
        self.transfer_btn.setIcon(QIcon(Transfer_Logo))
        self.transfer_btn.clicked.connect(self.transfer)

        self.stats_label = QLabel(self)
        self.stats_label.setText("Statistics: ")

        self.stats_btn = QPushButton("Statistics", self)
        self.stats_btn.setToolTip("Click to open the profile statistics")
        self.stats_btn.setIcon(QIcon(Stats_Logo))
        self.stats_btn.clicked.connect(self.stats)

        self.export_label = QLabel(self)
        self.export_label.setText("Export: ")

        self.exportbtn = QPushButton("Export", self)
        self.exportbtn.setToolTip("Click to open the Export Menu")
        self.exportbtn.setIcon(QIcon(Export_Logo))
        self.exportbtn.clicked.connect(self.export)

        self.settings_label = QLabel(self)
        self.settings_label.setText("Settings: ")

        self.settingsbtn = QPushButton("Settings", self)
        self.settingsbtn.setToolTip("Click to open the Settings")
        self.settingsbtn.setIcon(QIcon(Settings_Logo))
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

        # New Layout 

        space_item_1 = QFrame()
        space_item_1.setStyleSheet("background-color: darkgray")
        space_item_1.setFixedWidth(10)

        space_item_2 = QFrame()
        space_item_2.setStyleSheet("background-color: darkgray")
        space_item_2.setFixedWidth(10)

        space_item_3 = QFrame()
        space_item_3.setStyleSheet("background-color: darkgray")
        space_item_3.setFixedWidth(10)

        space_item_4 = QFrame()
        space_item_4.setStyleSheet("background-color: darkgray")
        space_item_4.setFixedWidth(10)

        col_1 = QVBoxLayout()
        col_1.addLayout(expense_layout)
        col_1.addLayout(rev_layout)
        col_1.addLayout(plt_layout)

        col_2 = QVBoxLayout()
        col_2.addLayout(pass_layout)
        col_2.addLayout(pass_layout_exp)
        col_2.addLayout(trans_layout)

        col_3 = QVBoxLayout()
        col_3.addLayout(stats_layout)
        col_3.addLayout(export_layout)
        col_3.addLayout(settings_layout)

        root_1 = QHBoxLayout()
        root_1.addWidget(space_item_1)
        root_1.addLayout(col_1)
        root_1.addWidget(space_item_2)
        root_1.addLayout(col_2)
        root_1.addWidget(space_item_3)
        root_1.addLayout(col_3)
        root_1.addWidget(space_item_4)

        self.setWindowTitle("Home")
        self.setLayout(root_1)
        self.setGeometry(300, 300, 500, 650)
        self.setWindowIcon(QIcon(Main_Logo))
        self.show()


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
