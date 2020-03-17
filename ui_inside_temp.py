# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inside_temp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(921, 281)
        Dialog.setStyleSheet("background:rgb(0,0,0);border 2px solid grey;")
        self.widget_rms_1 = PlotWidget(Dialog)
        self.widget_rms_1.setGeometry(QtCore.QRect(20, 20, 881, 231))
        self.widget_rms_1.setStyleSheet("background:rgb(0,0,0);")
        self.widget_rms_1.setObjectName("widget_rms_1")
        self.label_44 = QtWidgets.QLabel(self.widget_rms_1)
        self.label_44.setGeometry(QtCore.QRect(100, 20, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(222, 114, 94);")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.widget_rms_1)
        self.label_45.setGeometry(QtCore.QRect(80, 10, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("background-color:rgba(9,9,255,0);\n"
"color:rgb(222, 114, 94);")
        self.label_45.setObjectName("label_45")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 921, 281))
        self.label.setStyleSheet("border: 2px solid grey;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.widget_rms_1.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Building Inside Temperature"))
        self.label_44.setText(_translate("Dialog", "Inside Temperature [Celsius]"))
        self.label_45.setText(_translate("Dialog", "▆"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
