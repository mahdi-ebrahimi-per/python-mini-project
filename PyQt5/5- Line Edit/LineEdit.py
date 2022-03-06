import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lineEdit()
        self.CreateLabel()
    
        self.setGeometry(100, 100, 700, 600)
        self.setWindowTitle("PyQt LineEdit")
        self.show()

    def lineEdit(self):
        lineedit1 = QLineEdit(self)
        lineedit1.move(200, 50)
        lineedit1.resize(300, 35)
        lineedit1.textChanged.connect(self.LebelFunction)        

    def CreateLabel(self):
        self.label = QLabel(self)
        self.label.move(200, 130)
    
    def LebelFunction(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = App()
    sys.exit(app.exec_())

