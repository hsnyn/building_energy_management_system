# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1213, 901)
        Dialog.setStyleSheet("background:rgb(0,0,0);")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 272, 183))
        self.calendarWidget.setStyleSheet("background:rgb(200,200,200);")
        self.calendarWidget.setSelectedDate(QtCore.QDate(2018, 4, 30))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2016, 5, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2020, 8, 17))
        self.calendarWidget.setObjectName("calendarWidget")
        self.widget_rms_1 = PlotWidget(Dialog)
        self.widget_rms_1.setGeometry(QtCore.QRect(310, 20, 881, 271))
        self.widget_rms_1.setStyleSheet("background:rgb(0,0,0);")
        self.widget_rms_1.setObjectName("widget_rms_1")
        self.label_44 = QtWidgets.QLabel(self.widget_rms_1)
        self.label_44.setGeometry(QtCore.QRect(100, 20, 171, 16))
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
        self.label_50 = QtWidgets.QLabel(self.widget_rms_1)
        self.label_50.setGeometry(QtCore.QRect(80, 30, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.widget_rms_1)
        self.label_51.setGeometry(QtCore.QRect(100, 40, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_51.setObjectName("label_51")
        self.widget_rms_2 = PlotWidget(Dialog)
        self.widget_rms_2.setGeometry(QtCore.QRect(310, 310, 881, 271))
        self.widget_rms_2.setStyleSheet("background:rgb(0,0,0);")
        self.widget_rms_2.setObjectName("widget_rms_2")
        self.label_52 = QtWidgets.QLabel(self.widget_rms_2)
        self.label_52.setGeometry(QtCore.QRect(80, 10, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("background-color:rgba(9,9,255,0);\n"
"color:rgb(222, 114, 94);")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.widget_rms_2)
        self.label_53.setGeometry(QtCore.QRect(100, 40, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.widget_rms_2)
        self.label_54.setGeometry(QtCore.QRect(80, 30, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.widget_rms_2)
        self.label_55.setGeometry(QtCore.QRect(100, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(222, 114, 94);")
        self.label_55.setObjectName("label_55")
        self.widget_rms_4 = PlotWidget(Dialog)
        self.widget_rms_4.setGeometry(QtCore.QRect(310, 600, 881, 281))
        self.widget_rms_4.setStyleSheet("background:rgb(0,0,0);")
        self.widget_rms_4.setObjectName("widget_rms_4")
        self.label_48 = QtWidgets.QLabel(self.widget_rms_4)
        self.label_48.setGeometry(QtCore.QRect(100, 20, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(222, 114, 94);")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.widget_rms_4)
        self.label_49.setGeometry(QtCore.QRect(80, 10, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(222, 114, 94);")
        self.label_49.setObjectName("label_49")
        self.label_59 = QtWidgets.QLabel(self.widget_rms_4)
        self.label_59.setGeometry(QtCore.QRect(100, 40, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_59.setObjectName("label_59")
        self.label_58 = QtWidgets.QLabel(self.widget_rms_4)
        self.label_58.setGeometry(QtCore.QRect(80, 30, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:rgb(60, 114, 174);")
        self.label_58.setObjectName("label_58")
        self.pushButton_cost_AI = QtWidgets.QPushButton(Dialog)
        self.pushButton_cost_AI.setGeometry(QtCore.QRect(30, 250, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.pushButton_cost_AI.setFont(font)
        self.pushButton_cost_AI.setStyleSheet("border:0px;color:rgb(222, 114, 94);background:rgb(45,45,45);border-radius: 10px;")
        self.pushButton_cost_AI.setText("")
        self.pushButton_cost_AI.setObjectName("pushButton_cost_AI")
        self.label_79 = QtWidgets.QLabel(Dialog)
        self.label_79.setGeometry(QtCore.QRect(30, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("background-color:rgba(0,0,0,0); color: rgba(200,200,200,0.9);")
        self.label_79.setObjectName("label_79")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 131, 101))
        self.label_2.setStyleSheet("border:2px solid gray;border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_energy_AI = QtWidgets.QPushButton(Dialog)
        self.pushButton_energy_AI.setGeometry(QtCore.QRect(170, 250, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.pushButton_energy_AI.setFont(font)
        self.pushButton_energy_AI.setStyleSheet("border:0px; color:rgb(222, 114, 94);\n"
"background:rgb(45,45,45);border-radius: 10px;")
        self.pushButton_energy_AI.setText("")
        self.pushButton_energy_AI.setObjectName("pushButton_energy_AI")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 220, 131, 101))
        self.label_3.setStyleSheet("border:2px solid gray;border-radius: 10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_84 = QtWidgets.QLabel(Dialog)
        self.label_84.setGeometry(QtCore.QRect(170, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("background-color:rgba(0,0,0,0); color: rgba(200,200,200,0.9);")
        self.label_84.setObjectName("label_84")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 340, 131, 101))
        self.label_4.setStyleSheet("border:2px solid gray;border-radius: 10px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_cost_AI_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_cost_AI_2.setGeometry(QtCore.QRect(30, 370, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.pushButton_cost_AI_2.setFont(font)
        self.pushButton_cost_AI_2.setStyleSheet("border:0px;color:rgb(222, 114, 94);background:rgb(45,45,45);border-radius: 10px;")
        self.pushButton_cost_AI_2.setText("")
        self.pushButton_cost_AI_2.setObjectName("pushButton_cost_AI_2")
        self.pushButton_energy_AI_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_energy_AI_2.setGeometry(QtCore.QRect(170, 370, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.pushButton_energy_AI_2.setFont(font)
        self.pushButton_energy_AI_2.setStyleSheet("border:0px; color:rgb(222, 114, 94);\n"
"background:rgb(45,45,45);border-radius: 10px;")
        self.pushButton_energy_AI_2.setText("")
        self.pushButton_energy_AI_2.setObjectName("pushButton_energy_AI_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 131, 101))
        self.label_5.setStyleSheet("border:2px solid gray;border-radius: 10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_87 = QtWidgets.QLabel(Dialog)
        self.label_87.setGeometry(QtCore.QRect(170, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("background-color:rgba(0,0,0,0); color: rgba(200,200,200,0.9);")
        self.label_87.setObjectName("label_87")
        self.label_80 = QtWidgets.QLabel(Dialog)
        self.label_80.setGeometry(QtCore.QRect(30, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("background-color:rgba(0,0,0,0); color: rgba(200,200,200,0.9);")
        self.label_80.setObjectName("label_80")
        self.chiller_label = QtWidgets.QLabel(Dialog)
        self.chiller_label.setGeometry(QtCore.QRect(65, 460, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.chiller_label.setFont(font)
        self.chiller_label.setStyleSheet("background-color:rgba(0,0,0,0); color: rgba(200,200,200,0.9);")
        self.chiller_label.setObjectName("chiller_label")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(30, 470, 251, 161))
        self.verticalSlider.setStyleSheet("QSlider{background: rgba(255,0,0,0); border: 0px; width: 0px;}\n"
"\n"
"QSlider::groove:vertical {background: rgba(255,0,0,0); border: 0px; width: 0px;}\n"
"\n"
"QSlider::handle:vertical {background: rgba(255,0,0,0); border: 0px; width: 0px;}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setObjectName("verticalSlider")
        self.chiller_label_2 = QtWidgets.QLabel(Dialog)
        self.chiller_label_2.setGeometry(QtCore.QRect(203, 461, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.chiller_label_2.setFont(font)
        self.chiller_label_2.setStyleSheet("background-color:rgba(0,0,0,0); color:rgb(222, 114, 94);")
        self.chiller_label_2.setObjectName("chiller_label_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(64, 570, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.label_7.setObjectName("label_7")
        self.AI_AC_2 = QtWidgets.QLabel(Dialog)
        self.AI_AC_2.setGeometry(QtCore.QRect(204, 570, 47, 25))
        self.AI_AC_2.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.AI_AC_2.setObjectName("AI_AC_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(64, 540, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(121, 500, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(60, 114, 174);")
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(64, 600, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.label_16.setObjectName("label_16")
        self.AI_AC_1 = QtWidgets.QLabel(Dialog)
        self.AI_AC_1.setGeometry(QtCore.QRect(204, 540, 47, 25))
        self.AI_AC_1.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.AI_AC_1.setObjectName("AI_AC_1")
        self.L_AC_3 = QtWidgets.QLabel(Dialog)
        self.L_AC_3.setGeometry(QtCore.QRect(134, 600, 47, 25))
        self.L_AC_3.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.L_AC_3.setObjectName("L_AC_3")
        self.L_AC_1 = QtWidgets.QLabel(Dialog)
        self.L_AC_1.setGeometry(QtCore.QRect(134, 540, 47, 25))
        self.L_AC_1.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.L_AC_1.setObjectName("L_AC_1")
        self.AI_AC_3 = QtWidgets.QLabel(Dialog)
        self.AI_AC_3.setGeometry(QtCore.QRect(204, 600, 47, 25))
        self.AI_AC_3.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.AI_AC_3.setObjectName("AI_AC_3")
        self.L_AC_2 = QtWidgets.QLabel(Dialog)
        self.L_AC_2.setGeometry(QtCore.QRect(134, 570, 47, 25))
        self.L_AC_2.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.L_AC_2.setObjectName("L_AC_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(204, 500, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(222, 114, 94);")
        self.pushButton.setObjectName("pushButton")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(57, 490, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgba(200,200,200,0.9);")
        self.label_19.setObjectName("label_19")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(60, 565, 180, 1))
        self.line.setStyleSheet("border: 0.5px solid grey;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(60, 594, 180, 1))
        self.line_2.setStyleSheet("border: 0.5px solid grey;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(60, 623, 180, 1))
        self.line_3.setStyleSheet("border: 0.5px solid grey;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 460, 271, 181))
        self.label_6.setStyleSheet("border:2px solid gray;border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.calendarWidget.raise_()
        self.widget_rms_1.raise_()
        self.widget_rms_2.raise_()
        self.widget_rms_4.raise_()
        self.pushButton_cost_AI.raise_()
        self.label_79.raise_()
        self.pushButton_energy_AI.raise_()
        self.label_84.raise_()
        self.label_4.raise_()
        self.pushButton_cost_AI_2.raise_()
        self.pushButton_energy_AI_2.raise_()
        self.label_87.raise_()
        self.label_80.raise_()
        self.chiller_label.raise_()
        self.chiller_label_2.raise_()
        self.label_7.raise_()
        self.AI_AC_2.raise_()
        self.label_8.raise_()
        self.label_12.raise_()
        self.label_16.raise_()
        self.AI_AC_1.raise_()
        self.L_AC_3.raise_()
        self.L_AC_1.raise_()
        self.AI_AC_3.raise_()
        self.L_AC_2.raise_()
        self.pushButton.raise_()
        self.label_19.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.verticalSlider.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_44.setText(_translate("Dialog", "Outside Temperature ~ C"))
        self.label_45.setText(_translate("Dialog", "▆"))
        self.label_50.setText(_translate("Dialog", "▆"))
        self.label_51.setText(_translate("Dialog", "Outside Humidity ~ %"))
        self.label_52.setText(_translate("Dialog", "▆"))
        self.label_53.setText(_translate("Dialog", "Legacy Cost Control ~ 만원"))
        self.label_54.setText(_translate("Dialog", "▆"))
        self.label_55.setText(_translate("Dialog", "AI Cost Control ~ 만원"))
        self.label_48.setText(_translate("Dialog", "AI Energy Control ~ GJ"))
        self.label_49.setText(_translate("Dialog", "▆"))
        self.label_59.setText(_translate("Dialog", "Legacy Energy Control ~ GJ"))
        self.label_58.setText(_translate("Dialog", "▆"))
        self.label_79.setText(_translate("Dialog", "Cost Saved Per Day"))
        self.label_84.setText(_translate("Dialog", "Energy Saved Per Day"))
        self.label_87.setText(_translate("Dialog", "Energy Saved Per 30 min"))
        self.label_80.setText(_translate("Dialog", "Cost Saved Per 30 min"))
        self.chiller_label.setText(_translate("Dialog", "Chiller Information at"))
        self.chiller_label_2.setText(_translate("Dialog", "23:30"))
        self.label_7.setText(_translate("Dialog", "LTC"))
        self.AI_AC_2.setText(_translate("Dialog", "AAAA"))
        self.label_8.setText(_translate("Dialog", "AC"))
        self.label_12.setText(_translate("Dialog", "Legacy"))
        self.label_16.setText(_translate("Dialog", "STC"))
        self.AI_AC_1.setText(_translate("Dialog", "AAAA"))
        self.L_AC_3.setText(_translate("Dialog", "AAAA"))
        self.L_AC_1.setText(_translate("Dialog", "AAAA"))
        self.AI_AC_3.setText(_translate("Dialog", "AAAA"))
        self.L_AC_2.setText(_translate("Dialog", "AAAA"))
        self.pushButton.setText(_translate("Dialog", "AI"))
        self.label_19.setText(_translate("Dialog", "Chiller"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
