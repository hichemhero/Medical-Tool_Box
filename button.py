# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 320)
        self.label_5 = QtWidgets.QPushButton(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 60, 60, 60))
        self.label_5.setStyleSheet("border: 5px solid rgb(230, 5, 64);\n"
"border-radius: 30px;")
        self.label_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/custom qmenu/icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_5.setIcon(icon)
        self.label_5.setIconSize(QtCore.QSize(40, 40))
        self.label_5.setObjectName("label_5")
        self.label_5.clicked.connect(self.open_webbrowser)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def open_webbrowser():
        webbrowser.open('http://www.google.com')

app = QApplication(sys.argv)
########################################################################
## 
########################################################################
window = Ui_Dialog()
window.show()
sys.exit(app.exec_())