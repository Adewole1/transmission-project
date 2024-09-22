# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'belt_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 1283)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1200, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(76, 76, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        brush2 = QBrush(QColor(65, 65, 218, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush2)
        brush3 = QBrush(QColor(76, 76, 255, 10))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush4 = QBrush(QColor(248, 248, 248, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(243, 243, 243, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush5)
        brush6 = QBrush(QColor(70, 70, 236, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        brush7 = QBrush(QColor(227, 227, 227, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        brush8 = QBrush(QColor(68, 68, 68, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        MainWindow.setPalette(palette)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"QPushButton::hover {\n"
"	background-color: rgb(69, 69, 232);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.transmissions = QTabWidget(self.centralwidget)
        self.transmissions.setObjectName(u"transmissions")
        sizePolicy1.setHeightForWidth(self.transmissions.sizePolicy().hasHeightForWidth())
        self.transmissions.setSizePolicy(sizePolicy1)
        self.transmissions.setTabPosition(QTabWidget.TabPosition.North)
        self.transmissions.setElideMode(Qt.TextElideMode.ElideLeft)
        self.transmissions.setTabsClosable(False)
        self.belt = QWidget()
        self.belt.setObjectName(u"belt")
        self.verticalLayout_2 = QVBoxLayout(self.belt)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.belt)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1156, 1162))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Title_2 = QLabel(self.scrollAreaWidgetContents)
        self.Title_2.setObjectName(u"Title_2")
        font = QFont()
        font.setFamilies([u"Merriweather"])
        font.setPointSize(16)
        font.setBold(True)
        self.Title_2.setFont(font)

        self.verticalLayout_3.addWidget(self.Title_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Subtitle_2 = QLabel(self.scrollAreaWidgetContents)
        self.Subtitle_2.setObjectName(u"Subtitle_2")
        font1 = QFont()
        font1.setFamilies([u"Syne"])
        font1.setPointSize(12)
        font1.setKerning(True)
        self.Subtitle_2.setFont(font1)
        self.Subtitle_2.setStyleSheet(u"line-height: 0.25;")
        self.Subtitle_2.setTextFormat(Qt.TextFormat.AutoText)
        self.Subtitle_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.Subtitle_2)

        self.I0 = QWidget(self.scrollAreaWidgetContents)
        self.I0.setObjectName(u"I0")
        sizePolicy1.setHeightForWidth(self.I0.sizePolicy().hasHeightForWidth())
        self.I0.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.I0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Inputs = QGroupBox(self.I0)
        self.Inputs.setObjectName(u"Inputs")
        font2 = QFont()
        font2.setFamilies([u"Merriweather"])
        font2.setPointSize(12)
        font2.setWeight(QFont.Medium)
        self.Inputs.setFont(font2)
        self.Inputs.setFlat(False)
        self.Inputs.setCheckable(False)
        self.horizontalLayout_6 = QHBoxLayout(self.Inputs)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_25 = QWidget(self.Inputs)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_28 = QVBoxLayout(self.widget_25)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_24 = QWidget(self.widget_25)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_8 = QVBoxLayout(self.widget_24)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.widget_24)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Syne"])
        font3.setPointSize(12)
        self.label_4.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_4)

        self.rev1Input = QLineEdit(self.widget_24)
        self.rev1Input.setObjectName(u"rev1Input")
        palette2 = QPalette()
        self.rev1Input.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Merriweather"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.rev1Input.setFont(font4)
        self.rev1Input.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.rev1Input.setFrame(True)
        self.rev1Input.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.rev1Input)


        self.verticalLayout_28.addWidget(self.widget_24)

        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_29 = QVBoxLayout(self.widget_26)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_5 = QLabel(self.widget_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_29.addWidget(self.label_5)

        self.rev2Input = QLineEdit(self.widget_26)
        self.rev2Input.setObjectName(u"rev2Input")
        palette3 = QPalette()
        self.rev2Input.setPalette(palette3)
        self.rev2Input.setFont(font4)
        self.rev2Input.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.rev2Input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.rev2Input.setClearButtonEnabled(True)

        self.verticalLayout_29.addWidget(self.rev2Input)


        self.verticalLayout_28.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_30 = QVBoxLayout(self.widget_27)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_10 = QLabel(self.widget_27)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_30.addWidget(self.label_10)

        self.beltLengthInput = QLineEdit(self.widget_27)
        self.beltLengthInput.setObjectName(u"beltLengthInput")
        palette4 = QPalette()
        self.beltLengthInput.setPalette(palette4)
        self.beltLengthInput.setFont(font4)
        self.beltLengthInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltLengthInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.beltLengthInput.setClearButtonEnabled(True)

        self.verticalLayout_30.addWidget(self.beltLengthInput)


        self.verticalLayout_28.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.verticalLayout_31 = QVBoxLayout(self.widget_28)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_14 = QLabel(self.widget_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_31.addWidget(self.label_14)

        self.powerFactorInput = QLineEdit(self.widget_28)
        self.powerFactorInput.setObjectName(u"powerFactorInput")
        palette5 = QPalette()
        self.powerFactorInput.setPalette(palette5)
        self.powerFactorInput.setFont(font4)
        self.powerFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.powerFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.powerFactorInput.setClearButtonEnabled(True)

        self.verticalLayout_31.addWidget(self.powerFactorInput)


        self.verticalLayout_28.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_25)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_32 = QVBoxLayout(self.widget_29)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_15 = QLabel(self.widget_29)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_32.addWidget(self.label_15)

        self.contactFactorInput = QLineEdit(self.widget_29)
        self.contactFactorInput.setObjectName(u"contactFactorInput")
        palette6 = QPalette()
        self.contactFactorInput.setPalette(palette6)
        self.contactFactorInput.setFont(font4)
        self.contactFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.contactFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.contactFactorInput.setClearButtonEnabled(True)

        self.verticalLayout_32.addWidget(self.contactFactorInput)


        self.verticalLayout_28.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_25)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_33 = QVBoxLayout(self.widget_30)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_8 = QLabel(self.widget_30)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_8)

        self.factorInput = QLineEdit(self.widget_30)
        self.factorInput.setObjectName(u"factorInput")
        palette7 = QPalette()
        self.factorInput.setPalette(palette7)
        self.factorInput.setFont(font4)
        self.factorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.factorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.factorInput.setClearButtonEnabled(True)

        self.verticalLayout_33.addWidget(self.factorInput)


        self.verticalLayout_28.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_25)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_34 = QVBoxLayout(self.widget_31)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_17 = QLabel(self.widget_31)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.verticalLayout_34.addWidget(self.label_17)

        self.beltWeightInput = QLineEdit(self.widget_31)
        self.beltWeightInput.setObjectName(u"beltWeightInput")
        palette8 = QPalette()
        self.beltWeightInput.setPalette(palette8)
        self.beltWeightInput.setFont(font4)
        self.beltWeightInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltWeightInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.beltWeightInput.setClearButtonEnabled(True)

        self.verticalLayout_34.addWidget(self.beltWeightInput)


        self.verticalLayout_28.addWidget(self.widget_31)


        self.horizontalLayout_6.addWidget(self.widget_25)

        self.widget_32 = QWidget(self.Inputs)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_36 = QVBoxLayout(self.widget_32)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_35 = QVBoxLayout(self.widget_33)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_6 = QLabel(self.widget_33)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_35.addWidget(self.label_6)

        self.powerInput = QLineEdit(self.widget_33)
        self.powerInput.setObjectName(u"powerInput")
        palette9 = QPalette()
        self.powerInput.setPalette(palette9)
        self.powerInput.setFont(font4)
        self.powerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.powerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.powerInput.setClearButtonEnabled(True)

        self.verticalLayout_35.addWidget(self.powerInput)


        self.verticalLayout_36.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_32)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_37 = QVBoxLayout(self.widget_34)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_7 = QLabel(self.widget_34)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout_37.addWidget(self.label_7)

        self.centerInput = QLineEdit(self.widget_34)
        self.centerInput.setObjectName(u"centerInput")
        palette10 = QPalette()
        self.centerInput.setPalette(palette10)
        self.centerInput.setFont(font4)
        self.centerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.centerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.centerInput.setClearButtonEnabled(True)

        self.verticalLayout_37.addWidget(self.centerInput)


        self.verticalLayout_36.addWidget(self.widget_34)

        self.widget_36 = QWidget(self.widget_32)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_36)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_38 = QVBoxLayout(self.widget_35)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_9 = QLabel(self.widget_35)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setToolTipDuration(1000)

        self.verticalLayout_38.addWidget(self.label_9)

        self.pitchInput = QLineEdit(self.widget_35)
        self.pitchInput.setObjectName(u"pitchInput")
        palette11 = QPalette()
        self.pitchInput.setPalette(palette11)
        self.pitchInput.setFont(font4)
        self.pitchInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.pitchInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.pitchInput.setClearButtonEnabled(True)

        self.verticalLayout_38.addWidget(self.pitchInput)


        self.horizontalLayout_4.addWidget(self.widget_35)

        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_39 = QVBoxLayout(self.widget_37)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.smallPulleySelect = QRadioButton(self.widget_37)
        self.smallPulleySelect.setObjectName(u"smallPulleySelect")
        palette12 = QPalette()
        self.smallPulleySelect.setPalette(palette12)
        self.smallPulleySelect.setFont(font3)
        self.smallPulleySelect.setToolTipDuration(1000)

        self.verticalLayout_39.addWidget(self.smallPulleySelect)

        self.bigPulleySelect = QRadioButton(self.widget_37)
        self.bigPulleySelect.setObjectName(u"bigPulleySelect")
        palette13 = QPalette()
        self.bigPulleySelect.setPalette(palette13)
        self.bigPulleySelect.setFont(font3)
        self.bigPulleySelect.setToolTipDuration(1000)

        self.verticalLayout_39.addWidget(self.bigPulleySelect)


        self.horizontalLayout_4.addWidget(self.widget_37)


        self.verticalLayout_36.addWidget(self.widget_36)

        self.allowance = QWidget(self.widget_32)
        self.allowance.setObjectName(u"allowance")
        self.horizontalLayout_5 = QHBoxLayout(self.allowance)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.installation = QWidget(self.allowance)
        self.installation.setObjectName(u"installation")
        self.verticalLayout_40 = QVBoxLayout(self.installation)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_13 = QLabel(self.installation)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setToolTipDuration(5)

        self.verticalLayout_40.addWidget(self.label_13)

        self.instAllowanceInput = QLineEdit(self.installation)
        self.instAllowanceInput.setObjectName(u"instAllowanceInput")
        palette14 = QPalette()
        self.instAllowanceInput.setPalette(palette14)
        self.instAllowanceInput.setFont(font4)
        self.instAllowanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.instAllowanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.instAllowanceInput.setClearButtonEnabled(True)

        self.verticalLayout_40.addWidget(self.instAllowanceInput)


        self.horizontalLayout_5.addWidget(self.installation)

        self.takeup = QWidget(self.allowance)
        self.takeup.setObjectName(u"takeup")
        self.verticalLayout_41 = QVBoxLayout(self.takeup)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_16 = QLabel(self.takeup)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setToolTipDuration(5)

        self.verticalLayout_41.addWidget(self.label_16)

        self.takeAllowanceInput = QLineEdit(self.takeup)
        self.takeAllowanceInput.setObjectName(u"takeAllowanceInput")
        palette15 = QPalette()
        self.takeAllowanceInput.setPalette(palette15)
        self.takeAllowanceInput.setFont(font4)
        self.takeAllowanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.takeAllowanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.takeAllowanceInput.setClearButtonEnabled(True)

        self.verticalLayout_41.addWidget(self.takeAllowanceInput)


        self.horizontalLayout_5.addWidget(self.takeup)


        self.verticalLayout_36.addWidget(self.allowance)

        self.rated_power = QWidget(self.widget_32)
        self.rated_power.setObjectName(u"rated_power")
        self.verticalLayout_43 = QVBoxLayout(self.rated_power)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_11 = QLabel(self.rated_power)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.verticalLayout_43.addWidget(self.label_11)

        self.ratedPowerInput = QLineEdit(self.rated_power)
        self.ratedPowerInput.setObjectName(u"ratedPowerInput")
        palette16 = QPalette()
        self.ratedPowerInput.setPalette(palette16)
        self.ratedPowerInput.setFont(font4)
        self.ratedPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.ratedPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.ratedPowerInput.setClearButtonEnabled(True)

        self.verticalLayout_43.addWidget(self.ratedPowerInput)


        self.verticalLayout_36.addWidget(self.rated_power)

        self.addPower = QWidget(self.widget_32)
        self.addPower.setObjectName(u"addPower")
        self.verticalLayout_42 = QVBoxLayout(self.addPower)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_12 = QLabel(self.addPower)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_42.addWidget(self.label_12)

        self.addPowerInput = QLineEdit(self.addPower)
        self.addPowerInput.setObjectName(u"addPowerInput")
        palette17 = QPalette()
        self.addPowerInput.setPalette(palette17)
        self.addPowerInput.setFont(font4)
        self.addPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.addPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.addPowerInput.setClearButtonEnabled(True)

        self.verticalLayout_42.addWidget(self.addPowerInput)


        self.verticalLayout_36.addWidget(self.addPower)

        self.cross_belt = QWidget(self.widget_32)
        self.cross_belt.setObjectName(u"cross_belt")
        self.verticalLayout_44 = QVBoxLayout(self.cross_belt)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_18 = QLabel(self.cross_belt)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setToolTipDuration(5)

        self.verticalLayout_44.addWidget(self.label_18)

        self.crossBelt = QCheckBox(self.cross_belt)
        self.crossBelt.setObjectName(u"crossBelt")
        font5 = QFont()
        font5.setFamilies([u"Syne"])
        font5.setPointSize(12)
        font5.setWeight(QFont.Medium)
        self.crossBelt.setFont(font5)
        self.crossBelt.setToolTipDuration(1000)

        self.verticalLayout_44.addWidget(self.crossBelt)


        self.verticalLayout_36.addWidget(self.cross_belt)


        self.horizontalLayout_6.addWidget(self.widget_32)


        self.horizontalLayout_7.addWidget(self.Inputs)

        self.Outputs = QGroupBox(self.I0)
        self.Outputs.setObjectName(u"Outputs")
        self.Outputs.setFont(font2)
        self.horizontalLayout_3 = QHBoxLayout(self.Outputs)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.widget_13 = QWidget(self.Outputs)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_10 = QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.widget_6 = QWidget(self.widget_13)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_9 = QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_37)

        self.speedRatioOutput = QLineEdit(self.widget_6)
        self.speedRatioOutput.setObjectName(u"speedRatioOutput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(12)
        sizePolicy2.setHeightForWidth(self.speedRatioOutput.sizePolicy().hasHeightForWidth())
        self.speedRatioOutput.setSizePolicy(sizePolicy2)
        palette18 = QPalette()
        self.speedRatioOutput.setPalette(palette18)
        self.speedRatioOutput.setFont(font4)
        self.speedRatioOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.speedRatioOutput.setFrame(True)
        self.speedRatioOutput.setReadOnly(True)
        self.speedRatioOutput.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.speedRatioOutput)


        self.verticalLayout_10.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_13)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_11 = QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_38 = QLabel(self.widget_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_38)

        self.designPowerOutput = QLineEdit(self.widget_7)
        self.designPowerOutput.setObjectName(u"designPowerOutput")
        sizePolicy2.setHeightForWidth(self.designPowerOutput.sizePolicy().hasHeightForWidth())
        self.designPowerOutput.setSizePolicy(sizePolicy2)
        palette19 = QPalette()
        self.designPowerOutput.setPalette(palette19)
        self.designPowerOutput.setFont(font4)
        self.designPowerOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.designPowerOutput.setFrame(True)
        self.designPowerOutput.setReadOnly(True)
        self.designPowerOutput.setClearButtonEnabled(False)

        self.verticalLayout_11.addWidget(self.designPowerOutput)


        self.verticalLayout_10.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_13)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_12 = QVBoxLayout(self.widget_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_42 = QLabel(self.widget_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_42)

        self.pulleyDiameterOutput = QLineEdit(self.widget_8)
        self.pulleyDiameterOutput.setObjectName(u"pulleyDiameterOutput")
        sizePolicy2.setHeightForWidth(self.pulleyDiameterOutput.sizePolicy().hasHeightForWidth())
        self.pulleyDiameterOutput.setSizePolicy(sizePolicy2)
        palette20 = QPalette()
        self.pulleyDiameterOutput.setPalette(palette20)
        self.pulleyDiameterOutput.setFont(font4)
        self.pulleyDiameterOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.pulleyDiameterOutput.setFrame(True)
        self.pulleyDiameterOutput.setReadOnly(True)
        self.pulleyDiameterOutput.setClearButtonEnabled(False)

        self.verticalLayout_12.addWidget(self.pulleyDiameterOutput)


        self.verticalLayout_10.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_13)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_13 = QVBoxLayout(self.widget_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_43 = QLabel(self.widget_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_43)

        self.beltLengthOutput = QLineEdit(self.widget_9)
        self.beltLengthOutput.setObjectName(u"beltLengthOutput")
        sizePolicy2.setHeightForWidth(self.beltLengthOutput.sizePolicy().hasHeightForWidth())
        self.beltLengthOutput.setSizePolicy(sizePolicy2)
        palette21 = QPalette()
        self.beltLengthOutput.setPalette(palette21)
        self.beltLengthOutput.setFont(font4)
        self.beltLengthOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltLengthOutput.setFrame(True)
        self.beltLengthOutput.setReadOnly(True)
        self.beltLengthOutput.setClearButtonEnabled(False)

        self.verticalLayout_13.addWidget(self.beltLengthOutput)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_13)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_14 = QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_44 = QLabel(self.widget_10)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)

        self.verticalLayout_14.addWidget(self.label_44)

        self.powerRatingOutput = QLineEdit(self.widget_10)
        self.powerRatingOutput.setObjectName(u"powerRatingOutput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(12)
        sizePolicy3.setHeightForWidth(self.powerRatingOutput.sizePolicy().hasHeightForWidth())
        self.powerRatingOutput.setSizePolicy(sizePolicy3)
        palette22 = QPalette()
        self.powerRatingOutput.setPalette(palette22)
        self.powerRatingOutput.setFont(font4)
        self.powerRatingOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.powerRatingOutput.setFrame(True)
        self.powerRatingOutput.setReadOnly(True)
        self.powerRatingOutput.setClearButtonEnabled(False)

        self.verticalLayout_14.addWidget(self.powerRatingOutput)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_13)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_15 = QVBoxLayout(self.widget_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_45 = QLabel(self.widget_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)

        self.verticalLayout_15.addWidget(self.label_45)

        self.beltNumberOutput = QLineEdit(self.widget_11)
        self.beltNumberOutput.setObjectName(u"beltNumberOutput")
        sizePolicy2.setHeightForWidth(self.beltNumberOutput.sizePolicy().hasHeightForWidth())
        self.beltNumberOutput.setSizePolicy(sizePolicy2)
        palette23 = QPalette()
        self.beltNumberOutput.setPalette(palette23)
        self.beltNumberOutput.setFont(font4)
        self.beltNumberOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltNumberOutput.setFrame(True)
        self.beltNumberOutput.setReadOnly(True)
        self.beltNumberOutput.setClearButtonEnabled(False)

        self.verticalLayout_15.addWidget(self.beltNumberOutput)


        self.verticalLayout_10.addWidget(self.widget_11)

        self.widget_22 = QWidget(self.widget_13)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_26 = QVBoxLayout(self.widget_22)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_53 = QLabel(self.widget_22)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)

        self.verticalLayout_26.addWidget(self.label_53)

        self.beltSpeedOutput = QLineEdit(self.widget_22)
        self.beltSpeedOutput.setObjectName(u"beltSpeedOutput")
        sizePolicy2.setHeightForWidth(self.beltSpeedOutput.sizePolicy().hasHeightForWidth())
        self.beltSpeedOutput.setSizePolicy(sizePolicy2)
        palette24 = QPalette()
        self.beltSpeedOutput.setPalette(palette24)
        self.beltSpeedOutput.setFont(font4)
        self.beltSpeedOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltSpeedOutput.setFrame(True)
        self.beltSpeedOutput.setReadOnly(True)
        self.beltSpeedOutput.setClearButtonEnabled(False)

        self.verticalLayout_26.addWidget(self.beltSpeedOutput)


        self.verticalLayout_10.addWidget(self.widget_22)

        self.widget_12 = QWidget(self.widget_13)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_16 = QVBoxLayout(self.widget_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_46 = QLabel(self.widget_12)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_46)

        self.exactCenterOutput = QLineEdit(self.widget_12)
        self.exactCenterOutput.setObjectName(u"exactCenterOutput")
        sizePolicy2.setHeightForWidth(self.exactCenterOutput.sizePolicy().hasHeightForWidth())
        self.exactCenterOutput.setSizePolicy(sizePolicy2)
        palette25 = QPalette()
        self.exactCenterOutput.setPalette(palette25)
        self.exactCenterOutput.setFont(font4)
        self.exactCenterOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.exactCenterOutput.setFrame(True)
        self.exactCenterOutput.setReadOnly(True)
        self.exactCenterOutput.setClearButtonEnabled(False)

        self.verticalLayout_16.addWidget(self.exactCenterOutput)


        self.verticalLayout_10.addWidget(self.widget_12)

        self.widget_38 = QWidget(self.widget_13)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_48 = QVBoxLayout(self.widget_38)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_59 = QLabel(self.widget_38)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)

        self.verticalLayout_48.addWidget(self.label_59)

        self.effectiveTensionOutput = QLineEdit(self.widget_38)
        self.effectiveTensionOutput.setObjectName(u"effectiveTensionOutput")
        sizePolicy2.setHeightForWidth(self.effectiveTensionOutput.sizePolicy().hasHeightForWidth())
        self.effectiveTensionOutput.setSizePolicy(sizePolicy2)
        palette26 = QPalette()
        self.effectiveTensionOutput.setPalette(palette26)
        self.effectiveTensionOutput.setFont(font4)
        self.effectiveTensionOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.effectiveTensionOutput.setFrame(True)
        self.effectiveTensionOutput.setReadOnly(True)
        self.effectiveTensionOutput.setClearButtonEnabled(False)

        self.verticalLayout_48.addWidget(self.effectiveTensionOutput)


        self.verticalLayout_10.addWidget(self.widget_38)


        self.horizontalLayout_3.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.Outputs)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_17 = QVBoxLayout(self.widget_14)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_18 = QVBoxLayout(self.widget_15)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_39 = QLabel(self.widget_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)

        self.verticalLayout_18.addWidget(self.label_39)

        self.torqueOutput = QLineEdit(self.widget_15)
        self.torqueOutput.setObjectName(u"torqueOutput")
        sizePolicy2.setHeightForWidth(self.torqueOutput.sizePolicy().hasHeightForWidth())
        self.torqueOutput.setSizePolicy(sizePolicy2)
        palette27 = QPalette()
        self.torqueOutput.setPalette(palette27)
        self.torqueOutput.setFont(font4)
        self.torqueOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.torqueOutput.setFrame(True)
        self.torqueOutput.setReadOnly(True)
        self.torqueOutput.setClearButtonEnabled(False)

        self.verticalLayout_18.addWidget(self.torqueOutput)


        self.verticalLayout_17.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_19 = QVBoxLayout(self.widget_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_40 = QLabel(self.widget_16)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_40)

        self.tightOutput = QLineEdit(self.widget_16)
        self.tightOutput.setObjectName(u"tightOutput")
        sizePolicy2.setHeightForWidth(self.tightOutput.sizePolicy().hasHeightForWidth())
        self.tightOutput.setSizePolicy(sizePolicy2)
        palette28 = QPalette()
        self.tightOutput.setPalette(palette28)
        self.tightOutput.setFont(font4)
        self.tightOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.tightOutput.setFrame(True)
        self.tightOutput.setReadOnly(True)
        self.tightOutput.setClearButtonEnabled(False)

        self.verticalLayout_19.addWidget(self.tightOutput)


        self.verticalLayout_17.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_14)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_20 = QVBoxLayout(self.widget_17)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_41 = QLabel(self.widget_17)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_41)

        self.slackOutput = QLineEdit(self.widget_17)
        self.slackOutput.setObjectName(u"slackOutput")
        sizePolicy2.setHeightForWidth(self.slackOutput.sizePolicy().hasHeightForWidth())
        self.slackOutput.setSizePolicy(sizePolicy2)
        palette29 = QPalette()
        self.slackOutput.setPalette(palette29)
        self.slackOutput.setFont(font4)
        self.slackOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.slackOutput.setFrame(True)
        self.slackOutput.setReadOnly(True)
        self.slackOutput.setClearButtonEnabled(False)

        self.verticalLayout_20.addWidget(self.slackOutput)


        self.verticalLayout_17.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_14)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_21 = QVBoxLayout(self.widget_18)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_48 = QLabel(self.widget_18)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_48)

        self.tensionRatioOutput = QLineEdit(self.widget_18)
        self.tensionRatioOutput.setObjectName(u"tensionRatioOutput")
        sizePolicy2.setHeightForWidth(self.tensionRatioOutput.sizePolicy().hasHeightForWidth())
        self.tensionRatioOutput.setSizePolicy(sizePolicy2)
        palette30 = QPalette()
        self.tensionRatioOutput.setPalette(palette30)
        self.tensionRatioOutput.setFont(font4)
        self.tensionRatioOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.tensionRatioOutput.setFrame(True)
        self.tensionRatioOutput.setReadOnly(True)
        self.tensionRatioOutput.setClearButtonEnabled(False)

        self.verticalLayout_21.addWidget(self.tensionRatioOutput)


        self.verticalLayout_17.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_22 = QVBoxLayout(self.widget_19)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_49 = QLabel(self.widget_19)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font3)

        self.verticalLayout_22.addWidget(self.label_49)

        self.staticTensionOutput = QLineEdit(self.widget_19)
        self.staticTensionOutput.setObjectName(u"staticTensionOutput")
        sizePolicy2.setHeightForWidth(self.staticTensionOutput.sizePolicy().hasHeightForWidth())
        self.staticTensionOutput.setSizePolicy(sizePolicy2)
        palette31 = QPalette()
        self.staticTensionOutput.setPalette(palette31)
        self.staticTensionOutput.setFont(font4)
        self.staticTensionOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.staticTensionOutput.setFrame(True)
        self.staticTensionOutput.setReadOnly(True)
        self.staticTensionOutput.setClearButtonEnabled(False)

        self.verticalLayout_22.addWidget(self.staticTensionOutput)


        self.verticalLayout_17.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_14)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_23 = QVBoxLayout(self.widget_20)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_50 = QLabel(self.widget_20)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_50)

        self.contactAngleOutput = QLineEdit(self.widget_20)
        self.contactAngleOutput.setObjectName(u"contactAngleOutput")
        sizePolicy2.setHeightForWidth(self.contactAngleOutput.sizePolicy().hasHeightForWidth())
        self.contactAngleOutput.setSizePolicy(sizePolicy2)
        palette32 = QPalette()
        self.contactAngleOutput.setPalette(palette32)
        self.contactAngleOutput.setFont(font4)
        self.contactAngleOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.contactAngleOutput.setFrame(True)
        self.contactAngleOutput.setReadOnly(True)
        self.contactAngleOutput.setClearButtonEnabled(False)

        self.verticalLayout_23.addWidget(self.contactAngleOutput)


        self.verticalLayout_17.addWidget(self.widget_20)

        self.widget_23 = QWidget(self.widget_14)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_27 = QVBoxLayout(self.widget_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_54 = QLabel(self.widget_23)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.verticalLayout_27.addWidget(self.label_54)

        self.shaftLoadOutput = QLineEdit(self.widget_23)
        self.shaftLoadOutput.setObjectName(u"shaftLoadOutput")
        sizePolicy2.setHeightForWidth(self.shaftLoadOutput.sizePolicy().hasHeightForWidth())
        self.shaftLoadOutput.setSizePolicy(sizePolicy2)
        palette33 = QPalette()
        self.shaftLoadOutput.setPalette(palette33)
        self.shaftLoadOutput.setFont(font4)
        self.shaftLoadOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.shaftLoadOutput.setFrame(True)
        self.shaftLoadOutput.setReadOnly(True)
        self.shaftLoadOutput.setClearButtonEnabled(False)

        self.verticalLayout_27.addWidget(self.shaftLoadOutput)


        self.verticalLayout_17.addWidget(self.widget_23)

        self.widget_21 = QWidget(self.widget_14)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_24 = QVBoxLayout(self.widget_21)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_51 = QLabel(self.widget_21)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font3)

        self.verticalLayout_24.addWidget(self.label_51)

        self.wrapAngleOutput = QLineEdit(self.widget_21)
        self.wrapAngleOutput.setObjectName(u"wrapAngleOutput")
        sizePolicy2.setHeightForWidth(self.wrapAngleOutput.sizePolicy().hasHeightForWidth())
        self.wrapAngleOutput.setSizePolicy(sizePolicy2)
        palette34 = QPalette()
        self.wrapAngleOutput.setPalette(palette34)
        self.wrapAngleOutput.setFont(font4)
        self.wrapAngleOutput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.wrapAngleOutput.setFrame(True)
        self.wrapAngleOutput.setReadOnly(True)
        self.wrapAngleOutput.setClearButtonEnabled(False)

        self.verticalLayout_24.addWidget(self.wrapAngleOutput)


        self.verticalLayout_17.addWidget(self.widget_21)

        self.widget_39 = QWidget(self.widget_14)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_49 = QVBoxLayout(self.widget_39)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_60 = QLabel(self.widget_39)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)

        self.verticalLayout_49.addWidget(self.label_60)

        self.wrapAngleOutput_2 = QLineEdit(self.widget_39)
        self.wrapAngleOutput_2.setObjectName(u"wrapAngleOutput_2")
        sizePolicy2.setHeightForWidth(self.wrapAngleOutput_2.sizePolicy().hasHeightForWidth())
        self.wrapAngleOutput_2.setSizePolicy(sizePolicy2)
        palette35 = QPalette()
        self.wrapAngleOutput_2.setPalette(palette35)
        self.wrapAngleOutput_2.setFont(font4)
        self.wrapAngleOutput_2.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.wrapAngleOutput_2.setFrame(True)
        self.wrapAngleOutput_2.setReadOnly(True)
        self.wrapAngleOutput_2.setClearButtonEnabled(False)

        self.verticalLayout_49.addWidget(self.wrapAngleOutput_2)


        self.verticalLayout_17.addWidget(self.widget_39)


        self.horizontalLayout_3.addWidget(self.widget_14)


        self.horizontalLayout_7.addWidget(self.Outputs)


        self.verticalLayout_3.addWidget(self.I0)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resultText = QTextEdit(self.widget)
        self.resultText.setObjectName(u"resultText")
        palette36 = QPalette()
        self.resultText.setPalette(palette36)
        font6 = QFont()
        font6.setFamilies([u"Merriweather"])
        font6.setPointSize(12)
        self.resultText.setFont(font6)
        self.resultText.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.resultText.setStyleSheet(u".eq-c {\n"
"  text-align: center;\n"
"  padding: 0em 0em;\n"
"  font-size: 2rem;\n"
"}\n"
"\n"
".eq-c .radical {\n"
"  font-size: 3.6rem;\n"
"  vertical-align: middle;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  right: -0.8rem;\n"
"}\n"
"\n"
".eq-c .radicand {\n"
"  top: 0.4rem;\n"
"  padding: 0 0.5rem;\n"
"  border-top: 0.2rem black solid;\n"
"}\n"
"\n"
".eq-c sup {\n"
"  font-size: 75%;\n"
"}\n"
"\n"
".fraction {\n"
"  display: inline-block;\n"
"  vertical-align: middle;\n"
"  margin: 0 0.2em 0.4ex;\n"
"  text-align: center;\n"
"}\n"
"\n"
".fraction > span {\n"
"  display: block;\n"
"  padding-top: 0.15em;\n"
"}\n"
"\n"
".fraction span.fdn {\n"
"  border-top: thin solid black;\n"
"}\n"
"\n"
".fraction span.bar {\n"
"  display: none;\n"
"}\n"
"\n"
".sy {\n"
"  position: relative;\n"
"  text-align: center;\n"
"}\n"
"\n"
".oncapital, .onsmall {\n"
"  position: absolute;\n"
"  top: -0.8em;\n"
"  left: 0px;\n"
"  width: 100%;\n"
"  font-size: 70%;\n"
"  text-align: center;\n"
"}\n"
"\n"
".onsmall {\n"
"  top: -0.5em"
                        ";\n"
"}\n"
"\n"
"")
        self.resultText.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.resultText.setReadOnly(True)
        self.resultText.setAcceptRichText(True)
        self.resultText.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.resultText)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nextButton = QPushButton(self.widget_2)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setEnabled(True)
        font7 = QFont()
        font7.setFamilies([u"Syne"])
        font7.setPointSize(12)
        font7.setWeight(QFont.DemiBold)
        self.nextButton.setFont(font7)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;\n"
