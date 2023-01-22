from PyQt5.QtWidgets import QDialog, QComboBox, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon


from ...const import years_all, types_all, Graph_Icon
from .Calculations import Math
from .Plotter import Plot
 
from ...const import wo_month

class Plot_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active_user = active

        self.select_label = QLabel(self)
        self.select_label.setText("Selected: ")

        self.select = QComboBox(self)
        self.select.setToolTip("Select if you want Expenses, Revenue or both")
        self.select.addItems(["Income", "Expenses"])

        self.year_label = QLabel(self)
        self.year_label.setText("Year: ")

        self.year = QComboBox(self)
        self.year.setToolTip("Select the year from which you want to see the Graph")
        self.year.addItems(years_all)

        self.type_label = QLabel(self)
        self.type_label.setText("Type: ")

        self.type = QComboBox(self)
        self.type.setToolTip("Select the type you want to plot")
        self.type.addItems(types_all)

        self.diff_label = QLabel(self)
        self.diff_label.setText("Comparison beetween Expenses and Income: ")

        self.diff = QPushButton("Comparison", self)
        self.diff.setToolTip("Click to get a Grah which is showing the Difference beetween Expense and Revenue")
        self.diff.clicked.connect(self.difference)

        self.plotButton = QPushButton("Plot", self)
        self.plotButton.setToolTip("Click to plot the selected choice")
        self.plotButton.clicked.connect(self.plot)

        select_layout = QHBoxLayout()
        select_layout.addWidget(self.select_label)
        select_layout.addWidget(self.select)

        diff_layout = QHBoxLayout()
        diff_layout.addWidget(self.diff_label)
        diff_layout.addWidget(self.diff)

        year_layout = QHBoxLayout()
        year_layout.addWidget(self.year_label)
        year_layout.addWidget(self.year)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type)

        root = QVBoxLayout()
        root.addLayout(select_layout)
        root.addLayout(year_layout)
        root.addLayout(type_layout)
        root.addLayout(diff_layout)
        root.addWidget(self.plotButton)

        self.setWindowTitle("Plot Menu")
        self.setGeometry(400, 400, 450, 550)
        self.setLayout(root)
        self.setWindowIcon(QIcon(Graph_Icon))
        self.exec_()

    def plot(self) -> None:
        if self.type.currentText() == "All" and self.year.currentText() == "All":
            amounts = Math.get_data(selected=self.select.currentText(), active=self.active_user)  
            Math.clean_data()        
            Plot(wo_month, amounts, "", "Month", "Amount")

        elif self.type.currentText() != "All" and self.year.currentText() != "All": 
            amounts = Math.get_data(selected=self.select.currentText(), active=self.active_user, year=self.year.currentText() ,type=self.type.currentText())
            Math.clean_data()        
            Plot(wo_month, amounts, "", "Month", "Amount")    

        elif self.type.currentText != "All" and self.year.currentText() == "All":
            amounts = Math.get_data(selected=self.select.currentText(), active=self.active_user, type=self.type.currentText())
            Math.clean_data()        
            Plot(wo_month, amounts, "", "Month", "Amount")
            
        else: 
            amounts =Math.get_data(selected=self.select.currentText(), active=self.active_user, year=self.year.currentText())
            Math.clean_data()        
            Plot(wo_month, amounts, "", "Month", "Amount")

    def difference(self):
        Math.difference(self.active_user)