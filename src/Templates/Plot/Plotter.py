from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ...const import Graph_Icon

import random
import matplotlib
matplotlib.use('Qt5Agg')


class CanvasSimplePlt(FigureCanvasQTAgg):
    def __init__(self, x, y, title, xlabel, ylabel, width=13.0, height=6.0,):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

        self.COLORS = ['black', 'red', 'green', 'blue']

        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.bar(x, y, color=[].append(random.choice(self.COLORS)))
        
class Plot(QDialog):
    def __init__(self, x, y, title, xlabel, ylabel, parent=None):
        super().__init__(parent)

        canvas = CanvasSimplePlt(x, y, title, xlabel, ylabel)

        self.root = QVBoxLayout()
        self.root.addWidget(canvas)

        self.setWindowTitle("Plot")
        self.setLayout(self.root)
        self.setWindowIcon(QIcon(Graph_Icon))
        self.exec_()
        

