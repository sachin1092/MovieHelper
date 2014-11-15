# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Nov 10 03:45:19 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
# import PySide

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.resize(641, 593)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        mainWindow.setFont(font)
        mainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic_launcher.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("QMainWindow #mainWindow {\nbackground-color:#ffffff\n}")
        mainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backButton = QtGui.QToolButton(self.centralWidget)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.mainframe = QtGui.QFrame(self.centralWidget)
        self.mainframe.setStyleSheet("\n"
"background-color: rgb(63, 81, 181);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px;\n"
"border-radius: 2px;\n"
"")
        self.mainframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtGui.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mainframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uselessGWidget = QtGui.QWidget(self.mainframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uselessGWidget.sizePolicy().hasHeightForWidth())
        self.uselessGWidget.setSizePolicy(sizePolicy)
        self.uselessGWidget.setAcceptDrops(True)
        self.uselessGWidget.setAutoFillBackground(False)
        self.uselessGWidget.setStyleSheet("")
        self.uselessGWidget.setObjectName("uselessGWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.uselessGWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtGui.QProgressBar(self.uselessGWidget)
        self.progressBar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.progressBar.setBaseSize(QtCore.QSize(0, 20))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d81b60;\n"
"    width: 70px;\n"
"    margin: 0.5px;\n"
"}")
        self.progressBar.setMaximum(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 3)
        self.buttinClear = QtGui.QPushButton(self.uselessGWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.buttinClear.setFont(font)
        self.buttinClear.setStyleSheet("QPushButton{\n"
"background-color:#fff;\n"
"font: 9pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:#e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #9e9e9e;\n"
"}")
        self.buttinClear.setObjectName("buttinClear")
        self.gridLayout_2.addWidget(self.buttinClear, 2, 2, 1, 1)
        self.leSearch = QtGui.QLineEdit(self.uselessGWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        self.leSearch.setFont(font)
        self.leSearch.setStyleSheet("background-color:#fff")
        self.leSearch.setObjectName("leSearch")
        self.gridLayout_2.addWidget(self.leSearch, 2, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.uselessGWidget)
        self.verticalLayout.addWidget(self.mainframe)
        self.tvEverything = QtGui.QTableView(self.centralWidget)
        self.tvEverything.setObjectName("tvEverything")
        self.verticalLayout.addWidget(self.tvEverything)
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menuBar.setObjectName("menuBar")
        mainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.buttinClear, QtCore.SIGNAL("clicked()"), self.leSearch.clear)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Movies Helper", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("mainWindow", "Change folder", None, QtGui.QApplication.UnicodeUTF8))
        self.buttinClear.setText(QtGui.QApplication.translate("mainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.leSearch.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))

