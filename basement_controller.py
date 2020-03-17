from ui_basement_floor import Ui_Dialog
from PyQt5 import QtCore
class basementController(Ui_Dialog):
    def __init__(self):
        super(basementController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(basementController, self).exec_()