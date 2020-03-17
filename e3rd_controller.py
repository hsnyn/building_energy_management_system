from ui_third_floor import Ui_Dialog
from PyQt5 import QtCore
class ThirdController(Ui_Dialog):
    def __init__(self):
        super(ThirdController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(ThirdController, self).exec_()