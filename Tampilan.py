from PyQt5 import QtCore, QtGui, QtWidgets

class UI(object):
    def setupUI(self,EduScientist):
        EduScientist.setObejectName("Edu Scientist")
        EduScientist.resize(487, 368)
        self.label = QtWidgets.QLabel(EduScientist)
        self.label.setGeometry(QtCore.QRect(60,30,101,16))
        self.label.setObjectName("Label")
        self.label2 = QtWidgets.QLabel(EduScientist)
        self.label2.setGeometry(QtCore.QRect(60,80,91,16))
        self.label2.setObjectName("Label2")
        self.lineEditUsername = QtWidgets.QLineEdit(EduScientist)
        self.lineEditUsername.setGeometry(QtCore.QRect(200,80,171,21))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(EduScientist)
        self.lineEditPassword.setGeometry(QtCore.QRect(200,30,171,21))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.buttonclicked = QtWidgets.QPushButton(EduScientist)
        self.buttonclicked.setGeometry(QtCore.QRect(190,320,113,32))
        self.buttonclicked.setObjectName("ButtonClicked")
        self.labelResponse = QtWidgets.QLabel(EduScientist)
        self.labelResponse.setGeometry(QtCore.QRect(100,230,291,61))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUI(EduScientist)
        QtCore.QMetaObject.connectSlotsByName(EduScientist)
    def retranslateUI(self,EduScientist):
        _translate = QtCore.QCoreApplication.translate
        EduScientist.setWindowTitle(_translate("EduScientist","EduScientist"))
        self.label.setText(_translate("EduScientist","Username"))
        self.label2.setText(_translate("EduScientist","Password"))
        self.buttonclicked.setText(_translate("EduScientist","Next"))




