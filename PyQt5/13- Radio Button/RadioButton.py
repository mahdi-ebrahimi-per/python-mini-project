import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui()
        self.RadioButton_GridLayout()

        self.show()

    def ui(self):
        self.setWindowTitle("Qt Radio Button") 
        self.setGeometry(700, 500, 500, 70)   


    def RadioButton_GridLayout(self):
        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel(self)
        label1.setText("Gender : " )
        layout.addWidget(label1, 0, 0)

        radioButton1 = QRadioButton("Male")
        radioButton1.setChecked(False)
        radioButton1.gender = "Male"
        radioButton1.toggled.connect(self.RadioButton_onclick)
        layout.addWidget(radioButton1, 0, 1)

        radioButton2 = QRadioButton("Female")
        radioButton2.setChecked(False)
        radioButton2.gender = "Female"
        radioButton2.toggled.connect(self.RadioButton_onclick)
        layout.addWidget(radioButton2, 0, 2)

    def RadioButton_onclick(self):
        radioButton1 = self.sender()

        if radioButton1.isChecked():
            print(f"User Gender is {radioButton1.gender}")


app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())