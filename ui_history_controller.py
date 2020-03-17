from ui_history import Ui_Dialog
import pandas as pd
from threading import Thread
from PyQt5 import QtCore, QtGui
from pyqtgraph import mkPen
import time
class HistoryController(Ui_Dialog):
    def main_function(self):
        print('Daily History')
        while 1:
            alpha = self.calendarWidget.selectedDate()
            alpha = alpha.toString("yyyy-MM-dd")
            self.data_copy = self.data.copy()
            if alpha in self.data_copy['Date'].unique():
                self.data_of_date = self.data_copy.loc[self.data_copy['Date'] == alpha]
                self.data_of_date = self.data_of_date.reset_index(drop=True)
                sum_legacy_cost = sum(self.data_of_date['Legacy_cost (t+1)'].values)
                sum_AI_cost = sum(self.data_of_date['AI_cost (t+1)'].values)
                self.pushButton_cost_AI.setText("{0:.1f}".format(((sum_legacy_cost-sum_AI_cost)/sum_legacy_cost) * 100) + ' %')
                sum_legacy_energy = sum(self.data_of_date['Legacy_energyProd (t+1)'].values)
                sum_AI_energy = sum(self.data_of_date['AI_energyProd (t+1)'].values)
                self.pushButton_energy_AI.setText("{0:.1f}".format(((sum_legacy_energy - sum_AI_energy) / sum_legacy_energy) * 100) + ' %')
                ticks_alpha = self.data_of_date['Time'].values
                self.verticalSlider.setMaximum(len(ticks_alpha)-1)
                major_ticks = list(zip(range(len(ticks_alpha))[1::3], list(ticks_alpha)[1::3]))
                minor_ticks = list(zip(range(len(ticks_alpha)), list(ticks_alpha)))
                selection_value = int(self.verticalSlider.value())
                self.pushButton_cost_AI_2.setText("{0:.1f}".format(((self.data_of_date['Legacy_cost (t+1)'][selection_value] - self.data_of_date['AI_cost (t+1)'][selection_value]) / self.data_of_date['Legacy_cost (t+1)'][selection_value]) * 100) + ' %')
                self.pushButton_energy_AI_2.setText("{0:.1f}".format(((self.data_of_date['Legacy_energyProd (t+1)'][selection_value] -self.data_of_date['AI_energyProd (t+1)'][selection_value]) /self.data_of_date['Legacy_energyProd (t+1)'][selection_value]) * 100) + ' %')
                self.chiller_label_2.setText(self.data_of_date['Time'][selection_value])
                self.widget_rms_1.getAxis('bottom').setTicks([major_ticks, minor_ticks]), self.widget_rms_2.getAxis('bottom').setTicks([major_ticks, minor_ticks]), self.widget_rms_4.getAxis('bottom').setTicks([major_ticks, minor_ticks])
                self.out_temp_plot.setData(self.data_of_date['Otemp'].values)
                self.out_hum_plot.setData(self.data_of_date['Ohum'].values/2)
                self.cost_legacy_plot.setData(self.data_of_date['Legacy_cost (t+1)'].values/10000)
                self.cost_ai_plot.setData(self.data_of_date['AI_cost (t+1)'].values/10000)
                self.ene_legacy_plot.setData(self.data_of_date['Legacy_energyProd (t+1)'].values/1000)
                self.ene_ai_plot.setData(self.data_of_date['AI_energyProd (t+1)'].values/1000)
                if self.data_of_date['Legacy_AC_action (t)'][selection_value] != 0:self.L_AC_1.setPixmap(QtGui.QPixmap('on.png'))
                else: self.L_AC_1.setPixmap(QtGui.QPixmap('off.png'))
                if self.data_of_date['Legacy_LTC_action (t)'][selection_value] != 0:self.L_AC_2.setPixmap(QtGui.QPixmap('on.png'))
                else: self.L_AC_2.setPixmap(QtGui.QPixmap('off.png'))
                if self.data_of_date['Legacy_STC_action (t)'][selection_value] != 0:self.L_AC_3.setPixmap(QtGui.QPixmap('on.png'))
                else: self.L_AC_3.setPixmap(QtGui.QPixmap('off.png'))
                if self.data_of_date['AI_AC_action (t)'][selection_value] != 0:self.AI_AC_1.setPixmap(QtGui.QPixmap('on.png'))
                else:self.AI_AC_1.setPixmap(QtGui.QPixmap('off.png'))
                if self.data_of_date['AI_LTC_action (t)'][selection_value] != 0:self.AI_AC_2.setPixmap(QtGui.QPixmap('on.png'))
                else:self.AI_AC_2.setPixmap(QtGui.QPixmap('off.png'))
                if self.data_of_date['AI_STC_action (t)'][selection_value] != 0: self.AI_AC_3.setPixmap(QtGui.QPixmap('on.png'))
                else:self.AI_AC_3.setPixmap(QtGui.QPixmap('off.png'))
                if self.widget_rms_1.isVisible() == False:
                    break
            time.sleep(1)
    def __init__(self):
        super(HistoryController, self).__init__()
        filename = pd.read_csv('file_input', header=None).values
        self.data = pd.read_csv(filename[0][0])
    def setupUi(self, Ui_Form_stats):
        Ui_Dialog.setupUi(self, Ui_Form_stats)
        Ui_Form_stats.setWindowTitle('Daily Report View')
        self.widget_rms_1.showGrid(x=False, y=True, alpha=0.3)
        self.widget_rms_1.setBackground((0, 0, 0))
        self.widget_rms_1.setLabel('right', **{'color': '#000000', 'font-size': '10pt'})
        self.widget_rms_2.setMenuEnabled(False)
        self.widget_rms_2.showGrid(x=False, y=True, alpha=0.3)
        self.widget_rms_2.setBackground((0, 0, 0))
        self.widget_rms_2.setLabel('right', **{'color': '#000000', 'font-size': '10pt'})
        self.widget_rms_4.setMenuEnabled(False)
        self.widget_rms_4.showGrid(x=False, y=True, alpha=0.3)
        self.widget_rms_4.setLabel('right', **{'color': '#000000', 'font-size': '10pt'})
        self.widget_rms_4.setLabel('bottom', "Time", **{'color': '#999999', 'font-size': '10pt'})
        self.widget_rms_4.setBackground((0, 0, 0))
        self.out_temp_plot = self.widget_rms_1.plot(name="Outside Temperature", symbolPen=None, symbol='o',symbolSize=3, symbolBrush=(222, 114, 94), fillLevel=0.0,brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        self.out_hum_plot = self.widget_rms_1.plot(name="Outside humidity", symbolPen=None, symbol='o', symbolSize=3, symbolBrush=(60, 114, 174), fillLevel=0.0, brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.cost_legacy_plot = self.widget_rms_2.plot(name="Legacy Control", symbolPen=None, symbol='o', symbolSize=3,symbolBrush=(60, 114, 174), fillLevel=0.0,brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.cost_ai_plot = self.widget_rms_2.plot(name="AI Control", symbolPen=None, symbol='o', symbolSize=3,symbolBrush=(222, 114, 94), fillLevel=0.0, brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        self.ene_legacy_plot = self.widget_rms_4.plot(name="Legacy Control", symbol='o', symbolSize=3,symbolBrush=(60, 114, 174), fillLevel=0.0,brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.ene_ai_plot = self.widget_rms_4.plot(name="AI Control", symbolPen=None, symbol='o', symbolSize=3,symbolBrush=(222, 114, 94), fillLevel=0.0, brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        Thread(target=self.main_function, daemon=True).start()
    def exec_(self):
        super(HistoryController, self).exec_()