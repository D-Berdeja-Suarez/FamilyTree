# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overwritedialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_overwritedialog(object):
    def setupUi(self, overwritedialog):
        if not overwritedialog.objectName():
            overwritedialog.setObjectName(u"overwritedialog")
        overwritedialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        overwritedialog.resize(405, 80)
        self.verticalLayout = QVBoxLayout(overwritedialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(overwritedialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(overwritedialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(overwritedialog)
        self.buttonBox.accepted.connect(overwritedialog.accept)
        self.buttonBox.rejected.connect(overwritedialog.reject)

        QMetaObject.connectSlotsByName(overwritedialog)
    # setupUi

    def retranslateUi(self, overwritedialog):
        overwritedialog.setWindowTitle(QCoreApplication.translate("overwritedialog", u"WARNING", None))
        self.label.setText(QCoreApplication.translate("overwritedialog", u"WARNING GOES HERE", None))
    # retranslateUi

