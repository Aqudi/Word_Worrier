# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game Main Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 644)
        MainWindow.setMinimumSize(QtCore.QSize(866, 644))
        MainWindow.setMaximumSize(QtCore.QSize(866, 644))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VillainPicture = QtWidgets.QLabel(self.centralwidget)
        self.VillainPicture.setGeometry(QtCore.QRect(630, 40, 211, 251))
        self.VillainPicture.setMinimumSize(QtCore.QSize(211, 251))
        self.VillainPicture.setMaximumSize(QtCore.QSize(211, 251))
        self.VillainPicture.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.VillainPicture.setText("")
        self.VillainPicture.setPixmap(QtGui.QPixmap(":/newPrefix/First Boss.PNG"))
        self.VillainPicture.setScaledContents(True)
        self.VillainPicture.setWordWrap(False)
        self.VillainPicture.setObjectName("VillainPicture")
        self.HeroPicture = QtWidgets.QLabel(self.centralwidget)
        self.HeroPicture.setGeometry(QtCore.QRect(20, 40, 211, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeroPicture.sizePolicy().hasHeightForWidth())
        self.HeroPicture.setSizePolicy(sizePolicy)
        self.HeroPicture.setMinimumSize(QtCore.QSize(211, 251))
        self.HeroPicture.setMaximumSize(QtCore.QSize(211, 251))
        self.HeroPicture.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.HeroPicture.setText("")
        self.HeroPicture.setPixmap(QtGui.QPixmap(":/newPrefix/Hero.PNG"))
        self.HeroPicture.setScaledContents(True)
        self.HeroPicture.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.HeroPicture.setObjectName("HeroPicture")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 40, 381, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StatusLabels = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StatusLabels.setContentsMargins(0, 0, 0, 0)
        self.StatusLabels.setObjectName("StatusLabels")
        self.attackSummary = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attackSummary.sizePolicy().hasHeightForWidth())
        self.attackSummary.setSizePolicy(sizePolicy)
        self.attackSummary.setFrameShape(QtWidgets.QFrame.Box)
        self.attackSummary.setText("")
        self.attackSummary.setObjectName("attackSummary")
        self.StatusLabels.addWidget(self.attackSummary)
        self.APLayout = QtWidgets.QHBoxLayout()
        self.APLayout.setObjectName("APLayout")
        self.AP_Hero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.AP_Hero.setFrameShape(QtWidgets.QFrame.Box)
        self.AP_Hero.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AP_Hero.setObjectName("AP_Hero")
        self.APLayout.addWidget(self.AP_Hero)
        self.AttackPoint = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AttackPoint.sizePolicy().hasHeightForWidth())
        self.AttackPoint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.AttackPoint.setFont(font)
        self.AttackPoint.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AttackPoint.setTextFormat(QtCore.Qt.PlainText)
        self.AttackPoint.setScaledContents(False)
        self.AttackPoint.setAlignment(QtCore.Qt.AlignCenter)
        self.AttackPoint.setWordWrap(False)
        self.AttackPoint.setObjectName("AttackPoint")
        self.APLayout.addWidget(self.AttackPoint)
        self.AP_villain = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.AP_villain.setFrameShape(QtWidgets.QFrame.Box)
        self.AP_villain.setObjectName("AP_villain")
        self.APLayout.addWidget(self.AP_villain)
        self.StatusLabels.addLayout(self.APLayout)
        self.ACLayout = QtWidgets.QHBoxLayout()
        self.ACLayout.setObjectName("ACLayout")
        self.AC_Hero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.AC_Hero.setFrameShape(QtWidgets.QFrame.Box)
        self.AC_Hero.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AC_Hero.setObjectName("AC_Hero")
        self.ACLayout.addWidget(self.AC_Hero)
        self.AvoidChance = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvoidChance.sizePolicy().hasHeightForWidth())
        self.AvoidChance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.AvoidChance.setFont(font)
        self.AvoidChance.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AvoidChance.setTextFormat(QtCore.Qt.PlainText)
        self.AvoidChance.setScaledContents(False)
        self.AvoidChance.setAlignment(QtCore.Qt.AlignCenter)
        self.AvoidChance.setWordWrap(False)
        self.AvoidChance.setObjectName("AvoidChance")
        self.ACLayout.addWidget(self.AvoidChance)
        self.AC_villain = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.AC_villain.setFrameShape(QtWidgets.QFrame.Box)
        self.AC_villain.setObjectName("AC_villain")
        self.ACLayout.addWidget(self.AC_villain)
        self.StatusLabels.addLayout(self.ACLayout)
        self.CCLayout = QtWidgets.QHBoxLayout()
        self.CCLayout.setObjectName("CCLayout")
        self.CC_Hero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CC_Hero.setFrameShape(QtWidgets.QFrame.Box)
        self.CC_Hero.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CC_Hero.setObjectName("CC_Hero")
        self.CCLayout.addWidget(self.CC_Hero)
        self.CriticalChance = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CriticalChance.sizePolicy().hasHeightForWidth())
        self.CriticalChance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("휴먼아미체")
        font.setPointSize(18)
        self.CriticalChance.setFont(font)
        self.CriticalChance.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CriticalChance.setTextFormat(QtCore.Qt.PlainText)
        self.CriticalChance.setScaledContents(False)
        self.CriticalChance.setAlignment(QtCore.Qt.AlignCenter)
        self.CriticalChance.setWordWrap(False)
        self.CriticalChance.setObjectName("CriticalChance")
        self.CCLayout.addWidget(self.CriticalChance)
        self.CC_villain = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CC_villain.setFrameShape(QtWidgets.QFrame.Box)
        self.CC_villain.setObjectName("CC_villain")
        self.CCLayout.addWidget(self.CC_villain)
        self.StatusLabels.addLayout(self.CCLayout)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 821, 29))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.topStatus = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.topStatus.setContentsMargins(0, 0, 0, 0)
        self.topStatus.setObjectName("topStatus")
        self.HeroHPBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_4)
        self.HeroHPBar.setStyleSheet("QProgressBar{ \n"
"    border: 2px solid grey; \n"
"    border-radius: 5px; \n"
"    text-align: center \n"
"} \n"
"\n"
"QProgressBar::chunk { \n"
"    background-color: lightblue; \n"
"    width: 10px; \n"
"    margin: 1px; \n"
"} ")
        self.HeroHPBar.setProperty("value", 24)
        self.HeroHPBar.setAlignment(QtCore.Qt.AlignCenter)
        self.HeroHPBar.setInvertedAppearance(True)
        self.HeroHPBar.setObjectName("HeroHPBar")
        self.topStatus.addWidget(self.HeroHPBar)
        self.HP1 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.HP1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HP1.setObjectName("HP1")
        self.topStatus.addWidget(self.HP1)
        self.summaryTitle = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.summaryTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.summaryTitle.setObjectName("summaryTitle")
        self.topStatus.addWidget(self.summaryTitle)
        self.HP2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.HP2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HP2.setObjectName("HP2")
        self.topStatus.addWidget(self.HP2)
        self.villainHPBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_4)
        self.villainHPBar.setStyleSheet("QProgressBar{ \n"
"    border: 2px solid grey; \n"
"    border-radius: 5px; \n"
"    text-align: center \n"
"} \n"
"\n"
"QProgressBar::chunk { \n"
"    background-color: lightblue; \n"
"    width: 10px; \n"
"    margin: 1px; \n"
"} ")
        self.villainHPBar.setProperty("value", 24)
        self.villainHPBar.setAlignment(QtCore.Qt.AlignCenter)
        self.villainHPBar.setInvertedAppearance(False)
        self.villainHPBar.setObjectName("villainHPBar")
        self.topStatus.addWidget(self.villainHPBar)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(21, 300, 821, 321))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gameAndUpgradeLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gameAndUpgradeLayout.setContentsMargins(0, 0, 0, 0)
        self.gameAndUpgradeLayout.setObjectName("gameAndUpgradeLayout")
        self.gameLayout = QtWidgets.QGridLayout()
        self.gameLayout.setObjectName("gameLayout")
        self.wordInput = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordInput.sizePolicy().hasHeightForWidth())
        self.wordInput.setSizePolicy(sizePolicy)
        self.wordInput.setMinimumSize(QtCore.QSize(0, 40))
        self.wordInput.setObjectName("wordInput")
        self.gameLayout.addWidget(self.wordInput, 0, 0, 1, 1)
        self.check = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.check.setObjectName("check")
        self.gameLayout.addWidget(self.check, 0, 1, 1, 1)
        self.wordInformation = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordInformation.sizePolicy().hasHeightForWidth())
        self.wordInformation.setSizePolicy(sizePolicy)
        self.wordInformation.setFrameShape(QtWidgets.QFrame.Box)
        self.wordInformation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wordInformation.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.wordInformation.setWordWrap(True)
        self.wordInformation.setObjectName("wordInformation")
        self.gameLayout.addWidget(self.wordInformation, 1, 0, 1, 2)
        self.gameAndUpgradeLayout.addLayout(self.gameLayout, 0, 0, 1, 1)
        self.upgradeLayout = QtWidgets.QGridLayout()
        self.upgradeLayout.setObjectName("upgradeLayout")
        self.UpgradeButton4 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpgradeButton4.sizePolicy().hasHeightForWidth())
        self.UpgradeButton4.setSizePolicy(sizePolicy)
        self.UpgradeButton4.setAutoFillBackground(False)
        self.UpgradeButton4.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7;\n"
