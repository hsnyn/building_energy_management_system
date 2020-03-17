# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_floor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1261, 911)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 911))
        self.label.setStyleSheet("border: 2px solid grey;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2F.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(660, 290, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 400, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 80, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(1120, 440, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(540, 760, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 430, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "2nd Floor Temperature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
