import time
from PySide6.QtCore import *
from mytime import MyTime

class WorldClockThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.timeTehran = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))
        self.timeBerlin = self.timeTehran.sub(MyTime(2,30,0))
        self.timeWashington = self.timeTehran.sub(MyTime(7,30,0))

    def run(self):
        while True:
            self.timeTehran.add_second()
            self.signal_show.emit(self.timeTehran)
            time.sleep(1)
            # print(self.second)