"}\n"
"")
        self.UpgradeButton4.setAutoDefault(False)
        self.UpgradeButton4.setObjectName("UpgradeButton4")
        self.upgradeLayout.addWidget(self.UpgradeButton4, 1, 1, 1, 1)
        self.UpgradeButton3 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        self.UpgradeButton3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpgradeButton3.sizePolicy().hasHeightForWidth())
        self.UpgradeButton3.setSizePolicy(sizePolicy)
        self.UpgradeButton3.setAutoFillBackground(False)
        self.UpgradeButton3.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7;\n"
"}\n"
"")
        self.UpgradeButton3.setAutoDefault(False)
        self.UpgradeButton3.setObjectName("UpgradeButton3")
        self.upgradeLayout.addWidget(self.UpgradeButton3, 1, 0, 1, 1)
        self.UpgradeButton2 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpgradeButton2.sizePolicy().hasHeightForWidth())
        self.UpgradeButton2.setSizePolicy(sizePolicy)
        self.UpgradeButton2.setAutoFillBackground(False)
        self.UpgradeButton2.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7;\n"
"}\n"
"")
        self.UpgradeButton2.setAutoDefault(False)
        self.UpgradeButton2.setObjectName("UpgradeButton2")
        self.upgradeLayout.addWidget(self.UpgradeButton2, 0, 1, 1, 1)
        self.UpgradeButton1 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpgradeButton1.sizePolicy().hasHeightForWidth())
        self.UpgradeButton1.setSizePolicy(sizePolicy)
        self.UpgradeButton1.setAutoFillBackground(False)
        self.UpgradeButton1.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f7f7f7;\n"
