# Form implementation generated from reading ui file 'FIA2_Design_1.ui'
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
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Team2Score = QtWidgets.QLCDNumber(self.centralwidget)
        self.Team2Score.setGeometry(QtCore.QRect(630, 280, 321, 131))
        self.Team2Score.setDigitCount(3)
        self.Team2Score.setObjectName("Team2Score")
        self.Team1Score = QtWidgets.QLCDNumber(self.centralwidget)
        self.Team1Score.setGeometry(QtCore.QRect(10, 280, 321, 141))
        self.Team1Score.setDigitCount(3)
        self.Team1Score.setObjectName("Team1Score")
        self.Team1Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Team1Name.setGeometry(QtCore.QRect(10, 180, 321, 91))
        self.Team1Name.setObjectName("Team1Name")
        self.Team2Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Team2Name.setGeometry(QtCore.QRect(630, 180, 321, 91))
        self.Team2Name.setObjectName("Team2Name")
        self.ResetTimer = QtWidgets.QPushButton(self.centralwidget)
        self.ResetTimer.setGeometry(QtCore.QRect(410, 310, 141, 61))
        self.ResetTimer.setObjectName("ResetTimer")
        self.ResetScores = QtWidgets.QPushButton(self.centralwidget)
        self.ResetScores.setGeometry(QtCore.QRect(410, 370, 141, 61))
        self.ResetScores.setObjectName("ResetScores")
        self.ResetAll = QtWidgets.QPushButton(self.centralwidget)
        self.ResetAll.setGeometry(QtCore.QRect(410, 430, 141, 61))
        self.ResetAll.setObjectName("ResetAll")
        self.add1team1 = QtWidgets.QPushButton(self.centralwidget)
        self.add1team1.setGeometry(QtCore.QRect(130, 430, 61, 61))
        self.add1team1.setObjectName("add1team1")
        self.add2team1 = QtWidgets.QPushButton(self.centralwidget)
        self.add2team1.setGeometry(QtCore.QRect(210, 430, 61, 61))
        self.add2team1.setObjectName("add2team1")
        self.minus1team1 = QtWidgets.QPushButton(self.centralwidget)
        self.minus1team1.setGeometry(QtCore.QRect(50, 430, 61, 61))
        self.minus1team1.setObjectName("minus1team1")
        self.add2team2 = QtWidgets.QPushButton(self.centralwidget)
        self.add2team2.setGeometry(QtCore.QRect(850, 420, 61, 61))
        self.add2team2.setObjectName("add2team2")
        self.add1team2 = QtWidgets.QPushButton(self.centralwidget)
        self.add1team2.setGeometry(QtCore.QRect(770, 420, 61, 61))
        self.add1team2.setObjectName("add1team2")
        self.minus1team2 = QtWidgets.QPushButton(self.centralwidget)
        self.minus1team2.setGeometry(QtCore.QRect(690, 420, 61, 61))
        self.minus1team2.setObjectName("minus1team2")
        self.Timerstart = QtWidgets.QPushButton(self.centralwidget)
        self.Timerstart.setGeometry(QtCore.QRect(340, 250, 141, 61))
        self.Timerstart.setObjectName("Timerstart")
        self.Timerpause = QtWidgets.QPushButton(self.centralwidget)
        self.Timerpause.setGeometry(QtCore.QRect(480, 250, 141, 61))
        self.Timerpause.setObjectName("Timerpause")
        self.team1background = QtWidgets.QLabel(self.centralwidget)
        self.team1background.setGeometry(QtCore.QRect(10, 0, 251, 171))
        self.team1background.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.team1background.setText("")
        self.team1background.setObjectName("team1background")
        self.team2background = QtWidgets.QLabel(self.centralwidget)
        self.team2background.setGeometry(QtCore.QRect(700, 0, 251, 171))
        self.team2background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.team2background.setText("")
        self.team2background.setObjectName("team2background")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(270, 0, 421, 171))
        self.lcdNumber.setObjectName("lcdNumber")
        self.team1background.raise_()
        self.Team2Score.raise_()
        self.Team1Score.raise_()
        self.Team1Name.raise_()
        self.Team2Name.raise_()
        self.ResetTimer.raise_()
        self.ResetScores.raise_()
        self.ResetAll.raise_()
        self.add1team1.raise_()
        self.add2team1.raise_()
        self.minus1team1.raise_()
        self.add2team2.raise_()
        self.add1team2.raise_()
        self.minus1team2.raise_()
        self.Timerstart.raise_()
        self.Timerpause.raise_()
        self.team2background.raise_()
        self.lcdNumber.raise_()
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
        self.Team1Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">Team 1 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:72pt;\"><br /></p></body></html>"))
        self.Team2Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">Team 2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:72pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:72pt;\"><br /></p></body></html>"))
        self.ResetTimer.setText(_translate("MainWindow", "Reset Timer"))
        self.ResetScores.setText(_translate("MainWindow", "Reset Scores"))
        self.ResetAll.setText(_translate("MainWindow", "Reset All"))
        self.add1team1.setText(_translate("MainWindow", "+1"))
        self.add2team1.setText(_translate("MainWindow", "+2"))
        self.minus1team1.setText(_translate("MainWindow", "-1"))
        self.add2team2.setText(_translate("MainWindow", "+2"))
        self.add1team2.setText(_translate("MainWindow", "+1"))
        self.minus1team2.setText(_translate("MainWindow", "-1"))
        self.Timerstart.setText(_translate("MainWindow", "Start Timer"))
        self.Timerpause.setText(_translate("MainWindow", "Pause Timer"))