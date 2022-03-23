import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui()
        self.TabWidget()

        self.show()

    def ui(self):
        self.setWindowTitle("Qt Tab Widget")    
        self.setGeometry(700, 500, 500, 200)

    def TabWidget(self):
        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel("This is label for Tab1")
        label2 = QLabel("This is label for Tab2")

        tabWidget = QTabWidget()
        tabWidget.addTab(label1, "Tab1")
        tabWidget.addTab(label2, "Tab2")
        layout.addWidget(tabWidget, 0, 0)


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())
