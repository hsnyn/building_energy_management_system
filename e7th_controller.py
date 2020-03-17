from ui_seven_floor import Ui_Dialog
from PyQt5 import QtCore
class sevenController(Ui_Dialog):
    def __init__(self):
        super(sevenController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(sevenController, self).exec_()