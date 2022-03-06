import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

def Window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    counter = 1
    for i in range(5):
        for j in range(5):
            grid.addWidget(QPushButton(str(counter)), i, j)
            counter += 1
    
    win.setLayout(grid)
    win.setWindowTitle("PyQt Layout")
    win.setGeometry(630, 400, 700, 400)
    win.show()

    sys.exit(app.exec_())


Window()

