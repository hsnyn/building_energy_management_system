from PyQt5 import QtCore
from ui_nineth_floor import Ui_Dialog
class ninthController(Ui_Dialog):
    def __init__(self):
        super(ninthController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(ninthController, self).exec_()