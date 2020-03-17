from ui_calendar import Ui_Form
import time
from threading import Thread
class CalendarController(Ui_Form):
    def __init__(self):
        super(CalendarController, self).__init__()
    def get_date(self):
        print('Calender Thread Started')
        t_end = time.time()+60
        while time.time() < t_end:
            f = open('date.txt', 'w'); alpha = self.calendarWidget.selectedDate(); f.write(alpha.toString("yyyy-MM-dd")); f.close()
            time.sleep(0.2)
            if self.calendarWidget.isVisible() == False:
                print('Calender Thread Stopped')
                break
    def setupUi(self, Ui_Form_stats):
        Ui_Form.setupUi(self, Ui_Form_stats)
        Ui_Form_stats.setWindowTitle('Please Select Date')
        Thread(target=self.get_date, daemon=True).start()
    def exec_(self):
        super(CalendarController, self).exec_()