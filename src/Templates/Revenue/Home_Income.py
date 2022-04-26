from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon

from .Add_Revenue import Add_Income
from .Delete_Revenue import Delete_Revenue

from ...const import Money_Logo

class Home_Income(QDialog): 
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)
        
        self.active = active_user

        self.addButton = QPushButton("Add Income", self)
        self.addButton.setToolTip("Click to open the Add Menu")
        self.addButton.clicked.connect(self.add)

        self.delButton = QPushButton("Delete Income", self)
        self.delButton.setToolTip("Click to open the Delete Menu")
        self.delButton.clicked.connect(self.delete)

        self.plot = QPushButton("Show", self)
        self.plot.setToolTip("Click to open the Plot Menu")
        self.plot.clicked.connect(self.PlotDial)

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.delButton)
        layout.addWidget(self.plot)

        self.setWindowTitle("Income")
        self.setWindowIcon(QIcon(Money_Logo))
        self.setGeometry(400, 400, 500, 750)
        self.setLayout(layout)
        self.exec_()

    def add(self): 
        dial = Add_Income(self.active) 

    def delete(self): 
        dial = Delete_Revenue(self.active) 

    def PlotDial(self): 
        pass 