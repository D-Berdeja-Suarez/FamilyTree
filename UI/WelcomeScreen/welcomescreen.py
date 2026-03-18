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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_welcomescreen(object):
    def setupUi(self, welcomescreen):
        if not welcomescreen.objectName():
            welcomescreen.setObjectName(u"welcomescreen")
        welcomescreen.resize(319, 186)
        self.centralwidget = QWidget(welcomescreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_new = QPushButton(self.widget_3)
        self.pb_new.setObjectName(u"pb_new")

        self.horizontalLayout.addWidget(self.pb_new)

        self.pb_load = QPushButton(self.widget_3)
        self.pb_load.setObjectName(u"pb_load")

        self.horizontalLayout.addWidget(self.pb_load)


        self.verticalLayout_2.addWidget(self.widget_3)

        welcomescreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(welcomescreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 319, 36))
        welcomescreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(welcomescreen)
        self.statusbar.setObjectName(u"statusbar")
        welcomescreen.setStatusBar(self.statusbar)

        self.retranslateUi(welcomescreen)

        QMetaObject.connectSlotsByName(welcomescreen)
    # setupUi

    def retranslateUi(self, welcomescreen):
        welcomescreen.setWindowTitle(QCoreApplication.translate("welcomescreen", u"Welcome Screen", None))
        self.lineEdit.setText(QCoreApplication.translate("welcomescreen", u"familytree", None))
        self.label.setText(QCoreApplication.translate("welcomescreen", u".db", None))
        self.pb_new.setText(QCoreApplication.translate("welcomescreen", u"New", None))
        self.pb_load.setText(QCoreApplication.translate("welcomescreen", u"Load", None))
    # retranslateUi

