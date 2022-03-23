import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui()
        self.CreateLayOut()
        self.ListWidget()

        self.show()

    def ui(self):
        self.setWindowTitle("Qt List Widget")    
        self.setGeometry(700, 500, 500, 200)

    def CreateLayOut(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def ListWidget(self):
        self.ListWidget = QListWidget()
        self.ListWidget.insertItems(0, ["Name 2", "Name 3", "Name 4"])
        self.ListWidget.insertItem(0, "Name 1")
        self.ListWidget.insertItem(4, "Name 5")
                
        self.ListWidget.clicked.connect(self.ListWidget_GetOutPut_onclick)
        self.layout.addWidget(self.ListWidget)
    
    def ListWidget_GetOutPut_onclick(self):
        item = self.ListWidget.currentItem()
        print(item.text())
    

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())
