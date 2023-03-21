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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(374, 391)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_tehran_2 = QLabel(self.tab)
        self.lb_tehran_2.setObjectName(u"lb_tehran_2")
        font = QFont()
        font.setFamilies([u"Centaur"])
        font.setPointSize(16)
        self.lb_tehran_2.setFont(font)

        self.gridLayout_4.addWidget(self.lb_tehran_2, 0, 0, 1, 1)

        self.lb_tehran = QLabel(self.tab)
        self.lb_tehran.setObjectName(u"lb_tehran")
        self.lb_tehran.setFont(font)

        self.gridLayout_4.addWidget(self.lb_tehran, 0, 1, 1, 1)

        self.lb_tehran_3 = QLabel(self.tab)
        self.lb_tehran_3.setObjectName(u"lb_tehran_3")
        self.lb_tehran_3.setFont(font)

        self.gridLayout_4.addWidget(self.lb_tehran_3, 1, 0, 1, 1)

        self.lb_berlin = QLabel(self.tab)
        self.lb_berlin.setObjectName(u"lb_berlin")
        self.lb_berlin.setFont(font)

        self.gridLayout_4.addWidget(self.lb_berlin, 1, 1, 1, 1)

        self.lb_tehran_5 = QLabel(self.tab)
        self.lb_tehran_5.setObjectName(u"lb_tehran_5")
        self.lb_tehran_5.setFont(font)

        self.gridLayout_4.addWidget(self.lb_tehran_5, 2, 0, 1, 1)

        self.lb_washington = QLabel(self.tab)
        self.lb_washington.setObjectName(u"lb_washington")
        self.lb_washington.setFont(font)

        self.gridLayout_4.addWidget(self.lb_washington, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gl_alarms = QGridLayout()
        self.gl_alarms.setObjectName(u"gl_alarms")

        self.gridLayout_2.addLayout(self.gl_alarms, 0, 0, 1, 2)

        self.btn_addalarm = QPushButton(self.tab_2)
        self.btn_addalarm.setObjectName(u"btn_addalarm")
        font1 = QFont()
        font1.setFamilies([u"Centaur"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.btn_addalarm.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_addalarm, 1, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.tab_2)
        self.timeEdit.setObjectName(u"timeEdit")
        font2 = QFont()
        font2.setPointSize(14)
        self.timeEdit.setFont(font2)

        self.gridLayout_2.addWidget(self.timeEdit, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        font3 = QFont()
        font3.setFamilies([u"Seven Segment"])
        font3.setPointSize(40)
        self.label_stopwatch.setFont(font3)
        self.label_stopwatch.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_stopwatch.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_stopwatch, 0, 0, 1, 3)

        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        font4 = QFont()
        font4.setFamilies([u"Centaur"])
        font4.setPointSize(18)
        self.btn_start_stopwatch.setFont(font4)

        self.gridLayout_3.addWidget(self.btn_start_stopwatch, 1, 0, 1, 1)

        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setFont(font4)

        self.gridLayout_3.addWidget(self.btn_stop_stopwatch, 1, 1, 1, 1)

        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setFont(font4)

        self.gridLayout_3.addWidget(self.btn_reset_stopwatch, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_hour_timer = QLineEdit(self.tab_4)
        self.tb_hour_timer.setObjectName(u"tb_hour_timer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_hour_timer.sizePolicy().hasHeightForWidth())
        self.tb_hour_timer.setSizePolicy(sizePolicy)
        self.tb_hour_timer.setMaximumSize(QSize(100, 100))
        self.tb_hour_timer.setFont(font3)
        self.tb_hour_timer.setStyleSheet(u"")
        self.tb_hour_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.tb_hour_timer)

        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.label)

        self.tb_minute_timer = QLineEdit(self.tab_4)
        self.tb_minute_timer.setObjectName(u"tb_minute_timer")
        sizePolicy.setHeightForWidth(self.tb_minute_timer.sizePolicy().hasHeightForWidth())
        self.tb_minute_timer.setSizePolicy(sizePolicy)
        self.tb_minute_timer.setMaximumSize(QSize(100, 100))
        self.tb_minute_timer.setFont(font3)
        self.tb_minute_timer.setStyleSheet(u"")
        self.tb_minute_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.tb_minute_timer)

        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.horizontalLayout.addWidget(self.label_2)

        self.tb_second_timer = QLineEdit(self.tab_4)
        self.tb_second_timer.setObjectName(u"tb_second_timer")
        sizePolicy.setHeightForWidth(self.tb_second_timer.sizePolicy().hasHeightForWidth())
        self.tb_second_timer.setSizePolicy(sizePolicy)
        self.tb_second_timer.setMaximumSize(QSize(100, 100))
        self.tb_second_timer.setFont(font3)
        self.tb_second_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.tb_second_timer)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        font5 = QFont()
        font5.setFamilies([u"Centaur"])
        font5.setPointSize(15)
        self.btn_start_timer.setFont(font5)

        self.gridLayout_5.addWidget(self.btn_start_timer, 1, 0, 1, 1)

        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setFont(font5)

        self.gridLayout_5.addWidget(self.btn_stop_timer, 1, 1, 1, 1)

        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setFont(font5)

        self.gridLayout_5.addWidget(self.btn_reset_timer, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 374, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.lb_tehran_2.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_3.setText(QCoreApplication.translate("MainWindow", u"Berlin", None))
        self.lb_berlin.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_5.setText(QCoreApplication.translate("MainWindow", u"Washington", None))
        self.lb_washington.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.btn_addalarm.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"rest", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.tb_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"rest", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