"")
        self.nextButton.setAutoDefault(False)
        self.nextButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.nextButton)

        self.clearInputButton = QPushButton(self.widget_2)
        self.clearInputButton.setObjectName(u"clearInputButton")
        self.clearInputButton.setFont(font7)
        self.clearInputButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearInputButton.setAutoFillBackground(False)
        self.clearInputButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;\n"
"")

        self.verticalLayout_4.addWidget(self.clearInputButton)

        self.clearResultButton = QPushButton(self.widget_2)
        self.clearResultButton.setObjectName(u"clearResultButton")
        self.clearResultButton.setFont(font7)
        self.clearResultButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearResultButton.setAutoFillBackground(False)
        self.clearResultButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;\n"
"")

        self.verticalLayout_4.addWidget(self.clearResultButton)

        self.clearAllButton = QPushButton(self.widget_2)
        self.clearAllButton.setObjectName(u"clearAllButton")
        self.clearAllButton.setFont(font7)
        self.clearAllButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clearAllButton.setAutoFillBackground(False)
        self.clearAllButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;\n"
"")

        self.verticalLayout_4.addWidget(self.clearAllButton)

        self.calculateButton = QPushButton(self.widget_2)
        self.calculateButton.setObjectName(u"calculateButton")
        self.calculateButton.setFont(font7)
        self.calculateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calculateButton.setAutoFillBackground(False)
        self.calculateButton.setStyleSheet(u"border: 2px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(76, 76, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"padding: 6px 12px 6px 12px;")

        self.verticalLayout_4.addWidget(self.calculateButton)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.transmissions.addTab(self.belt, "")
        self.chain = QWidget()
        self.chain.setObjectName(u"chain")
        self.verticalLayout = QVBoxLayout(self.chain)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_2 = QScrollArea(self.chain)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1156, 1162))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.chainTitle = QLabel(self.scrollAreaWidgetContents_2)
        self.chainTitle.setObjectName(u"chainTitle")
        self.chainTitle.setFont(font)
        self.chainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.chainTitle)

        self.chainSubtitle = QLabel(self.scrollAreaWidgetContents_2)
        self.chainSubtitle.setObjectName(u"chainSubtitle")
        self.chainSubtitle.setFont(font1)
        self.chainSubtitle.setStyleSheet(u"line-height: 0.25;")
        self.chainSubtitle.setLineWidth(1)
        self.chainSubtitle.setTextFormat(Qt.TextFormat.AutoText)
        self.chainSubtitle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.chainSubtitle)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.smallSprocketSelect = QRadioButton(self.groupBox_2)
        self.smallSprocketSelect.setObjectName(u"smallSprocketSelect")
        palette37 = QPalette()
        self.smallSprocketSelect.setPalette(palette37)
        self.smallSprocketSelect.setFont(font3)
        self.smallSprocketSelect.setToolTipDuration(1000)

        self.gridLayout_2.addWidget(self.smallSprocketSelect, 15, 2, 1, 1)

        self.massInput = QLineEdit(self.groupBox_2)
        self.massInput.setObjectName(u"massInput")
        palette38 = QPalette()
        self.massInput.setPalette(palette38)
        self.massInput.setFont(font4)
        self.massInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.massInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.massInput.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.massInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.massInput, 5, 2, 1, 2)

        self.label_56 = QLabel(self.groupBox_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)

        self.gridLayout_2.addWidget(self.label_56, 17, 0, 1, 1)

        self.label_36 = QLabel(self.groupBox_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.gridLayout_2.addWidget(self.label_36, 17, 2, 1, 1)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.gridLayout_2.addWidget(self.label_25, 4, 0, 1, 1)

        self.bearingAreaInput = QLineEdit(self.groupBox_2)
        self.bearingAreaInput.setObjectName(u"bearingAreaInput")
        palette39 = QPalette()
        self.bearingAreaInput.setPalette(palette39)
        self.bearingAreaInput.setFont(font4)
        self.bearingAreaInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.bearingAreaInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.bearingAreaInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.bearingAreaInput, 7, 0, 1, 1)

        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)
        self.label_35.setToolTipDuration(5)

        self.gridLayout_2.addWidget(self.label_35, 13, 1, 1, 1)

        self.overallJointInput = QLineEdit(self.groupBox_2)
        self.overallJointInput.setObjectName(u"overallJointInput")
        palette40 = QPalette()
        self.overallJointInput.setPalette(palette40)
        self.overallJointInput.setFont(font4)
        self.overallJointInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.overallJointInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.overallJointInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.overallJointInput, 3, 2, 1, 2)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout_2.addWidget(self.label_28, 6, 1, 1, 1)

        self.label_55 = QLabel(self.groupBox_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)
        self.label_55.setToolTipDuration(5)

        self.gridLayout_2.addWidget(self.label_55, 17, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.gridLayout_2.addWidget(self.label_26, 4, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setToolTipDuration(5)

        self.gridLayout_2.addWidget(self.label_31, 8, 1, 2, 1)

        self.chainRev1Input = QLineEdit(self.groupBox_2)
        self.chainRev1Input.setObjectName(u"chainRev1Input")
        palette41 = QPalette()
        self.chainRev1Input.setPalette(palette41)
        self.chainRev1Input.setFont(font4)
        self.chainRev1Input.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.chainRev1Input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.chainRev1Input.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.chainRev1Input, 18, 2, 1, 1)

        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.gridLayout_2.addWidget(self.label_33, 8, 0, 2, 1)

        self.betweenWidthInput = QLineEdit(self.groupBox_2)
        self.betweenWidthInput.setObjectName(u"betweenWidthInput")
        palette42 = QPalette()
        self.betweenWidthInput.setPalette(palette42)
        self.betweenWidthInput.setFont(font4)
        self.betweenWidthInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.betweenWidthInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.betweenWidthInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.betweenWidthInput, 1, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.gridLayout_2.addWidget(self.label_34, 13, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.gridLayout_2.addWidget(self.label_23, 0, 1, 1, 1)

        self.constantInput = QLineEdit(self.groupBox_2)
        self.constantInput.setObjectName(u"constantInput")
        palette43 = QPalette()
        self.constantInput.setPalette(palette43)
        self.constantInput.setFont(font4)
        self.constantInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.constantInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.constantInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.constantInput, 18, 0, 1, 1)

        self.transmissionRatioInput = QLineEdit(self.groupBox_2)
        self.transmissionRatioInput.setObjectName(u"transmissionRatioInput")
        palette44 = QPalette()
        self.transmissionRatioInput.setPalette(palette44)
        self.transmissionRatioInput.setFont(font4)
        self.transmissionRatioInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.transmissionRatioInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.transmissionRatioInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.transmissionRatioInput, 7, 2, 1, 2)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setToolTipDuration(1000)

        self.gridLayout_2.addWidget(self.label_19, 2, 2, 1, 2)

        self.initialSagInput = QLineEdit(self.groupBox_2)
        self.initialSagInput.setObjectName(u"initialSagInput")
        palette45 = QPalette()
        self.initialSagInput.setPalette(palette45)
        self.initialSagInput.setFont(font4)
        self.initialSagInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.initialSagInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.initialSagInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.initialSagInput, 15, 1, 1, 1)

        self.rollerDiameterInput = QLineEdit(self.groupBox_2)
        self.rollerDiameterInput.setObjectName(u"rollerDiameterInput")
        palette46 = QPalette()
        self.rollerDiameterInput.setPalette(palette46)
        self.rollerDiameterInput.setFont(font4)
        self.rollerDiameterInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.rollerDiameterInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.rollerDiameterInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.rollerDiameterInput, 1, 2, 1, 2)

        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setToolTipDuration(5)

        self.gridLayout_2.addWidget(self.label_30, 6, 2, 1, 2)

        self.breakingLoadInput = QLineEdit(self.groupBox_2)
        self.breakingLoadInput.setObjectName(u"breakingLoadInput")
        palette47 = QPalette()
        self.breakingLoadInput.setPalette(palette47)
        self.breakingLoadInput.setFont(font4)
        self.breakingLoadInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.breakingLoadInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.breakingLoadInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.breakingLoadInput, 7, 1, 1, 1)

        self.centerDistanceInput = QLineEdit(self.groupBox_2)
        self.centerDistanceInput.setObjectName(u"centerDistanceInput")
        palette48 = QPalette()
        self.centerDistanceInput.setPalette(palette48)
        self.centerDistanceInput.setFont(font4)
        self.centerDistanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.centerDistanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.centerDistanceInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.centerDistanceInput, 15, 0, 1, 1)

        self.plateDiameterInput = QLineEdit(self.groupBox_2)
        self.plateDiameterInput.setObjectName(u"plateDiameterInput")
        palette49 = QPalette()
        self.plateDiameterInput.setPalette(palette49)
        self.plateDiameterInput.setFont(font4)
        self.plateDiameterInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.plateDiameterInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.plateDiameterInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.plateDiameterInput, 3, 0, 1, 1)

        self.pinDiameterInput = QLineEdit(self.groupBox_2)
        self.pinDiameterInput.setObjectName(u"pinDiameterInput")
        palette50 = QPalette()
        self.pinDiameterInput.setPalette(palette50)
        self.pinDiameterInput.setFont(font4)
        self.pinDiameterInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.pinDiameterInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.pinDiameterInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.pinDiameterInput, 5, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.gridLayout_2.addWidget(self.label_32, 8, 2, 2, 2)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.tranversePitchInput = QLineEdit(self.groupBox_2)
        self.tranversePitchInput.setObjectName(u"tranversePitchInput")
        palette51 = QPalette()
        self.tranversePitchInput.setPalette(palette51)
        self.tranversePitchInput.setFont(font4)
        self.tranversePitchInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.tranversePitchInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.tranversePitchInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.tranversePitchInput, 5, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.gridLayout_2.addWidget(self.label_24, 0, 2, 1, 2)

        self.bigSprocketSelect = QRadioButton(self.groupBox_2)
        self.bigSprocketSelect.setObjectName(u"bigSprocketSelect")
        palette52 = QPalette()
        self.bigSprocketSelect.setPalette(palette52)
        self.bigSprocketSelect.setFont(font3)
        self.bigSprocketSelect.setToolTipDuration(1000)

        self.gridLayout_2.addWidget(self.bigSprocketSelect, 13, 2, 1, 1)

        self.chainPitchInput = QLineEdit(self.groupBox_2)
        self.chainPitchInput.setObjectName(u"chainPitchInput")
        palette53 = QPalette()
        self.chainPitchInput.setPalette(palette53)
        self.chainPitchInput.setFont(font4)
        self.chainPitchInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.chainPitchInput.setFrame(True)
        self.chainPitchInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.chainPitchInput, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.gridLayout_2.addWidget(self.label_22, 2, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_2.addWidget(self.label_27, 4, 2, 1, 2)

        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout_2.addWidget(self.label_29, 6, 0, 1, 1)

        self.innerWidthInput = QLineEdit(self.groupBox_2)
        self.innerWidthInput.setObjectName(u"innerWidthInput")
        palette54 = QPalette()
        self.innerWidthInput.setPalette(palette54)
        self.innerWidthInput.setFont(font4)
        self.innerWidthInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.innerWidthInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.innerWidthInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.innerWidthInput, 3, 1, 1, 1)

        self.loadFactorInput = QLineEdit(self.groupBox_2)
        self.loadFactorInput.setObjectName(u"loadFactorInput")
        palette55 = QPalette()
        self.loadFactorInput.setPalette(palette55)
        self.loadFactorInput.setFont(font4)
        self.loadFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.loadFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.loadFactorInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.loadFactorInput, 18, 1, 1, 1)

        self.chainRatedPowerInput = QLineEdit(self.groupBox_2)
        self.chainRatedPowerInput.setObjectName(u"chainRatedPowerInput")
        palette56 = QPalette()
        self.chainRatedPowerInput.setPalette(palette56)
        self.chainRatedPowerInput.setFont(font4)
        self.chainRatedPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.chainRatedPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.chainRatedPowerInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.chainRatedPowerInput, 10, 0, 1, 1)

        self.serviceFactorInput = QLineEdit(self.groupBox_2)
        self.serviceFactorInput.setObjectName(u"serviceFactorInput")
        palette57 = QPalette()
        self.serviceFactorInput.setPalette(palette57)
        self.serviceFactorInput.setFont(font4)
        self.serviceFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.serviceFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.serviceFactorInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.serviceFactorInput, 10, 1, 1, 1)

        self.teethInput = QLineEdit(self.groupBox_2)
        self.teethInput.setObjectName(u"teethInput")
        palette58 = QPalette()
        self.teethInput.setPalette(palette58)
        self.teethInput.setFont(font4)
        self.teethInput.setToolTipDuration(1000)
        self.teethInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.teethInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.teethInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.teethInput, 10, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chainResults = QTextEdit(self.widget_3)
        self.chainResults.setObjectName(u"chainResults")
        palette59 = QPalette()
        self.chainResults.setPalette(palette59)
        self.chainResults.setFont(font6)
        self.chainResults.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.chainResults.setStyleSheet(u".eq-c {\n"
"  text-align: center;\n"
"  padding: 0em 0em;\n"
"  font-size: 2rem;\n"
"}\n"
"\n"
".eq-c .radical {\n"
"  font-size: 3.6rem;\n"
"  vertical-align: middle;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  right: -0.8rem;\n"
"}\n"
"\n"
".eq-c .radicand {\n"
"  top: 0.4rem;\n"
"  padding: 0 0.5rem;\n"
"  border-top: 0.2rem black solid;\n"
"}\n"
"\n"
".eq-c sup {\n"
"  font-size: 75%;\n"
"}\n"
"\n"
".fraction {\n"
"  display: inline-block;\n"
"  vertical-align: middle;\n"
"  margin: 0 0.2em 0.4ex;\n"
"  text-align: center;\n"
"}\n"
"\n"
".fraction > span {\n"
"  display: block;\n"
"  padding-top: 0.15em;\n"
"}\n"
"\n"
".fraction span.fdn {\n"
"  border-top: thin solid black;\n"
"}\n"
"\n"
".fraction span.bar {\n"
"  display: none;\n"
"}\n"
"\n"
".sy {\n"
"  position: relative;\n"
"  text-align: center;\n"
"}\n"
"\n"
".oncapital, .onsmall {\n"
"  position: absolute;\n"
"  top: -0.8em;\n"
"  left: 0px;\n"
"  width: 100%;\n"
"  font-size: 70%;\n"
"  text-align: center;\n"
"}\n"
"\n"
".onsmall {\n"
"  top: -0.5em"
                        ";\n"
"}")
        self.chainResults.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.chainResults.setReadOnly(True)
        self.chainResults.setAcceptRichText(True)
        self.chainResults.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.chainResults)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.prevButton = QPushButton(self.widget_4)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setEnabled(True)
        self.prevButton.setFont(font7)
        self.prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.prevButton.setAutoFillBackground(False)
        self.prevButton.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;")
        self.prevButton.setAutoDefault(False)
        self.prevButton.setFlat(False)

        self.verticalLayout_6.addWidget(self.prevButton)

        self.chainClearInputsBtn = QPushButton(self.widget_4)
        self.chainClearInputsBtn.setObjectName(u"chainClearInputsBtn")
        self.chainClearInputsBtn.setFont(font7)
        self.chainClearInputsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chainClearInputsBtn.setAutoFillBackground(False)
        self.chainClearInputsBtn.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;")

        self.verticalLayout_6.addWidget(self.chainClearInputsBtn)

        self.chainClearResultsBtn = QPushButton(self.widget_4)
        self.chainClearResultsBtn.setObjectName(u"chainClearResultsBtn")
        self.chainClearResultsBtn.setFont(font7)
        self.chainClearResultsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chainClearResultsBtn.setAutoFillBackground(False)
        self.chainClearResultsBtn.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;")

        self.verticalLayout_6.addWidget(self.chainClearResultsBtn)

        self.chainClearAll = QPushButton(self.widget_4)
        self.chainClearAll.setObjectName(u"chainClearAll")
        self.chainClearAll.setFont(font7)
        self.chainClearAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chainClearAll.setAutoFillBackground(False)
        self.chainClearAll.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 255);\n"
