import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(1000, 700)
window.setWindowTitle("First Window")
window.show()

app.exec_()

