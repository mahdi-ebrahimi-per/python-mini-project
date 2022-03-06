import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(0, 0, 450, 450)
        self.setWindowTitle("Window With Icon")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()


app = QApplication(sys.argv)
myapp = Window()
app.exec_()    

