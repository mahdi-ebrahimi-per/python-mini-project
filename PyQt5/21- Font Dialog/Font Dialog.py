import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ui_property()
        
        
        
    def ui_property(self):
        self.setGeometry(300, 300, 450, 350)
        
        self.button()
        self.label()
        self.vbox()
        
        self.setWindowTitle("Font Dialog")
        self.show()
    
    

    def button(self):
        self.btn = QPushButton("Show Font Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.button_Connected_showDialog)
    
    def button_Connected_showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
    
    def label(self):
        self.label = QLabel("ما شکاریم و زمان هم دام است ...", self)
        self.label.move(130, 20)
        
    
    def vbox(self):
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.label)

        self.setLayout(self.vbox)

        
def main():
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())


main()