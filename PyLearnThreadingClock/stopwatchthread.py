import time
from PySide6.QtCore import *
from mytime import MyTime


class StopWatchThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        # self.second = 0
        self.time = MyTime(0,0,0)

    def run(self):
        while True:
            self.time.add_second()
            time.sleep(1)
            # print(self.second)
            self.signal_show.emit(self.time)
        
    def reset(self):
        self.time.second = 0
        self.time.minute = 0
        self.time.hour = 0