"border-color: rgb(76, 76, 255);\n"
"padding: 6px 12px 6px 12px;")

        self.verticalLayout_6.addWidget(self.chainClearAll)

        self.chainCalculateButton = QPushButton(self.widget_4)
        self.chainCalculateButton.setObjectName(u"chainCalculateButton")
        self.chainCalculateButton.setFont(font7)
        self.chainCalculateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.chainCalculateButton.setAutoFillBackground(False)
        self.chainCalculateButton.setStyleSheet(u"border: 2px solid;\n"
"border-radius: 6px;\n"
"background-color: rgb(76, 76, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"padding: 6px 12px 6px 12px;")

        self.verticalLayout_6.addWidget(self.chainCalculateButton)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.transmissions.addTab(self.chain, "")

        self.verticalLayout_5.addWidget(self.transmissions)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.transmissions.setCurrentIndex(0)
        self.nextButton.setDefault(False)
        self.prevButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Belt Screen", None))
        self.Title_2.setText(QCoreApplication.translate("MainWindow", u"Belt Drive Calculator", None))
        self.Subtitle_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Syne'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;line-height:30%;\">Belt drives use a flexible belt and pulleys. The belt runs over the pulleys, transmitting</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;line-height:30%;\">power through friction. Belt drives are quieter and require less</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;line-height:30%;\">maintenance compared to chain drives.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Inputs.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No of rev. on drive shaft (<var>N<sub>1</sub></var>)", None))
        self.rev1Input.setText("")
        self.rev1Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter drive shaft revolutions in rpm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"No of rev. on centrifugal pump (<var>N<sub>2</sub></var>)", None))
        self.rev2Input.setText("")
        self.rev2Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pump revolutions in rpm", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Standard Belt Length (<var>L</var>)", None))
        self.beltLengthInput.setText("")
        self.beltLengthInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter belt length from table in mm", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Power Correctional Factor (<var>F<sub>L</sub></var>)", None))
        self.powerFactorInput.setText("")
        self.powerFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter power correctional factor", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Arc of Contact Correctional Factor (<var>F<sub>A</sub></var>)", None))
        self.contactFactorInput.setText("")
        self.contactFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter arc of contact correctional factor", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Service Factor (<var>K</var>)", None))
        self.factorInput.setText("")
        self.factorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter service factor", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Belt Weight (W)", None))
        self.beltWeightInput.setText("")
        self.beltWeightInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter belt weight", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Power on drive shaft (<var>P</var>)", None))
        self.powerInput.setText("")
        self.powerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter power on drive shaft in kW", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Approx. Center distance (<var>C</var>)", None))
        self.centerInput.setText("")
        self.centerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter distance between pulleys in mm", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pitch Diameter", None))
        self.pitchInput.setText("")
        self.pitchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pulley pitch", None))
