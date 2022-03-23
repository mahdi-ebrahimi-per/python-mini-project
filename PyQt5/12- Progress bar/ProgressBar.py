import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5.QtCore import Qt, QTimer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
		
        self.ui()
        self.ProgressBarProperty()
        self.HandleTimer()

        self.show()
		
    def ProgressBarProperty(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(32, 32, 200, 25)
        self.pbar.setValue(60)

    def ui(self):
        self.setWindowTitle("Qt Progress Bar")
        self.setGeometry(500, 500, 500, 600)

    def HandleTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.HandleTimer)
        self.timer.start(1000)

        pbar_value = self.pbar.value()
        
        if pbar_value < 100:
            pbar_value += 1
            self.pbar.setValue(int(pbar_value))

        else:
            self.timer.stop()


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())
