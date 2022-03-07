import sys
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        combo = QComboBox(self)
        combo.addItems(["-", 'Iran', "Russia", "China"])
        combo.addItem("USA")
        combo.move(300, 50)

        self.label = QLabel(self)
        self.label.move(300, 100)

        combo.activated[str].connect(self.combo_PresidentName)


        self.setGeometry(630, 400, 700, 400)
        self.setWindowTitle("PyQt ComboBox")
        self.show()
    
    def combo_PresidentName(self, nation):
        president = {"Iran":"Khamenei", "Russia":"Vladimir putin", "China":"Xi Jinping", "USA":"Joe Biden"}
        try:
            self.label.setText(president[nation])
            self.label.adjustSize

        except:
            self.label.setText(" ")
            self.label.adjustSize


app = QApplication(sys.argv)
myApp = App()
sys.exit(app.exec_())

