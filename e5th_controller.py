from ui_fifth_floor import Ui_Dialog
from PyQt5 import QtCore
class fifthController(Ui_Dialog):
    def __init__(self):
        super(fifthController, self).__init__()
    def setupUi(self, Ui_Dialog_stats):
        Ui_Dialog.setupUi(self, Ui_Dialog_stats)
        Ui_Dialog_stats.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def exec_(self):
        super(fifthController, self).exec_()