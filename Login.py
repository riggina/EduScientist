import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Tampilan import *

class ob:
    username = ""
    password = int
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
class user(ob):
    def __init__(self,username,password):
        super().__init__ (self,username,password)
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI
        self.ui.setupUI(self)
        self.ui.buttonclicked.clicked.connect(self.dispmessage)
    def dispmessage(self):
        marksOBJECT = Marks(self.ui.lineEditPassword.text(),self.ui.lineEditUsername.text())
        self.ui.labelResponse.setText("Passowrd:"+ marksOBJECT.getPassword + ",Username" + marksOBJECT.getUsername())

if __name__ == 'main':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())






