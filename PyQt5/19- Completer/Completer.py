import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.Create_Layout()
        self.Completer()
        self.SearchBox()
        
        self.show()
    
    
    def Create_Layout(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)     
    
    def Completer(self):
        names = ["Ali", "Abbas", "Amin", "Mohammad", "Reza"]
        self.completer = QCompleter(names)
        
    def SearchBox(self):
        lineEdit = QLineEdit()
        lineEdit.setCompleter(self.completer)        
        self.layout.addWidget(lineEdit, 0, 0)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
