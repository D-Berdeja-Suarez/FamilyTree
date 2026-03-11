# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treeviewer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeView, QVBoxLayout, QWidget)

class Ui_mainwwin_treeviewer(object):
    def setupUi(self, mainwwin_treeviewer):
        if not mainwwin_treeviewer.objectName():
            mainwwin_treeviewer.setObjectName(u"mainwwin_treeviewer")
        mainwwin_treeviewer.resize(800, 600)
        self.wid_centralwidget = QWidget(mainwwin_treeviewer)
        self.wid_centralwidget.setObjectName(u"wid_centralwidget")
        self.verticalLayout = QVBoxLayout(self.wid_centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.wid_centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeView = QTreeView(self.widget)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_3.addWidget(self.treeView)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.wid_centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_ascendance = QPushButton(self.widget_3)
        self.pb_ascendance.setObjectName(u"pb_ascendance")

        self.horizontalLayout_2.addWidget(self.pb_ascendance)

        self.pb_descendance = QPushButton(self.widget_3)
        self.pb_descendance.setObjectName(u"pb_descendance")

        self.horizontalLayout_2.addWidget(self.pb_descendance)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pb_load = QPushButton(self.widget_4)
        self.pb_load.setObjectName(u"pb_load")

        self.verticalLayout_2.addWidget(self.pb_load)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        mainwwin_treeviewer.setCentralWidget(self.wid_centralwidget)
        self.menubar = QMenuBar(mainwwin_treeviewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 36))
        mainwwin_treeviewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainwwin_treeviewer)
        self.statusbar.setObjectName(u"statusbar")
        mainwwin_treeviewer.setStatusBar(self.statusbar)

        self.retranslateUi(mainwwin_treeviewer)

        QMetaObject.connectSlotsByName(mainwwin_treeviewer)
    # setupUi

    def retranslateUi(self, mainwwin_treeviewer):
        mainwwin_treeviewer.setWindowTitle(QCoreApplication.translate("mainwwin_treeviewer", u"Tree Viewer", None))
        self.pb_ascendance.setText(QCoreApplication.translate("mainwwin_treeviewer", u"\u2190 Ascendance", None))
        self.pb_descendance.setText(QCoreApplication.translate("mainwwin_treeviewer", u"Descendance \u2192", None))
        self.pb_load.setText(QCoreApplication.translate("mainwwin_treeviewer", u"Load FamilyTree", None))
    # retranslateUi