#if QT_CONFIG(tooltip)
        self.smallPulleySelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter pitch diameter in field to the left", None))
#endif // QT_CONFIG(tooltip)
        self.smallPulleySelect.setText(QCoreApplication.translate("MainWindow", u"Small pulley (d)", None))
#if QT_CONFIG(tooltip)
        self.bigPulleySelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter pitch diameter in field to the left", None))
#endif // QT_CONFIG(tooltip)
        self.bigPulleySelect.setText(QCoreApplication.translate("MainWindow", u"Big pulley (D)", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Installation allowance", None))
        self.instAllowanceInput.setText("")
        self.instAllowanceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter allowance in mm", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Takeup allowance", None))
        self.takeAllowanceInput.setText("")
        self.takeAllowanceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter allowance in mm", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rated Power", None))
        self.ratedPowerInput.setText("")
        self.ratedPowerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter rated power in kW", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Additional Power", None))
        self.addPowerInput.setText("")
        self.addPowerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter additional power for speed ratio in kW", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_18.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"*Check if belt is crossed", None))
#if QT_CONFIG(tooltip)
        self.crossBelt.setToolTip(QCoreApplication.translate("MainWindow", u"Check this box if belt is cross type", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.crossBelt.setWhatsThis(QCoreApplication.translate("MainWindow", u"Check this box if belt is cross type", None))
#endif // QT_CONFIG(whatsthis)
        self.crossBelt.setText(QCoreApplication.translate("MainWindow", u"Cross Belt", None))
        self.Outputs.setTitle(QCoreApplication.translate("MainWindow", u"Calculated Outputs", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Speed Ratio (<var>S<sub>r</sub></var>)", None))
        self.speedRatioOutput.setText("")
        self.speedRatioOutput.setPlaceholderText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Design Power (<var>P<sub>D</sub></var>)", None))
        self.designPowerOutput.setText("")
        self.designPowerOutput.setPlaceholderText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Other Pulley Diameter", None))
        self.pulleyDiameterOutput.setText("")
        self.pulleyDiameterOutput.setPlaceholderText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Belt Length (<var>L<sub>P</sub></var>)", None))
        self.beltLengthOutput.setText("")
        self.beltLengthOutput.setPlaceholderText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Power Rating (<var>P</var>)", None))
        self.powerRatingOutput.setText("")
        self.powerRatingOutput.setPlaceholderText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Number of Belts (<var>N</var>)", None))
        self.beltNumberOutput.setText("")
        self.beltNumberOutput.setPlaceholderText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Belt Speed (<var>V</var>)", None))
        self.beltSpeedOutput.setText("")
        self.beltSpeedOutput.setPlaceholderText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Exact Center Distance (<var>C</var>)", None))
        self.exactCenterOutput.setText("")
        self.exactCenterOutput.setPlaceholderText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Effective Tension (<var>T<sub>e</sub></var>)", None))
        self.effectiveTensionOutput.setText("")
        self.effectiveTensionOutput.setPlaceholderText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Torque (<var>T<sub>q</sub></var>)", None))
        self.torqueOutput.setText("")
        self.torqueOutput.setPlaceholderText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Tight Side Tension(<var>T<sub>t</sub></var>)", None))
        self.tightOutput.setText("")
        self.tightOutput.setPlaceholderText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Slack Side Tension(<var>T<sub>s</sub></var>)", None))
        self.slackOutput.setText("")
        self.slackOutput.setPlaceholderText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Tension Ratio (<var>T<sub>r</sub></var>)", None))
        self.tensionRatioOutput.setText("")
        self.tensionRatioOutput.setPlaceholderText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Minimum Static Tension (<var>T<sub>m</sub></var>)", None))
        self.staticTensionOutput.setText("")
        self.staticTensionOutput.setPlaceholderText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Belt contact angle (<var>\u03b2</var>)", None))
        self.contactAngleOutput.setText("")
        self.contactAngleOutput.setPlaceholderText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Static Shaft Load (<var>L<sub>s</sub></var>)", None))
        self.shaftLoadOutput.setText("")
        self.shaftLoadOutput.setPlaceholderText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Angle of Wrap (<var>a<sub>1</sub></var>)", None))
        self.wrapAngleOutput.setText("")
        self.wrapAngleOutput.setPlaceholderText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Angle of Wrap (<var>a<sub>2</sub></var>)", None))
        self.wrapAngleOutput_2.setText("")
        self.wrapAngleOutput_2.setPlaceholderText("")
        self.resultText.setMarkdown("")
        self.resultText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Merriweather'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next Tab", None))
#if QT_CONFIG(shortcut)
        self.nextButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.clearInputButton.setText(QCoreApplication.translate("MainWindow", u"Clear Inputs", None))
#if QT_CONFIG(shortcut)
        self.clearInputButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+I", None))
#endif // QT_CONFIG(shortcut)
        self.clearResultButton.setText(QCoreApplication.translate("MainWindow", u"Clear Results", None))
#if QT_CONFIG(shortcut)
        self.clearResultButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.clearAllButton.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
#if QT_CONFIG(shortcut)
        self.clearAllButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(shortcut)
        self.calculateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.transmissions.setTabText(self.transmissions.indexOf(self.belt), QCoreApplication.translate("MainWindow", u"Belt Drive", None))
        self.chainTitle.setText(QCoreApplication.translate("MainWindow", u"Chain Drive Calculator", None))
        self.chainSubtitle.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Syne'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30%;\">Chain drives use a metal chain and sprockets to transfer power. The chain wraps</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30%;\">around the sprockets, allowing for efficient power transmission, especially</p>\n"
"<p align=\"center\" style=\" margin-top:12"
                        "px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:30%;\">in applications requiring high torque and heavy loads. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
#if QT_CONFIG(tooltip)
        self.smallSprocketSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter no of teeth", None))
#endif // QT_CONFIG(tooltip)
        self.smallSprocketSelect.setText(QCoreApplication.translate("MainWindow", u"Small sprocket (Z1)", None))
        self.massInput.setText("")
        self.massInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter mass in kg/m2", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Constant due to arrangement of drive (<var>K</var>)", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"No of rev. on smaller sprocket (<var>n<sub>1</sub></var>)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pin body diameter (<var>P<sub>b</sub></var>)", None))
        self.bearingAreaInput.setText("")
        self.bearingAreaInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter bearing area in mm", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_35.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Initial sag", None))
        self.overallJointInput.setText("")
        self.overallJointInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter maximum overall joint in mm", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Breaking load (<var>Q</var>)", None))
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_55.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Load Factor (<var>K<sub>t</sub</var>)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Plate maximum diameter (<var>D<sub>h</sub></var>)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Tranverse Pitch (<var>P<sub>t</sub></var>)", None))
#if QT_CONFIG(tooltip)
        self.label_31.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_31.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Service Factor (<var>K<sub>s</sub></var>)", None))
        self.chainRev1Input.setText("")
        self.chainRev1Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter no of rev. in rpm", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Rated Power (<var>P<sub>r</sub></var>)", None))
        self.betweenWidthInput.setText("")
        self.betweenWidthInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter width between inner plate in mm", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Center Distance (<var>a<sub>p</sub></var>)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Width between inner plate (<var>W</var>)", None))
        self.constantInput.setText("")
        self.constantInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter constant", None))
        self.transmissionRatioInput.setText("")
        self.transmissionRatioInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter transmission ratio", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_19.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Maximum overall joint (<var>A<sub>1</sub></var>, <var>A<sub>2</sub></var>)", None))
        self.initialSagInput.setText("")
        self.initialSagInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter inital sag in mm", None))
        self.rollerDiameterInput.setText("")
        self.rollerDiameterInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter maximum roller diameter in mm", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_30.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Transmission ratio (<var>i</var>)", None))
        self.breakingLoadInput.setText("")
        self.breakingLoadInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter breaking load in N", None))
        self.centerDistanceInput.setText("")
        self.centerDistanceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter assumed center distance in mm", None))
        self.plateDiameterInput.setText("")
        self.plateDiameterInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter plate maximum diameter in mm", None))
        self.pinDiameterInput.setText("")
        self.pinDiameterInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pin body diameter in mm", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Number of teeth (<span style=\" font-style:italic;\">Z)</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pitch (<var>P</var>)", None))
        self.tranversePitchInput.setText("")
        self.tranversePitchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter transverse pitch in mm", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Maximum roller diameter (<var>D<sub>r</sub></var>)", None))
