# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'personinputscreen.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_personinputscreen(object):
    def setupUi(self, personinputscreen):
        if not personinputscreen.objectName():
            personinputscreen.setObjectName(u"personinputscreen")
        personinputscreen.setWindowModality(Qt.WindowModality.ApplicationModal)
        personinputscreen.resize(663, 504)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        personinputscreen.setFont(font)
        self.centralwidget = QWidget(personinputscreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_sex = QWidget(self.centralwidget)
        self.widget_sex.setObjectName(u"widget_sex")
        self.verticalLayout_2 = QVBoxLayout(self.widget_sex)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lab_contextual = QLabel(self.widget_sex)
        self.lab_contextual.setObjectName(u"lab_contextual")
        self.lab_contextual.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.lab_contextual)

        self.widget_radiobuttons = QWidget(self.widget_sex)
        self.widget_radiobuttons.setObjectName(u"widget_radiobuttons")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_radiobuttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.widget_radiobuttons)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.rb_male = QRadioButton(self.widget_3)
        self.rb_male.setObjectName(u"rb_male")

        self.horizontalLayout_4.addWidget(self.rb_male)

        self.rb_female = QRadioButton(self.widget_3)
        self.rb_female.setObjectName(u"rb_female")

        self.horizontalLayout_4.addWidget(self.rb_female)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget_radiobuttons)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.cb_day = QComboBox(self.widget_4)
        self.cb_day.setObjectName(u"cb_day")

        self.horizontalLayout_5.addWidget(self.cb_day)

        self.cb_month = QComboBox(self.widget_4)
        self.cb_month.setObjectName(u"cb_month")

        self.horizontalLayout_5.addWidget(self.cb_month)

        self.sp_year = QSpinBox(self.widget_4)
        self.sp_year.setObjectName(u"sp_year")
        self.sp_year.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sp_year.setMinimum(-10000)
        self.sp_year.setMaximum(3000)
        self.sp_year.setValue(0)

        self.horizontalLayout_5.addWidget(self.sp_year)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.le_pob = QLineEdit(self.widget_7)
        self.le_pob.setObjectName(u"le_pob")
        self.le_pob.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.le_pob)


        self.verticalLayout_3.addWidget(self.widget_7)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_radiobuttons)

        self.widget = QWidget(self.widget_sex)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.le_name = QLineEdit(self.widget)
        self.le_name.setObjectName(u"le_name")

        self.verticalLayout_4.addWidget(self.le_name)

        self.le_first_last = QLineEdit(self.widget)
        self.le_first_last.setObjectName(u"le_first_last")

        self.verticalLayout_4.addWidget(self.le_first_last)

        self.le_second_last = QLineEdit(self.widget)
        self.le_second_last.setObjectName(u"le_second_last")

        self.verticalLayout_4.addWidget(self.le_second_last)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_done = QPushButton(self.widget_2)
        self.pb_done.setObjectName(u"pb_done")

        self.horizontalLayout_3.addWidget(self.pb_done)

        self.pb_clear = QPushButton(self.widget_2)
        self.pb_clear.setObjectName(u"pb_clear")

        self.horizontalLayout_3.addWidget(self.pb_clear)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.widget_sex)

        personinputscreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(personinputscreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 36))
        personinputscreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(personinputscreen)
        self.statusbar.setObjectName(u"statusbar")
        personinputscreen.setStatusBar(self.statusbar)

        self.retranslateUi(personinputscreen)

        QMetaObject.connectSlotsByName(personinputscreen)
    # setupUi

    def retranslateUi(self, personinputscreen):
        personinputscreen.setWindowTitle(QCoreApplication.translate("personinputscreen", u"Input Personal Information", None))
        self.lab_contextual.setText(QCoreApplication.translate("personinputscreen", u"Contextual prompt goes here", None))
        self.label.setText(QCoreApplication.translate("personinputscreen", u"Sex *", None))
        self.rb_male.setText(QCoreApplication.translate("personinputscreen", u"M", None))
        self.rb_female.setText(QCoreApplication.translate("personinputscreen", u"F", None))
        self.label_2.setText(QCoreApplication.translate("personinputscreen", u"Date of Birth *", None))
        self.le_pob.setPlaceholderText(QCoreApplication.translate("personinputscreen", u"Place of Birth", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("personinputscreen", u"First Name *", None))
        self.le_first_last.setPlaceholderText(QCoreApplication.translate("personinputscreen", u"First Surname *", None))
        self.le_second_last.setPlaceholderText(QCoreApplication.translate("personinputscreen", u"Second Surname", None))
        self.pb_done.setText(QCoreApplication.translate("personinputscreen", u"Done", None))
        self.pb_clear.setText(QCoreApplication.translate("personinputscreen", u"Cancel", None))
    # retranslateUi

