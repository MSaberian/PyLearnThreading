import time
from PySide6.QtCore import *
from mytime import MyTime
from plyer.utils import platform
from plyer import notification

class AlarmThread(QThread):
    def __init__(self):
        super().__init__()
        self.Time_Alarms = []
        self.current_time = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))

    def run(self):
        while True:
            self.current_time.add_second()
            time.sleep(1)
            for alarmtime in self.Time_Alarms:
                if self.current_time.equal(alarmtime):
                    notification.notify(
                        title='Alarm',
                        message= alarmtime.toString(),
                        app_name='Clock',
                    )
            
        