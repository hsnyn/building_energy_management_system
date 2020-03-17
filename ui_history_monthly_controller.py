from ui_history_monthly import Ui_Dialog
import pandas as pd
from threading import Thread
from PyQt5 import QtCore, QtGui
from pyqtgraph import mkPen
import time
class MonthlyHistoryController(Ui_Dialog):
    def main_function(self):
        while 1:
            data_now = self.data.copy()
            if self.comboBox.currentText() in self.data['CreatedDate'].unique():
                data_now_selected = data_now.loc[data_now['CreatedDate'] == self.comboBox.currentText()]
                data_now_selected = data_now_selected.reset_index(drop=True)
                sum_legacy_cost = sum(data_now_selected['Legacy_cost (t+1)'].values)
                sum_AI_cost = sum(data_now_selected['AI_cost (t+1)'].values)
                self.pushButton.setText("{0:.1f}".format(((sum_legacy_cost - sum_AI_cost) / sum_legacy_cost) * 100) + ' %')
                sum_legacy_energy = sum(data_now_selected['Legacy_energyProd (t+1)'].values)
                sum_AI_energy = sum(data_now_selected['AI_energyProd (t+1)'].values)
                self.pushButton_2.setText("{0:.1f}".format(((sum_legacy_energy - sum_AI_energy) / sum_legacy_energy) * 100) + ' %')
                ticks_alpha = data_now_selected['CreatedDateTime'].values
                major_ticks = list(zip(range(len(ticks_alpha))[1::120], list(ticks_alpha)[1::120]))
                minor_ticks = list(zip(range(len(ticks_alpha)), list(ticks_alpha)))
                self.widget_rms_1.getAxis('bottom').setTicks([major_ticks, minor_ticks]), self.widget_rms_2.getAxis('bottom').setTicks([major_ticks, minor_ticks]), self.widget_rms_4.getAxis('bottom').setTicks([major_ticks, minor_ticks])
                self.out_temp_plot.setData(data_now_selected['Otemp'].values)
                self.out_hum_plot.setData(data_now_selected['Ohum'].values / 2)
                self.cost_legacy_plot.setData(data_now_selected['Legacy_cost (t+1)'].values / 10000)
                self.cost_ai_plot.setData(data_now_selected['AI_cost (t+1)'].values / 10000)
                self.ene_legacy_plot.setData(data_now_selected['Legacy_energyProd (t+1)'].values / 1000)
                self.ene_ai_plot.setData(data_now_selected['AI_energyProd (t+1)'].values / 1000)
                if self.widget_rms_1.isVisible() == False:
                    break
            time.sleep(1)
    def __init__(self):
        super(MonthlyHistoryController, self).__init__()
        filename = pd.read_csv('file_input', header=None).values
        self.data = pd.read_csv(filename[0][0])
        self.data['CreatedDate'] = self.data['Date'].str.split('-').str[0]+'.'+self.data['Date'].str.split('-').str[1]
        self.alpha = self.data['CreatedDate'].unique()
        self.data['CreatedDateTime'] =  self.data['Date'] +' - '+ self.data['Time']
    def setupUi(self, Ui_Form_stats):
        Ui_Dialog.setupUi(self, Ui_Form_stats)
        Ui_Form_stats.setWindowTitle('Monthly Report View')
        for i in range(len(self.alpha)):
            self.comboBox.addItem(self.alpha[i])
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
        self.widget_rms_4.setBackground((0, 0, 0))
        self.widget_rms_4.setLabel('bottom', "Date - Time", **{'color': '#999999', 'font-size': '10pt'})
        self.out_temp_plot = self.widget_rms_1.plot(name="Outside Temperature", fillLevel=0.0,brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        self.out_hum_plot = self.widget_rms_1.plot(name="Outside humidity", fillLevel=0.0, brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.cost_legacy_plot = self.widget_rms_2.plot(name="Legacy Control", fillLevel=0.0,brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.cost_ai_plot = self.widget_rms_2.plot(name="AI Control", fillLevel=0.0, brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        self.ene_legacy_plot = self.widget_rms_4.plot(name="Legacy Control", fillLevel=0.0,brush=(60, 114, 174, 50),pen=mkPen((60, 114, 174), width=1, style=QtCore.Qt.SolidLine))
        self.ene_ai_plot = self.widget_rms_4.plot(name="AI Control", fillLevel=0.0, brush=(222, 114, 94, 50),pen=mkPen((222, 114, 94), width=1, style=QtCore.Qt.SolidLine))
        Thread(target=self.main_function, daemon=True).start()
    def exec_(self):
        super(MonthlyHistoryController, self).exec_()