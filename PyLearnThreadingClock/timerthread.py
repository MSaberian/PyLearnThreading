import time
from PySide6.QtCore import *
from mytime import MyTime

class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        # self.second = 0
        self.time = MyTime(0,15,0)

    def run(self):
        while True:
            self.time.sub_second()
            self.signal_show.emit(self.time)
            time.sleep(1)
            # print(self.second)

    def set_time(self,hour,minute,second):
        self.time.hour = hour
        self.time.minute = minute
        self.time.second = second

    # def reset()
