# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(485, 367)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 10, 391, 321))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(50, 30, 261, 61))
        font = QFont()
        font.setFamilies([u"Seven Segment"])
        font.setPointSize(40)
        self.label_stopwatch.setFont(font)
        self.label_stopwatch.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(50, 110, 75, 24))
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(150, 110, 75, 24))
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(250, 110, 75, 24))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tb_hour_timer = QLineEdit(self.tab_4)
        self.tb_hour_timer.setObjectName(u"tb_hour_timer")
        self.tb_hour_timer.setGeometry(QRect(90, 60, 50, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_hour_timer.sizePolicy().hasHeightForWidth())
        self.tb_hour_timer.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(30)
        self.tb_hour_timer.setFont(font1)
        self.tb_hour_timer.setStyleSheet(u"")
        self.tb_hour_timer.setAlignment(Qt.AlignCenter)
        self.tb_minute_timer = QLineEdit(self.tab_4)
        self.tb_minute_timer.setObjectName(u"tb_minute_timer")
        self.tb_minute_timer.setGeometry(QRect(160, 60, 50, 50))
        sizePolicy.setHeightForWidth(self.tb_minute_timer.sizePolicy().hasHeightForWidth())
        self.tb_minute_timer.setSizePolicy(sizePolicy)
        self.tb_minute_timer.setFont(font1)
        self.tb_minute_timer.setStyleSheet(u"")
        self.tb_minute_timer.setAlignment(Qt.AlignCenter)
        self.tb_second_timer = QLineEdit(self.tab_4)
        self.tb_second_timer.setObjectName(u"tb_second_timer")
        self.tb_second_timer.setGeometry(QRect(230, 60, 50, 50))
        sizePolicy.setHeightForWidth(self.tb_second_timer.sizePolicy().hasHeightForWidth())
        self.tb_second_timer.setSizePolicy(sizePolicy)
        self.tb_second_timer.setFont(font1)
        self.tb_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(60, 140, 75, 24))
        self.btn_reset_stopwatch_2 = QPushButton(self.tab_4)
        self.btn_reset_stopwatch_2.setObjectName(u"btn_reset_stopwatch_2")
        self.btn_reset_stopwatch_2.setGeometry(QRect(240, 140, 75, 24))
        self.btn_stop_stopwatch_2 = QPushButton(self.tab_4)
        self.btn_stop_stopwatch_2.setObjectName(u"btn_stop_stopwatch_2")
        self.btn_stop_stopwatch_2.setGeometry(QRect(150, 140, 75, 24))
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 485, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"rest", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.tb_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tb_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.tb_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_reset_stopwatch_2.setText(QCoreApplication.translate("MainWindow", u"rest", None))
        self.btn_stop_stopwatch_2.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi
