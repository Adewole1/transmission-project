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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 1143)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(980, 16777215))
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
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"QPushButton::hover {\n"
"	background-color: rgb(69, 69, 232);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.transmissions = QTabWidget(self.centralwidget)
        self.transmissions.setObjectName(u"transmissions")
        sizePolicy.setHeightForWidth(self.transmissions.sizePolicy().hasHeightForWidth())
        self.transmissions.setSizePolicy(sizePolicy)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 936, 1022))
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

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamilies([u"Merriweather"])
        font2.setPointSize(12)
        font2.setWeight(QFont.Medium)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setFamilies([u"Syne"])
        font3.setPointSize(12)
        self.label_16.setFont(font3)
        self.label_16.setToolTipDuration(5)

        self.gridLayout.addWidget(self.label_16, 9, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.centerInput = QLineEdit(self.groupBox)
        self.centerInput.setObjectName(u"centerInput")
        palette2 = QPalette()
        self.centerInput.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Merriweather"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.centerInput.setFont(font4)
        self.centerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.centerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.centerInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.centerInput, 3, 1, 2, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.contactFactorInput = QLineEdit(self.groupBox)
        self.contactFactorInput.setObjectName(u"contactFactorInput")
        palette3 = QPalette()
        self.contactFactorInput.setPalette(palette3)
        self.contactFactorInput.setFont(font4)
        self.contactFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.contactFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.contactFactorInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.contactFactorInput, 8, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setToolTipDuration(5)

        self.gridLayout.addWidget(self.label_18, 9, 2, 1, 2)

        self.powerInput = QLineEdit(self.groupBox)
        self.powerInput.setObjectName(u"powerInput")
        palette4 = QPalette()
        self.powerInput.setPalette(palette4)
        self.powerInput.setFont(font4)
        self.powerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.powerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.powerInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.powerInput, 1, 1, 1, 1)

        self.addPowerInput = QLineEdit(self.groupBox)
        self.addPowerInput.setObjectName(u"addPowerInput")
        palette5 = QPalette()
        self.addPowerInput.setPalette(palette5)
        self.addPowerInput.setFont(font4)
        self.addPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.addPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.addPowerInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.addPowerInput, 6, 2, 1, 2)

        self.ratedPowerInput = QLineEdit(self.groupBox)
        self.ratedPowerInput.setObjectName(u"ratedPowerInput")
        palette6 = QPalette()
        self.ratedPowerInput.setPalette(palette6)
        self.ratedPowerInput.setFont(font4)
        self.ratedPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.ratedPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.ratedPowerInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ratedPowerInput, 6, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout.addWidget(self.label_14, 7, 1, 1, 1)

        self.beltLengthInput = QLineEdit(self.groupBox)
        self.beltLengthInput.setObjectName(u"beltLengthInput")
        palette7 = QPalette()
        self.beltLengthInput.setPalette(palette7)
        self.beltLengthInput.setFont(font4)
        self.beltLengthInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltLengthInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.beltLengthInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.beltLengthInput, 6, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setToolTipDuration(5)

        self.gridLayout.addWidget(self.label_13, 7, 2, 1, 2)

        self.smallPulleySelect = QRadioButton(self.groupBox)
        self.smallPulleySelect.setObjectName(u"smallPulleySelect")
        palette8 = QPalette()
        self.smallPulleySelect.setPalette(palette8)
        self.smallPulleySelect.setFont(font3)
        self.smallPulleySelect.setToolTipDuration(1000)

        self.gridLayout.addWidget(self.smallPulleySelect, 2, 3, 2, 1)

        self.takeAllowanceInput = QLineEdit(self.groupBox)
        self.takeAllowanceInput.setObjectName(u"takeAllowanceInput")
        palette9 = QPalette()
        self.takeAllowanceInput.setPalette(palette9)
        self.takeAllowanceInput.setFont(font4)
        self.takeAllowanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.takeAllowanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.takeAllowanceInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.takeAllowanceInput, 10, 1, 1, 1)

        self.factorInput = QLineEdit(self.groupBox)
        self.factorInput.setObjectName(u"factorInput")
        palette10 = QPalette()
        self.factorInput.setPalette(palette10)
        self.factorInput.setFont(font4)
        self.factorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.factorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.factorInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.factorInput, 1, 2, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.pitchInput = QLineEdit(self.groupBox)
        self.pitchInput.setObjectName(u"pitchInput")
        palette11 = QPalette()
        self.pitchInput.setPalette(palette11)
        self.pitchInput.setFont(font4)
        self.pitchInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.pitchInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.pitchInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pitchInput, 3, 2, 2, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setToolTipDuration(1000)

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.rev2Input = QLineEdit(self.groupBox)
        self.rev2Input.setObjectName(u"rev2Input")
        palette12 = QPalette()
        self.rev2Input.setPalette(palette12)
        self.rev2Input.setFont(font4)
        self.rev2Input.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.rev2Input.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.rev2Input.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.rev2Input, 3, 0, 2, 1)

        self.powerFactorInput = QLineEdit(self.groupBox)
        self.powerFactorInput.setObjectName(u"powerFactorInput")
        palette13 = QPalette()
        self.powerFactorInput.setPalette(palette13)
        self.powerFactorInput.setFont(font4)
        self.powerFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.powerFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.powerFactorInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.powerFactorInput, 8, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)

        self.beltWeightInput = QLineEdit(self.groupBox)
        self.beltWeightInput.setObjectName(u"beltWeightInput")
        palette14 = QPalette()
        self.beltWeightInput.setPalette(palette14)
        self.beltWeightInput.setFont(font4)
        self.beltWeightInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.beltWeightInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.beltWeightInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.beltWeightInput, 10, 0, 1, 1)

        self.rev1Input = QLineEdit(self.groupBox)
        self.rev1Input.setObjectName(u"rev1Input")
        palette15 = QPalette()
        self.rev1Input.setPalette(palette15)
        self.rev1Input.setFont(font4)
        self.rev1Input.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.rev1Input.setFrame(True)
        self.rev1Input.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.rev1Input, 1, 0, 1, 1)

        self.crossBelt = QCheckBox(self.groupBox)
        self.crossBelt.setObjectName(u"crossBelt")
        font5 = QFont()
        font5.setFamilies([u"Syne"])
        font5.setPointSize(12)
        font5.setWeight(QFont.Medium)
        self.crossBelt.setFont(font5)
        self.crossBelt.setToolTipDuration(1000)

        self.gridLayout.addWidget(self.crossBelt, 10, 2, 1, 1)

        self.bigPulleySelect = QRadioButton(self.groupBox)
        self.bigPulleySelect.setObjectName(u"bigPulleySelect")
        palette16 = QPalette()
        self.bigPulleySelect.setPalette(palette16)
        self.bigPulleySelect.setFont(font3)
        self.bigPulleySelect.setToolTipDuration(1000)

        self.gridLayout.addWidget(self.bigPulleySelect, 4, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.instAllowanceInput = QLineEdit(self.groupBox)
        self.instAllowanceInput.setObjectName(u"instAllowanceInput")
        palette17 = QPalette()
        self.instAllowanceInput.setPalette(palette17)
        self.instAllowanceInput.setFont(font4)
        self.instAllowanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.instAllowanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.instAllowanceInput.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.instAllowanceInput, 8, 2, 1, 2)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resultText = QTextEdit(self.widget)
        self.resultText.setObjectName(u"resultText")
        palette18 = QPalette()
        self.resultText.setPalette(palette18)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 936, 1022))
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
        palette19 = QPalette()
        self.smallSprocketSelect.setPalette(palette19)
        self.smallSprocketSelect.setFont(font3)
        self.smallSprocketSelect.setToolTipDuration(1000)

        self.gridLayout_2.addWidget(self.smallSprocketSelect, 15, 2, 1, 1)

        self.massInput = QLineEdit(self.groupBox_2)
        self.massInput.setObjectName(u"massInput")
        palette20 = QPalette()
        self.massInput.setPalette(palette20)
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
        palette21 = QPalette()
        self.bearingAreaInput.setPalette(palette21)
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
        palette22 = QPalette()
        self.overallJointInput.setPalette(palette22)
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
        palette23 = QPalette()
        self.chainRev1Input.setPalette(palette23)
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
        palette24 = QPalette()
        self.betweenWidthInput.setPalette(palette24)
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
        palette25 = QPalette()
        self.constantInput.setPalette(palette25)
        self.constantInput.setFont(font4)
        self.constantInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.constantInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.constantInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.constantInput, 18, 0, 1, 1)

        self.transmissionRatioInput = QLineEdit(self.groupBox_2)
        self.transmissionRatioInput.setObjectName(u"transmissionRatioInput")
        palette26 = QPalette()
        self.transmissionRatioInput.setPalette(palette26)
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
        palette27 = QPalette()
        self.initialSagInput.setPalette(palette27)
        self.initialSagInput.setFont(font4)
        self.initialSagInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.initialSagInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.initialSagInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.initialSagInput, 15, 1, 1, 1)

        self.rollerDiameterInput = QLineEdit(self.groupBox_2)
        self.rollerDiameterInput.setObjectName(u"rollerDiameterInput")
        palette28 = QPalette()
        self.rollerDiameterInput.setPalette(palette28)
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
        palette29 = QPalette()
        self.breakingLoadInput.setPalette(palette29)
        self.breakingLoadInput.setFont(font4)
        self.breakingLoadInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.breakingLoadInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.breakingLoadInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.breakingLoadInput, 7, 1, 1, 1)

        self.centerDistanceInput = QLineEdit(self.groupBox_2)
        self.centerDistanceInput.setObjectName(u"centerDistanceInput")
        palette30 = QPalette()
        self.centerDistanceInput.setPalette(palette30)
        self.centerDistanceInput.setFont(font4)
        self.centerDistanceInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.centerDistanceInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.centerDistanceInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.centerDistanceInput, 15, 0, 1, 1)

        self.plateDiameterInput = QLineEdit(self.groupBox_2)
        self.plateDiameterInput.setObjectName(u"plateDiameterInput")
        palette31 = QPalette()
        self.plateDiameterInput.setPalette(palette31)
        self.plateDiameterInput.setFont(font4)
        self.plateDiameterInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.plateDiameterInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.plateDiameterInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.plateDiameterInput, 3, 0, 1, 1)

        self.pinDiameterInput = QLineEdit(self.groupBox_2)
        self.pinDiameterInput.setObjectName(u"pinDiameterInput")
        palette32 = QPalette()
        self.pinDiameterInput.setPalette(palette32)
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
        palette33 = QPalette()
        self.tranversePitchInput.setPalette(palette33)
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
        palette34 = QPalette()
        self.bigSprocketSelect.setPalette(palette34)
        self.bigSprocketSelect.setFont(font3)
        self.bigSprocketSelect.setToolTipDuration(1000)

        self.gridLayout_2.addWidget(self.bigSprocketSelect, 13, 2, 1, 1)

        self.chainPitchInput = QLineEdit(self.groupBox_2)
        self.chainPitchInput.setObjectName(u"chainPitchInput")
        palette35 = QPalette()
        self.chainPitchInput.setPalette(palette35)
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
        palette36 = QPalette()
        self.innerWidthInput.setPalette(palette36)
        self.innerWidthInput.setFont(font4)
        self.innerWidthInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.innerWidthInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.innerWidthInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.innerWidthInput, 3, 1, 1, 1)

        self.loadFactorInput = QLineEdit(self.groupBox_2)
        self.loadFactorInput.setObjectName(u"loadFactorInput")
        palette37 = QPalette()
        self.loadFactorInput.setPalette(palette37)
        self.loadFactorInput.setFont(font4)
        self.loadFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.loadFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.loadFactorInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.loadFactorInput, 18, 1, 1, 1)

        self.chainRatedPowerInput = QLineEdit(self.groupBox_2)
        self.chainRatedPowerInput.setObjectName(u"chainRatedPowerInput")
        palette38 = QPalette()
        self.chainRatedPowerInput.setPalette(palette38)
        self.chainRatedPowerInput.setFont(font4)
        self.chainRatedPowerInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.chainRatedPowerInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.chainRatedPowerInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.chainRatedPowerInput, 10, 0, 1, 1)

        self.serviceFactorInput = QLineEdit(self.groupBox_2)
        self.serviceFactorInput.setObjectName(u"serviceFactorInput")
        palette39 = QPalette()
        self.serviceFactorInput.setPalette(palette39)
        self.serviceFactorInput.setFont(font4)
        self.serviceFactorInput.setStyleSheet(u"font: 700 10pt \"Merriweather\";")
        self.serviceFactorInput.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.serviceFactorInput.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.serviceFactorInput, 10, 1, 1, 1)

        self.teethInput = QLineEdit(self.groupBox_2)
        self.teethInput.setObjectName(u"teethInput")
        palette40 = QPalette()
        self.teethInput.setPalette(palette40)
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
        palette41 = QPalette()
        self.chainResults.setPalette(palette41)
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
        self.menubar.setGeometry(QRect(0, 0, 980, 33))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Takeup allowance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Power on drive shaft (<var>P</var>)", None))
        self.centerInput.setText("")
        self.centerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter distance between pulleys in mm", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Belt Weight (W)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Standard Belt Length (<var>L</var>)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Approx. Center distance (<var>C</var>)", None))
        self.contactFactorInput.setText("")
        self.contactFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter arc of contact correctional factor", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_18.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"*Check if belt is crossed", None))
        self.powerInput.setText("")
        self.powerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter power on drive shaft in kW", None))
        self.addPowerInput.setText("")
        self.addPowerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter additional power for speed ratio in kW", None))
        self.ratedPowerInput.setText("")
        self.ratedPowerInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter rated power in kW", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Power Correctional Factor (<var>F<sub>L</sub></var>)", None))
        self.beltLengthInput.setText("")
        self.beltLengthInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter belt length from table in mm", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Installation allowance", None))
