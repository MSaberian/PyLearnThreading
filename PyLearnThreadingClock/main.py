import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from stopwatchthread import StopWatchThread
from timerthread import TimerThread
from worldclock import WorldClockThread
from main_window import Ui_MainWindow 
from plyer.utils import platform
from plyer import notification
import qdarktheme


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_stopwatch.setText('0:0:0')
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        qdarktheme.setup_theme("dark")

        self.thered_timer = TimerThread()
        self.thread_stopwatch = StopWatchThread()
        self.thread_WorldClock = WorldClockThread()
        self.thered_timer.signal_show.connect(self.show_time_timer)
        self.thread_stopwatch.signal_show.connect(self.show_number_stopwatch)
        self.thread_WorldClock.signal_show.connect(self.show_world_clock)
        self.thread_WorldClock.start()


    def show_world_clock(self):
        self.thread_WorldClock.timeBerlin = self.thread_WorldClock.timeTehran.sub(MyTime(2,30,0))
        self.thread_WorldClock.timeWashington = self.thread_WorldClock.timeTehran.sub(MyTime(7,30,0))
        self.ui.lb_tehran.setText(f'{self.thread_WorldClock.timeTehran.hour}:{self.thread_WorldClock.timeTehran.minute}:{self.thread_WorldClock.timeTehran.second}')
        self.ui.lb_berlin.setText(f'{self.thread_WorldClock.timeBerlin.hour}:{self.thread_WorldClock.timeBerlin.minute}:{self.thread_WorldClock.timeBerlin.second}')
        self.ui.lb_washington.setText(f'{self.thread_WorldClock.timeWashington.hour}:{self.thread_WorldClock.timeWashington.minute}:{self.thread_WorldClock.timeWashington.second}')

    # @Slot
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    # @Slot
    def show_number_stopwatch(self):
        self.ui.label_stopwatch.setText(f'{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.minute}:{self.thread_stopwatch.time.second}')

    # @Slot    
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()

    # @Slot
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def start_timer(self):
        if self.thered_timer.time.second + self.thered_timer.time.minute + self.thered_timer.time.hour != 0:
            self.thered_timer.set_time(int(self.ui.tb_hour_timer.text()),int(self.ui.tb_minute_timer.text()),int(self.ui.tb_second_timer.text()))
            self.thered_timer.start()

    # @Slot
    def show_time_timer(self):
        self.ui.tb_hour_timer.setText(str(self.thered_timer.time.hour))
        self.ui.tb_minute_timer.setText(str(self.thered_timer.time.minute))
        self.ui.tb_second_timer.setText(str(self.thered_timer.time.second))
        if self.thered_timer.time.second + self.thered_timer.time.minute + self.thered_timer.time.hour == 0:
            self.thered_timer.terminate()
            notification.notify(
                title='Clock',
                message='Timer Alarm',
                app_name='Clock',
            )

    def stop_timer(self):
        self.thered_timer.terminate()

    def reset_timer(self):
        self.thered_timer.set_time(0,15,0)
        self.ui.tb_hour_timer.setText(str(self.thered_timer.time.hour))
        self.ui.tb_minute_timer.setText(str(self.thered_timer.time.minute))
        self.ui.tb_second_timer.setText(str(self.thered_timer.time.second))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()