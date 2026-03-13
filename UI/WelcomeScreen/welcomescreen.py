# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomescreen.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_welcomescreen(object):
    def setupUi(self, welcomescreen):
        if not welcomescreen.objectName():
            welcomescreen.setObjectName(u"welcomescreen")
        welcomescreen.resize(389, 431)
        self.centralwidget = QWidget(welcomescreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout.addWidget(self.widget_4)

        self.pb_load = QPushButton(self.widget_3)
        self.pb_load.setObjectName(u"pb_load")

        self.verticalLayout.addWidget(self.pb_load)

        self.pb_new = QPushButton(self.widget_3)
        self.pb_new.setObjectName(u"pb_new")

        self.verticalLayout.addWidget(self.pb_new)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        welcomescreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(welcomescreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 389, 36))
        welcomescreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(welcomescreen)
        self.statusbar.setObjectName(u"statusbar")
        welcomescreen.setStatusBar(self.statusbar)

        self.retranslateUi(welcomescreen)

        QMetaObject.connectSlotsByName(welcomescreen)
    # setupUi

    def retranslateUi(self, welcomescreen):
        welcomescreen.setWindowTitle(QCoreApplication.translate("welcomescreen", u"Welcome Screen", None))
        self.pb_load.setText(QCoreApplication.translate("welcomescreen", u"Load", None))
        self.pb_new.setText(QCoreApplication.translate("welcomescreen", u"New", None))
    # retranslateUi

