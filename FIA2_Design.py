# Form implementation generated from reading ui file 'FIA2_Design.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.team1background = QtWidgets.QLabel(self.centralwidget)
        self.team1background.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.team1background.setText("")
        self.team1background.setObjectName("team1background")
        self.horizontalLayout.addWidget(self.team1background)
        self.clockLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.clockLabel.setObjectName("clockLabel")
        self.horizontalLayout.addWidget(self.clockLabel)
        self.team2background = QtWidgets.QLabel(self.centralwidget)
        self.team2background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.team2background.setText("")
        self.team2background.setObjectName("team2background")
        self.horizontalLayout.addWidget(self.team2background)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.team1name = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team1name.sizePolicy().hasHeightForWidth())
        self.team1name.setSizePolicy(sizePolicy)
        self.team1name.setMinimumSize(QtCore.QSize(0, 91))
        self.team1name.setMaximumSize(QtCore.QSize(16777215, 91))
        self.team1name.setStyleSheet("font: 75 72pt \"Helvetica Neue\";")
        self.team1name.setObjectName("team1name")
        self.verticalLayout.addWidget(self.team1name)
        self.team1ScoreLabel = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team1ScoreLabel.sizePolicy().hasHeightForWidth())
        self.team1ScoreLabel.setSizePolicy(sizePolicy)
        self.team1ScoreLabel.setDigitCount(3)
        self.team1ScoreLabel.setObjectName("team1ScoreLabel")
        self.verticalLayout.addWidget(self.team1ScoreLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.team1SubtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.team1SubtractButton.setObjectName("team1SubtractButton")
        self.horizontalLayout_2.addWidget(self.team1SubtractButton)
        self.team1Add1Button = QtWidgets.QPushButton(self.centralwidget)
        self.team1Add1Button.setObjectName("team1Add1Button")
        self.horizontalLayout_2.addWidget(self.team1Add1Button)
        self.team1Add2Button = QtWidgets.QPushButton(self.centralwidget)
        self.team1Add2Button.setObjectName("team1Add2Button")
        self.horizontalLayout_2.addWidget(self.team1Add2Button)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.addMinuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMinuteButton.setObjectName("addMinuteButton")
        self.gridLayout.addWidget(self.addMinuteButton, 0, 1, 1, 1)
        self.addSecondButton = QtWidgets.QPushButton(self.centralwidget)
        self.addSecondButton.setObjectName("addSecondButton")
        self.gridLayout.addWidget(self.addSecondButton, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Team2Name = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Team2Name.sizePolicy().hasHeightForWidth())
        self.Team2Name.setSizePolicy(sizePolicy)
        self.Team2Name.setMaximumSize(QtCore.QSize(16777215, 91))
        self.Team2Name.setObjectName("Team2Name")
        self.verticalLayout_2.addWidget(self.Team2Name)
        self.team2ScoreLabel = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team2ScoreLabel.sizePolicy().hasHeightForWidth())
        self.team2ScoreLabel.setSizePolicy(sizePolicy)
        self.team2ScoreLabel.setDigitCount(3)
        self.team2ScoreLabel.setObjectName("team2ScoreLabel")
        self.verticalLayout_2.addWidget(self.team2ScoreLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.team2SubtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.team2SubtractButton.setObjectName("team2SubtractButton")
        self.horizontalLayout_3.addWidget(self.team2SubtractButton)
        self.team2Add1Button = QtWidgets.QPushButton(self.centralwidget)
        self.team2Add1Button.setObjectName("team2Add1Button")
        self.horizontalLayout_3.addWidget(self.team2Add1Button)
        self.team2Add2Button = QtWidgets.QPushButton(self.centralwidget)
        self.team2Add2Button.setObjectName("team2Add2Button")
        self.horizontalLayout_3.addWidget(self.team2Add2Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 2, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_4.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.frame)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_4.addWidget(self.pauseButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.resetTimerButton = QtWidgets.QPushButton(self.frame)
        self.resetTimerButton.setObjectName("resetTimerButton")
        self.verticalLayout_3.addWidget(self.resetTimerButton)
        self.resetScoresButton = QtWidgets.QPushButton(self.frame)
        self.resetScoresButton.setObjectName("resetScoresButton")
        self.verticalLayout_3.addWidget(self.resetScoresButton)
        self.resetAllButton = QtWidgets.QPushButton(self.frame)
        self.resetAllButton.setObjectName("resetAllButton")
        self.verticalLayout_3.addWidget(self.resetAllButton)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.team1background.raise_()
        self.team2ScoreLabel.raise_()
        self.team1ScoreLabel.raise_()
        self.team1name.raise_()
        self.Team2Name.raise_()
        self.resetTimerButton.raise_()
        self.resetScoresButton.raise_()
        self.resetAllButton.raise_()
        self.team1Add1Button.raise_()
        self.team1Add2Button.raise_()
        self.team1SubtractButton.raise_()
        self.team2Add2Button.raise_()
        self.team2Add1Button.raise_()
        self.team2SubtractButton.raise_()
        self.startButton.raise_()
        self.pauseButton.raise_()
        self.team2background.raise_()
        self.clockLabel.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.addMinuteButton.raise_()
        self.addSecondButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.team1name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Helvetica Neue\'; font-size:72pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Team 1</p></body></html>"))
        self.team1SubtractButton.setText(_translate("MainWindow", "-1"))
        self.team1Add1Button.setText(_translate("MainWindow", "+1"))
        self.team1Add2Button.setText(_translate("MainWindow", "+2"))
        self.addMinuteButton.setText(_translate("MainWindow", "Minutes"))
        self.addSecondButton.setText(_translate("MainWindow", "Seconds"))
        self.Team2Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">Team 2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:72pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:72pt;\"><br /></p></body></html>"))
        self.team2SubtractButton.setText(_translate("MainWindow", "-1"))
        self.team2Add1Button.setText(_translate("MainWindow", "+1"))
        self.team2Add2Button.setText(_translate("MainWindow", "+2"))
        self.startButton.setText(_translate("MainWindow", "Start Timer"))
        self.pauseButton.setText(_translate("MainWindow", "Pause Timer"))
        self.resetTimerButton.setText(_translate("MainWindow", "Reset Timer"))
        self.resetScoresButton.setText(_translate("MainWindow", "Reset Scores"))
        self.resetAllButton.setText(_translate("MainWindow", "Reset All"))
