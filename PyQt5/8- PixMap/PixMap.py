import sys
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.image = QPixmap('picture.png')
        self.label = QLabel()
        self.label.setPixmap(self.image) 

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)

        self.setGeometry(630, 400, 700, 400)
        self.setWindowTitle("PyQt Pixmap")
        self.show()


app = QApplication(sys.argv)
instance = App()
sys.exit(app.exec_())

