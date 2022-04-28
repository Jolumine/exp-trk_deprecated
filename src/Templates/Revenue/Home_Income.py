from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon

from .Add_Revenue import Add_Income
from .Delete_Revenue import Delete_Revenue
from ..Plot.Plot_Window import Plot_Window

from ...const import Money_Logo

class Home_Income(QDialog): 
    def __init__(self, active_user, parent=None): 
        super().__init__(parent)
        
        self.active = active_user

        self.add_btn = QPushButton("Add Income", self)
        self.add_btn.setToolTip("Click to open the Add Menu")
        self.add_btn.clicked.connect(self.add)

        self.del_btn = QPushButton("Delete Income", self)
        self.del_btn.setToolTip("Click to open the Delete Menu")
        self.del_btn.clicked.connect(self.delete)

        self.plot_btn = QPushButton("Show", self)
        self.plot_btn.setToolTip("Click to open the Plot Menu")
        self.plot_btn.clicked.connect(self.plot)

        layout = QVBoxLayout()
        layout.addWidget(self.add_btn)
        layout.addWidget(self.del_btn)
        layout.addWidget(self.plot_btn)

        self.setWindowTitle("Income")
        self.setWindowIcon(QIcon(Money_Logo))
        self.setGeometry(400, 400, 500, 750)
        self.setLayout(layout)
        self.exec_()

    def add(self): 
        dialog = Add_Income(self.active) 

    def delete(self): 
        dialog = Delete_Revenue(self.active) 

    def plot(self): 
        dialog = Plot_Window(self.active) 