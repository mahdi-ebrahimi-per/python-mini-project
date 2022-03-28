import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.Create_Layout()
        self.LineEdit_withToolTip()
        self.UI_property()
        
        self.show()
    
    def UI_property(self):
        self.setGeometry(400, 500, 600, 400)
    
    def Create_Layout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)        
        
    def LineEdit_withToolTip(self):
        lineEdit = QLineEdit(self)
        lineEdit.setToolTip("نام خود را وارد کنید")
        lineEdit.move(100, 160)
        lineEdit.resize(400, 50)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())