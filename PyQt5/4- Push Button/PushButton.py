import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def Application():
    app = QApplication(sys.argv)
    form = QWidget()

    button1 = QPushButton(form)
    button1.setText("Exit")
    button1.move(64,32)
    button1.clicked.connect(buttonClicked)

    form.setGeometry(100,100, 700, 600)
    form.setWindowTitle("PyQt Button")
    form.show()

    sys.exit(app.exec_())


def buttonClicked():
    quit()


Application()