#if QT_CONFIG(tooltip)
        self.bigSprocketSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter no of teeth", None))
#endif // QT_CONFIG(tooltip)
        self.bigSprocketSelect.setText(QCoreApplication.translate("MainWindow", u"Big sprocket (Z2)", None))
        self.chainPitchInput.setText("")
        self.chainPitchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pitch in mm", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Inner width of the plate (<var>W<sub>i</sub></var>)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Mass (<var>m</var>)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Bearing area (<var>A</var>)", None))
        self.innerWidthInput.setText("")
        self.innerWidthInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter inner width of the plate in mm", None))
        self.loadFactorInput.setText("")
        self.loadFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter load factor", None))
        self.chainRatedPowerInput.setText("")
        self.chainRatedPowerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter rated power in kW", None))
        self.serviceFactorInput.setText("")
        self.serviceFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter service factor", None))
#if QT_CONFIG(tooltip)
        self.teethInput.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the sprocket from the selection below</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.teethInput.setText("")
        self.teethInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter no of teeth", None))
        self.chainResults.setMarkdown("")
        self.chainResults.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Merriweather'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Previous Tab", None))
#if QT_CONFIG(shortcut)
        self.prevButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.chainClearInputsBtn.setText(QCoreApplication.translate("MainWindow", u"Clear Inputs", None))
#if QT_CONFIG(shortcut)
        self.chainClearInputsBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+I", None))
#endif // QT_CONFIG(shortcut)
        self.chainClearResultsBtn.setText(QCoreApplication.translate("MainWindow", u"Clear Results", None))
#if QT_CONFIG(shortcut)
        self.chainClearResultsBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.chainClearAll.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
#if QT_CONFIG(shortcut)
        self.chainClearAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.chainCalculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(shortcut)
        self.chainCalculateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.transmissions.setTabText(self.transmissions.indexOf(self.chain), QCoreApplication.translate("MainWindow", u"Chain Drive", None))
    # retranslateUi

