import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(200, 100, 300, 40)
        slider.valueChanged[int].connect(self.CheckChangeValue)

        self.setGeometry(630, 400, 700, 400)
        self.setWindowTitle("PyQt Slider")
        self.show()
    

    def CheckChangeValue(self, value):
        print(value)


app = QApplication(sys.argv)
myApp = App()
sys.exit(app.exec_())

