import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.ui()

    def ui(self):
        checkbox1 = QCheckBox("Show Title", self)
        checkbox1.move(20, 30)
        # checkbox1.setChecked(True)
        checkbox1.stateChanged.connect(self.CheckBox_state)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("PyQt CheckBox")
        self.show()

    def CheckBox_state(self, state):
        if state == Qt.Checked:
            print(state, Qt.Checked)
            self.setWindowTitle("PyQt CheckBox")

        else:
            print(state, Qt.Checked)
            self.setWindowTitle(" ")



app = QApplication(sys.argv)
instance = App()
sys.exit(app.exec_())
