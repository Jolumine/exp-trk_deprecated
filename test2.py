from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis, QBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
 
 
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("PyQt BarChart")
        self.setGeometry(100,100, 680,500)
        self.show()
        self.create_bar()
 
 
 
 
    def create_bar(self):
        #The QBarSet class represents a set of bars in the bar chart.
         # It groups several bars into a bar set

        set1 = QBarSet("Test")
 
        
 
        series = QBarSeries()
        series.append(set1)

 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Percent Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartView)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())