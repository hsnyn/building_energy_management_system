from ui_inside_temp import Ui_Dialog
from pyqtgraph import mkPen
from PyQt5 import QtCore
class InsideTempController(Ui_Dialog):
    def __init__(self):
        super(InsideTempController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        self.widget_rms_1.setMenuEnabled(False)
        self.widget_rms_1.showGrid(x=False, y=True, alpha=0.3)
        self.widget_rms_1.setBackground((0, 0, 0))
        self.widget_rms_1.setLabel('right', **{'color': '#000000', 'font-size': '10pt'})
        self.widget_rms_1.setLabel('bottom', "Time", **{'color': '#999999', 'font-size': '10pt'})
        self.inside_temp_plot = self.widget_rms_1.plot(name="Outside Temperature", symbolPen=None, symbol='o',symbolSize=5, symbolBrush=(222, 114, 94),fillLevel=20.0, brush=(222, 114, 94,50),pen=mkPen((222, 114, 94), width=2, style=QtCore.Qt.DotLine))
    def exec_(self):
        super(InsideTempController, self).exec_()