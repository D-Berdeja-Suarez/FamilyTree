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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTreeView,
    QVBoxLayout, QWidget)

class Ui_treeviewer(object):
    def setupUi(self, treeviewer):
        if not treeviewer.objectName():
            treeviewer.setObjectName(u"treeviewer")
        treeviewer.resize(811, 535)
        self.wid_centralwidget = QWidget(treeviewer)
        self.wid_centralwidget.setObjectName(u"wid_centralwidget")
        self.verticalLayout = QVBoxLayout(self.wid_centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.wid_centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeView = QTreeView(self.widget)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_3.addWidget(self.treeView)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rb_desc = QRadioButton(self.widget_8)
        self.rb_desc.setObjectName(u"rb_desc")
        self.rb_desc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_4.addWidget(self.rb_desc)

        self.rb_asc = QRadioButton(self.widget_8)
        self.rb_asc.setObjectName(u"rb_asc")
        self.rb_asc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_4.addWidget(self.rb_asc)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pb_collapse_all = QPushButton(self.widget_5)
        self.pb_collapse_all.setObjectName(u"pb_collapse_all")

        self.verticalLayout_3.addWidget(self.pb_collapse_all)

        self.pb_expand_all = QPushButton(self.widget_5)
        self.pb_expand_all.setObjectName(u"pb_expand_all")

        self.verticalLayout_3.addWidget(self.pb_expand_all)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pb_load = QPushButton(self.widget_5)
        self.pb_load.setObjectName(u"pb_load")

        self.verticalLayout_3.addWidget(self.pb_load)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.wid_centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lab_contextual = QLabel(self.widget_2)
        self.lab_contextual.setObjectName(u"lab_contextual")

        self.verticalLayout_2.addWidget(self.lab_contextual)


        self.verticalLayout.addWidget(self.widget_2)

        treeviewer.setCentralWidget(self.wid_centralwidget)
        self.menubar = QMenuBar(treeviewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 36))
        treeviewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(treeviewer)
        self.statusbar.setObjectName(u"statusbar")
        treeviewer.setStatusBar(self.statusbar)

        self.retranslateUi(treeviewer)

        QMetaObject.connectSlotsByName(treeviewer)
    # setupUi

    def retranslateUi(self, treeviewer):
        treeviewer.setWindowTitle(QCoreApplication.translate("treeviewer", u"Tree Viewer", None))
        self.rb_desc.setText(QCoreApplication.translate("treeviewer", u"Ascendance", None))
        self.rb_asc.setText(QCoreApplication.translate("treeviewer", u"Descendance", None))
        self.pb_collapse_all.setText(QCoreApplication.translate("treeviewer", u"Collapse", None))
        self.pb_expand_all.setText(QCoreApplication.translate("treeviewer", u"Expand", None))
        self.pb_load.setText(QCoreApplication.translate("treeviewer", u"Save", None))
        self.lab_contextual.setText(QCoreApplication.translate("treeviewer", u"Contextual label", None))
    # retranslateUi

