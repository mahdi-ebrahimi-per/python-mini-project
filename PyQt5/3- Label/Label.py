import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def Application():
    app = QApplication(sys.argv)
    window = QWidget()

    textlabel = QLabel(window)
    textlabel.setText("Hello world")
    textlabel.move(150, 200)

    window.resize(700, 400)
    window.setWindowTitle("PyQt Label")

    window.show()

    sys.exit(app.exec_())


Application()




