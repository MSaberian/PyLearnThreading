import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from stopwatchthread import StopWatchThread
from timerthread import TimerThread
from main_window import Ui_MainWindow 
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
        qdarktheme.setup_theme("dark")

        self.thered_timer = TimerThread()
        self.thread_stopwatch = StopWatchThread()
        self.thered_timer.signal_show.connect(self.show_time_timer)
        self.thread_stopwatch.signal_show.connect(self.show_number_stopwatch)

    def start_timer(self):
        self.thered_timer.start()

    # @Slot
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    # @Slot
    def show_number_stopwatch(self):
        self.ui.label_stopwatch.setText(f'{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.minute}:{self.thread_stopwatch.time.second}')

    # @Slot
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    # @Slot
    def show_time_timer(self):
        self.ui.tb_hour_timer.setText(str(self.thered_timer.time.hour))
        self.ui.tb_minute_timer.setText(str(self.thered_timer.time.minute))
        self.ui.tb_second_timer.setText(str(self.thered_timer.time.second))


    # @Slot    
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()