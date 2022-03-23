import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.SetWindowProperty()
        self.CreateLayOut()
        self.Dial()

        self.show()

    def SetWindowProperty(self):
        self.setWindowTitle("Qt Dial")    
        self.setGeometry(700, 500, 500, 200)

    def CreateLayOut(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def Dial(self):
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(5)
        self.dial.valueChanged.connect(self.Dial_GetValue_onClick)
        
        self.layout.addWidget(self.dial)
        
    def Dial_GetValue_onClick(self):
        print(f"Dial Value is {self.dial.value()}")

app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())
