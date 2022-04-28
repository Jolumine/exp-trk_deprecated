from locale import normalize
from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtChart import QPieSlice, QChartView, QPieSeries, QChart
from PyQt5.QtGui import QIcon, QPainter, QPen
from PyQt5.QtCore import Qt

from ...const import log_file, Stats_Logo
from .Calc_Stats import get_expenses_sum, get_income_sum, get_sum_passive_exp, get_sum_passive_in

import os
import json

class Statistic_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        # GUI Elements

        self.active = active
        self.active_path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}"

        self.balance_label = QLabel(self)
        self.balance_label.setText("Account balance: ")

        self.balance = QLineEdit(self)
        self.balance.setReadOnly(True)
        self.balance.setAlignment(Qt.AlignCenter)
        self.balance.setFixedWidth(250)
        self.balance.setText(str((get_income_sum(self.active_path)-get_expenses_sum(self.active_path)))+self.get_currency())

        self.balance_exp_label = QLabel(self)
        self.balance_exp_label.setText("Sum of expenses: ")
        
        self.sum_exp = QLineEdit(self)
        self.sum_exp.setReadOnly(True)
        self.sum_exp.setAlignment(Qt.AlignCenter)
        self.sum_exp.setFixedWidth(250)
        self.sum_exp.setText(str(get_expenses_sum(self.active_path))+self.get_currency())

        self.balance_in_label = QLabel(self)
        self.balance_in_label.setText("Sum of income: ")

        self.sum_in = QLineEdit(self)
        self.sum_in.setReadOnly(True)
        self.sum_in.setAlignment(Qt.AlignCenter)
        self.sum_in.setFixedWidth(250)
        self.sum_in.setText(str(get_income_sum(self.active_path))+self.get_currency())

        self.passive_label_in = QLabel(self)
        self.passive_label_in.setText("Sum of passive income: ")

        self.passive_in = QLineEdit(self)
        self.passive_in.setReadOnly(True)
        self.passive_in.setAlignment(Qt.AlignCenter)
        self.passive_in.setFixedWidth(250)
        self.passive_in.setText(str(get_sum_passive_in(self.active_path))+self.get_currency())

        self.passive_label_exp = QLabel(self)
        self.passive_label_exp.setText("Sum of passive expenses: ")

        self.passive_exp = QLineEdit(self)
        self.passive_exp.setReadOnly(True)
        self.passive_exp.setAlignment(Qt.AlignCenter)
        self.passive_exp.setFixedWidth(250)
        self.passive_exp.setText(str(get_sum_passive_exp(self.active_path))+self.get_currency())

        # Normal Sum Chart

        self.series_normal = QPieSeries()
        self.series_normal.append("Incomes", get_income_sum(self.active_path))
        self.series_normal.append("Expenses", get_expenses_sum(self.active_path))

        self.chart_normal = QChart()
        self.chart_normal.legend().hide()
        self.chart_normal.addSeries(self.series_normal)
        self.chart_normal.createDefaultAxes()
        self.chart_normal.setAnimationOptions(QChart.SeriesAnimations)
        self.chart_normal.setTitle("Comparison beetween incomes and expenses")

        slice_income = QPieSlice()
        slice_income = self.series_normal.slices()[0]
        slice_income.setLabelVisible(True)
        slice_income.setBrush(Qt.black)

        slice_expense = QPieSlice()
        slice_expense = self.series_normal.slices()[1]
        slice_expense.setLabelVisible(True)
        slice_expense.setExploded(True)
        slice_expense.setBrush(Qt.red)
 
        self.chart_normal.legend().setVisible(True)
        self.chart_normal.legend().setAlignment(Qt.AlignBottom)
 
        self.chartview_normal = QChartView(self.chart_normal)
        self.chartview_normal.setFixedHeight(600)
        self.chartview_normal.setFixedWidth(600)
        
        # Passive Chart

        self.series_passive = QPieSeries()
        self.series_passive.append("Incomes", get_sum_passive_in(self.active_path))
        self.series_passive.append("Expenses", get_sum_passive_exp(self.active_path))

        self.chart_passive = QChart()
        self.chart_passive.legend().hide()
        self.chart_passive.addSeries(self.series_passive)
        self.chart_passive.createDefaultAxes()
        self.chart_passive.setAnimationOptions(QChart.SeriesAnimations)
        self.chart_passive.setTitle("Comparison beetween passive incomes and expenses")

        slice_income_passive = QPieSlice()
        slice_income_passive = self.series_passive.slices()[0]
        slice_income_passive.setLabelVisible(True)
        slice_income_passive.setBrush(Qt.darkGreen)

        slice_expense_passive = QPieSlice()
        slice_expense_passive = self.series_passive.slices()[1]
        slice_expense_passive.setLabelVisible(True)
        slice_expense_passive.setExploded(True)
        slice_expense_passive.setBrush(Qt.darkBlue)
 
        self.chart_passive.legend().setVisible(True)
        self.chart_passive.legend().setAlignment(Qt.AlignBottom)
 
        self.chartview_passive = QChartView(self.chart_passive)
        self.chartview_passive.setFixedHeight(600)
        self.chartview_passive.setFixedWidth(600)

        # Layouts 

        balance_layout = QHBoxLayout()
        balance_layout.addWidget(self.balance_label)
        balance_layout.addWidget(self.balance)

        balance_exp_layout = QHBoxLayout()
        balance_exp_layout.addWidget(self.balance_exp_label)
        balance_exp_layout.addWidget(self.sum_exp)

        balance_in_layout = QHBoxLayout()
        balance_in_layout.addWidget(self.balance_in_label)
        balance_in_layout.addWidget(self.sum_in)

        passive_layout_in = QHBoxLayout()
        passive_layout_in.addWidget(self.passive_label_in)
        passive_layout_in.addWidget(self.passive_in)

        passive_layout_exp = QHBoxLayout()
        passive_layout_exp.addWidget(self.passive_label_exp)
        passive_layout_exp.addSpacing(20)
        passive_layout_exp.addWidget(self.passive_exp)

        stats = QVBoxLayout()
        stats.addLayout(balance_layout)
        stats.addLayout(balance_in_layout)
        stats.addLayout(balance_exp_layout)
        stats.addLayout(passive_layout_in)
        stats.addLayout(passive_layout_exp)

        graph_1 = QVBoxLayout()
        graph_1.addWidget(self.chartview_normal)
        graph_1.addWidget(self.chartview_passive)

        graph_2 = QVBoxLayout()
        #graph_2.addWidget(self.chartview_passive)

        root = QHBoxLayout()
        root.addLayout(stats)
        root.addLayout(graph_1)
        root.addLayout(graph_2)

        # Window Settings

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
