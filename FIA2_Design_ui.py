# Form implementation generated from reading ui file '/Users/ryanwpc/Desktop/FIA2 Digital Solutions/FIA2-Scoreboard-Code/FIA2_Design.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setStyleSheet("background-color: rgb(64, 77, 84);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.team1background = QtWidgets.QLabel(parent=self.centralwidget)
        self.team1background.setStyleSheet("background-color: rgb(0, 174, 239);")
        self.team1background.setText("")
        self.team1background.setObjectName("team1background")
        self.horizontalLayout.addWidget(self.team1background)
        self.clockLabel = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.clockLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 13pt \".AppleSystemUIFont\";")
        self.clockLabel.setObjectName("clockLabel")
        self.horizontalLayout.addWidget(self.clockLabel)
        self.team2background = QtWidgets.QLabel(parent=self.centralwidget)
        self.team2background.setStyleSheet("background-color: rgb(186, 1, 78);")
        self.team2background.setText("")
        self.team2background.setObjectName("team2background")
        self.horizontalLayout.addWidget(self.team2background)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.team1name = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team1name.sizePolicy().hasHeightForWidth())
        self.team1name.setSizePolicy(sizePolicy)
        self.team1name.setMinimumSize(QtCore.QSize(0, 91))
        self.team1name.setMaximumSize(QtCore.QSize(16777215, 91))
        self.team1name.setStyleSheet("font: 75 72pt \"Helvetica Neue\"; background-color: rgb(255, 255, 255);")
        self.team1name.setObjectName("team1name")
        self.verticalLayout.addWidget(self.team1name)
        self.team1ScoreLabel = QtWidgets.QLCDNumber(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team1ScoreLabel.sizePolicy().hasHeightForWidth())
        self.team1ScoreLabel.setSizePolicy(sizePolicy)
        self.team1ScoreLabel.setStyleSheet("background-color: rgb(0, 174, 239);")
        self.team1ScoreLabel.setDigitCount(3)
        self.team1ScoreLabel.setObjectName("team1ScoreLabel")
        self.verticalLayout.addWidget(self.team1ScoreLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.team1SubtractButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team1SubtractButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team1SubtractButton.setObjectName("team1SubtractButton")
        self.horizontalLayout_2.addWidget(self.team1SubtractButton)
        self.team1Add1Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team1Add1Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team1Add1Button.setObjectName("team1Add1Button")
        self.horizontalLayout_2.addWidget(self.team1Add1Button)
        self.team1Add2Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team1Add2Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team1Add2Button.setObjectName("team1Add2Button")
        self.horizontalLayout_2.addWidget(self.team1Add2Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.addMinuteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addMinuteButton.setStyleSheet("background-color: rgb(0, 174, 239);")
        self.addMinuteButton.setObjectName("addMinuteButton")
        self.gridLayout.addWidget(self.addMinuteButton, 0, 1, 1, 1)
        self.addSecondButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addSecondButton.setStyleSheet("background-color: rgb(186, 1, 78);")
        self.addSecondButton.setObjectName("addSecondButton")
        self.gridLayout.addWidget(self.addSecondButton, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Team2Name = QtWidgets.QTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Team2Name.sizePolicy().hasHeightForWidth())
        self.Team2Name.setSizePolicy(sizePolicy)
        self.Team2Name.setMaximumSize(QtCore.QSize(16777215, 91))
        self.Team2Name.setStyleSheet("font: 75 72pt \"Helvetica Neue\"; background-color: rgb(255, 255, 255);")
        self.Team2Name.setObjectName("Team2Name")
        self.verticalLayout_2.addWidget(self.Team2Name)
        self.team2ScoreLabel = QtWidgets.QLCDNumber(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team2ScoreLabel.sizePolicy().hasHeightForWidth())
        self.team2ScoreLabel.setSizePolicy(sizePolicy)
        self.team2ScoreLabel.setStyleSheet("background-color: rgb(186, 1, 78);")
        self.team2ScoreLabel.setDigitCount(3)
        self.team2ScoreLabel.setObjectName("team2ScoreLabel")
        self.verticalLayout_2.addWidget(self.team2ScoreLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.team2SubtractButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team2SubtractButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team2SubtractButton.setObjectName("team2SubtractButton")
        self.horizontalLayout_3.addWidget(self.team2SubtractButton)
        self.team2Add1Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team2Add1Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team2Add1Button.setObjectName("team2Add1Button")
        self.horizontalLayout_3.addWidget(self.team2Add1Button)
        self.team2Add2Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.team2Add2Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team2Add2Button.setObjectName("team2Add2Button")
        self.horizontalLayout_3.addWidget(self.team2Add2Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 2, 1)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startButton = QtWidgets.QPushButton(parent=self.frame)
        self.startButton.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(parent=self.frame)
        self.pauseButton.setStyleSheet("background-color: rgb(252, 1, 7);")
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout_3.addWidget(self.pauseButton)
        self.resetTimerButton = QtWidgets.QPushButton(parent=self.frame)
        self.resetTimerButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resetTimerButton.setObjectName("resetTimerButton")
        self.verticalLayout_3.addWidget(self.resetTimerButton)
        self.resetScoresButton = QtWidgets.QPushButton(parent=self.frame)
        self.resetScoresButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resetScoresButton.setObjectName("resetScoresButton")
        self.verticalLayout_3.addWidget(self.resetScoresButton)
        self.resetAllButton = QtWidgets.QPushButton(parent=self.frame)
        self.resetAllButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resetAllButton.setObjectName("resetAllButton")
        self.verticalLayout_3.addWidget(self.resetAllButton)
        self.presetsComboBox = QtWidgets.QComboBox(parent=self.frame)
        self.presetsComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.presetsComboBox.setObjectName("presetsComboBox")
        self.verticalLayout_3.addWidget(self.presetsComboBox)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
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
"</style></head><body style=\" font-family:\'Helvetica Neue\'; font-size:72pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Team 1</p></body></html>"))
        self.team2SubtractButton.setText(_translate("MainWindow", "-1"))
        self.team2Add1Button.setText(_translate("MainWindow", "+1"))
        self.team2Add2Button.setText(_translate("MainWindow", "+2"))
        self.startButton.setText(_translate("MainWindow", "Start Timer"))
        self.pauseButton.setText(_translate("MainWindow", "Pause Timer"))
        self.resetTimerButton.setText(_translate("MainWindow", "Reset Timer"))
        self.resetScoresButton.setText(_translate("MainWindow", "Reset Scores"))
        self.resetAllButton.setText(_translate("MainWindow", "Reset All"))
