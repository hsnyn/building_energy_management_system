from ui_four_floor import Ui_Dialog
from PyQt5 import QtCore
class fourController(Ui_Dialog):
    def __init__(self):
        super(fourController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(fourController, self).exec_()