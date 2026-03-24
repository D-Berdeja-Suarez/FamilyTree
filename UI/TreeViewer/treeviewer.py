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
    QMainWindow, QMenuBar, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_treeviewer(object):
    def setupUi(self, treeviewer):
        if not treeviewer.objectName():
            treeviewer.setObjectName(u"treeviewer")
        treeviewer.resize(801, 511)
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


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.wid_centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_desc = QRadioButton(self.widget_8)
        self.rb_desc.setObjectName(u"rb_desc")
        self.rb_desc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.rb_desc)

        self.rb_asc = QRadioButton(self.widget_8)
        self.rb_asc.setObjectName(u"rb_asc")
        self.rb_asc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.rb_asc)


        self.horizontalLayout.addWidget(self.widget_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rb_collapsed = QRadioButton(self.widget_9)
        self.rb_collapsed.setObjectName(u"rb_collapsed")
        self.rb_collapsed.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.rb_collapsed)

        self.rb_expanded = QRadioButton(self.widget_9)
        self.rb_expanded.setObjectName(u"rb_expanded")
        self.rb_expanded.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_4.addWidget(self.rb_expanded)


        self.horizontalLayout.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget_2)

        self.lab_contextual = QLabel(self.wid_centralwidget)
        self.lab_contextual.setObjectName(u"lab_contextual")

        self.verticalLayout.addWidget(self.lab_contextual)

        treeviewer.setCentralWidget(self.wid_centralwidget)
        self.menubar = QMenuBar(treeviewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 36))
        treeviewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(treeviewer)
        self.statusbar.setObjectName(u"statusbar")
        treeviewer.setStatusBar(self.statusbar)

        self.retranslateUi(treeviewer)

        QMetaObject.connectSlotsByName(treeviewer)
    # setupUi

    def retranslateUi(self, treeviewer):
        treeviewer.setWindowTitle(QCoreApplication.translate("treeviewer", u"Tree Viewer", None))
        self.rb_desc.setText(QCoreApplication.translate("treeviewer", u"Descendance", None))
        self.rb_asc.setText(QCoreApplication.translate("treeviewer", u"Ascendance", None))
        self.rb_collapsed.setText(QCoreApplication.translate("treeviewer", u"Collapse", None))
        self.rb_expanded.setText(QCoreApplication.translate("treeviewer", u"Expand", None))
        self.lab_contextual.setText(QCoreApplication.translate("treeviewer", u"Contextual label", None))
    # retranslateUi

