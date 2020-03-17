# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nineth_floor.ui'
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
        self.label.setPixmap(QtGui.QPixmap("9F.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(650, 290, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(460, 400, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(222, 114, 94,100);\n"
"color:rgb(222, 114, 94);\n"
"border:1px solid grey;\n"
"border-radius: 10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "9th Floor Temperature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
