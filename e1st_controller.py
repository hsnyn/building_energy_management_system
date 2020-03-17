from ui_first_floor import Ui_Dialog
from PyQt5 import QtCore
class FirstController(Ui_Dialog):
    def __init__(self):
        super(FirstController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(FirstController, self).exec_()