"}\n"
"")
        self.UpgradeButton1.setAutoDefault(False)
        self.UpgradeButton1.setObjectName("UpgradeButton1")
        self.upgradeLayout.addWidget(self.UpgradeButton1, 0, 0, 1, 1)
        self.gameAndUpgradeLayout.addLayout(self.upgradeLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT Worrier"))
        self.AP_Hero.setText(_translate("MainWindow", "TextLabel"))
        self.AttackPoint.setText(_translate("MainWindow", " AP "))
        self.AP_villain.setText(_translate("MainWindow", "TextLabel"))
        self.AC_Hero.setText(_translate("MainWindow", "TextLabel"))
        self.AvoidChance.setText(_translate("MainWindow", " AC "))
        self.AC_villain.setText(_translate("MainWindow", "TextLabel"))
        self.CC_Hero.setText(_translate("MainWindow", "TextLabel"))
        self.CriticalChance.setText(_translate("MainWindow", " CC "))
        self.CC_villain.setText(_translate("MainWindow", "TextLabel"))
        self.HeroHPBar.setFormat(_translate("MainWindow", "%p/%m"))
        self.HP1.setText(_translate("MainWindow", "HP"))
        self.summaryTitle.setText(_translate("MainWindow", "                       전투 결과 요약                       "))
        self.HP2.setText(_translate("MainWindow", "HP"))
        self.villainHPBar.setFormat(_translate("MainWindow", "%p/%m"))
        self.check.setText(_translate("MainWindow", "입력"))
        self.wordInformation.setText(_translate("MainWindow", "능력치 Button은 한번 클릭 할 때 마다   "))
        self.UpgradeButton4.setText(_translate("MainWindow", "CC증가"))
        self.UpgradeButton3.setText(_translate("MainWindow", "AC증가"))
        self.UpgradeButton2.setText(_translate("MainWindow", "HP증가"))
        self.UpgradeButton1.setText(_translate("MainWindow", "AP증가\n"
"공격력 100 상승"))

import Data.Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