#if QT_CONFIG(tooltip)
        self.smallPulleySelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter pitch diameter in field to the left", None))
#endif // QT_CONFIG(tooltip)
        self.smallPulleySelect.setText(QCoreApplication.translate("MainWindow", u"Small pulley (d)", None))
        self.takeAllowanceInput.setText("")
        self.takeAllowanceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter allowance in mm", None))
        self.factorInput.setText("")
        self.factorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter service factor", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"No of rev. on centrifugal pump (<var>N<sub>2</sub></var>)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Arc of Contact Correctional Factor (<var>F<sub>A</sub></var>)", None))
        self.pitchInput.setText("")
        self.pitchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pulley pitch", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"Also select the pitch from the selection to the right", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pitch Diameter", None))
        self.rev2Input.setText("")
        self.rev2Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pump revolutions in rpm", None))
        self.powerFactorInput.setText("")
        self.powerFactorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter power correctional factor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No of rev. on drive shaft (<var>N<sub>1</sub></var>)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rated Power", None))
        self.beltWeightInput.setText("")
        self.beltWeightInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter belt weight", None))
        self.rev1Input.setText("")
        self.rev1Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter drive shaft revolutions in rpm", None))
#if QT_CONFIG(tooltip)
        self.crossBelt.setToolTip(QCoreApplication.translate("MainWindow", u"Check this box if belt is cross type", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.crossBelt.setWhatsThis(QCoreApplication.translate("MainWindow", u"Check this box if belt is cross type", None))
#endif // QT_CONFIG(whatsthis)
        self.crossBelt.setText(QCoreApplication.translate("MainWindow", u"Cross Belt", None))
#if QT_CONFIG(tooltip)
        self.bigPulleySelect.setToolTip(QCoreApplication.translate("MainWindow", u"Enter pitch diameter in field to the left", None))
#endif // QT_CONFIG(tooltip)
        self.bigPulleySelect.setText(QCoreApplication.translate("MainWindow", u"Big pulley (D)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Service Factor (<var>K</var>)", None))
        self.instAllowanceInput.setText("")
        self.instAllowanceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter allowance in mm", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Additional Power", None))
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

