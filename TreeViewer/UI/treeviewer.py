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
    QStatusBar, QTabWidget, QTreeView, QVBoxLayout,
    QWidget)

class Ui_mainwwin_treeviewer(object):
    def setupUi(self, mainwwin_treeviewer):
        if not mainwwin_treeviewer.objectName():
            mainwwin_treeviewer.setObjectName(u"mainwwin_treeviewer")
        mainwwin_treeviewer.resize(800, 600)
        self.wid_centralwidget = QWidget(mainwwin_treeviewer)
        self.wid_centralwidget.setObjectName(u"wid_centralwidget")
        self.verticalLayout = QVBoxLayout(self.wid_centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabwid_viewmodes = QTabWidget(self.wid_centralwidget)
        self.tabwid_viewmodes.setObjectName(u"tabwid_viewmodes")
        self.tree = QWidget()
        self.tree.setObjectName(u"tree")
        self.horizontalLayout_2 = QHBoxLayout(self.tree)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wid2 = QWidget(self.tree)
        self.wid2.setObjectName(u"wid2")
        self.verticalLayout_2 = QVBoxLayout(self.wid2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.vspacer)

        self.pb_ancestors = QPushButton(self.wid2)
        self.pb_ancestors.setObjectName(u"pb_ancestors")

        self.verticalLayout_2.addWidget(self.pb_ancestors)

        self.pb_descendants = QPushButton(self.wid2)
        self.pb_descendants.setObjectName(u"pb_descendants")

        self.verticalLayout_2.addWidget(self.pb_descendants)

        self.vspacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.vspacer2)


        self.horizontalLayout_2.addWidget(self.wid2)

        self.treeView = QTreeView(self.tree)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_2.addWidget(self.treeView)

        self.tabwid_viewmodes.addTab(self.tree, "")
        self.index = QWidget()
        self.index.setObjectName(u"index")
        self.tabwid_viewmodes.addTab(self.index, "")

        self.verticalLayout.addWidget(self.tabwid_viewmodes)

        self.wid = QWidget(self.wid_centralwidget)
        self.wid.setObjectName(u"wid")
        self.horizontalLayout = QHBoxLayout(self.wid)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hspacer)

        self.pb_load = QPushButton(self.wid)
        self.pb_load.setObjectName(u"pb_load")

        self.horizontalLayout.addWidget(self.pb_load)


        self.verticalLayout.addWidget(self.wid)

        mainwwin_treeviewer.setCentralWidget(self.wid_centralwidget)
        self.menubar = QMenuBar(mainwwin_treeviewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 36))
        mainwwin_treeviewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainwwin_treeviewer)
        self.statusbar.setObjectName(u"statusbar")
        mainwwin_treeviewer.setStatusBar(self.statusbar)

        self.retranslateUi(mainwwin_treeviewer)

        self.tabwid_viewmodes.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainwwin_treeviewer)
    # setupUi

    def retranslateUi(self, mainwwin_treeviewer):
        mainwwin_treeviewer.setWindowTitle(QCoreApplication.translate("mainwwin_treeviewer", u"Tree Viewer", None))
        self.pb_ancestors.setText(QCoreApplication.translate("mainwwin_treeviewer", u"Ancestors", None))
        self.pb_descendants.setText(QCoreApplication.translate("mainwwin_treeviewer", u"Descendants", None))
        self.tabwid_viewmodes.setTabText(self.tabwid_viewmodes.indexOf(self.tree), QCoreApplication.translate("mainwwin_treeviewer", u"Tree View", None))
        self.tabwid_viewmodes.setTabText(self.tabwid_viewmodes.indexOf(self.index), QCoreApplication.translate("mainwwin_treeviewer", u"Index View", None))
        self.pb_load.setText(QCoreApplication.translate("mainwwin_treeviewer", u"Load Tree...", None))
    # retranslateUi

