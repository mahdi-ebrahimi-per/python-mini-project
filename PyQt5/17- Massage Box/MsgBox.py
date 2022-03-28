import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        while True:
            reply = self.MsgBox_question()
            
            if reply == True:
                self.MsgBox_IKnewIt()
                quit()
                
            elif reply == False:
                continue
            
    def MsgBox_question(self):
        buttonReply = QMessageBox.question(self, "A Question", "Are You Stupid?",
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        
    
        if buttonReply == QMessageBox.Yes:
            return True
        
        else:
            return False
    
    def MsgBox_IKnewIt(self):
        buttonReply = QMessageBox.information(self, "Ok then...", "I knew it ;)",
                                           QMessageBox.Ok,
                                           QMessageBox.Ok)
    
    
app = QApplication(sys.argv)
screen = Window()
sys.exit(app.exec_())

