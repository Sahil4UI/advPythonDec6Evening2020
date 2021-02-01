# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 472)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 261, 51))
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 261, 51))
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(380, 140, 82, 31))
        self.radioButton.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(470, 140, 82, 31))
        self.radioButton_2.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 220, 161, 51))
        self.pushButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 611, 351))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 401, 331))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../tictactoe.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(38, 35, 111, 91))
        self.pushButton_2.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(38, 141, 111, 91))
        self.pushButton_3.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(38, 247, 111, 91))
        self.pushButton_4.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(167, 247, 111, 91))
        self.pushButton_5.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(168, 141, 111, 91))
        self.pushButton_6.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(168, 35, 111, 91))
        self.pushButton_7.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(294, 247, 111, 91))
        self.pushButton_8.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(294, 141, 111, 91))
        self.pushButton_9.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(294, 36, 111, 91))
        self.pushButton_10.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(470, 20, 111, 51))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(450, 70, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
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
        self.label.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.label_2.setText(_translate("MainWindow", "Choose X or 0 :"))
        self.radioButton.setText(_translate("MainWindow", "0"))
        self.radioButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "START GAME"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_7.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_8.setText(_translate("MainWindow", "9"))
        self.label_4.setText(_translate("MainWindow", "WINNER"))
        self.frame.hide()
        self.initEvents()
        
    def initEvents(self):
            self.pushButton.clicked.connect(self.StartGame)
            
            self.user_btns = [self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5,
                         self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9,self.pushButton_10]
            self.cpu_btns = self.user_btns.copy()
            
            for btn in self.user_btns:
                btn.clicked.connect(self.user_move)
                
        
            
    def user_move(self):
            btn=self.sender()
            btn.setDisabled(True)
            btn.setText(self.user_ch)
            self.cpu_btns.remove(btn)
            res=self.checkWinner(self.user_ch)
            if res=="winner":
                self.lineEdit.setText("User wins")
            self.cpu_move()
            
    def checkWinner(self,choice):
        self.combinations= [
            [self.pushButton_2,self.pushButton_7,self.pushButton_10],
            [self.pushButton_3,self.pushButton_6,self.pushButton_9],
            [self.pushButton_4,self.pushButton_5,self.pushButton_8],
            [self.pushButton_2,self.pushButton_3,self.pushButton_4],
            [self.pushButton_7,self.pushButton_6,self.pushButton_5],
            [self.pushButton_10,self.pushButton_9,self.pushButton_8],
            [self.pushButton_2,self.pushButton_6,self.pushButton_8],
            [self.pushButton_10,self.pushButton_6,self.pushButton_4]
        ]
        
        for i in self.combinations:
            if i[0].text()==choice and i[1].text()==choice and i[2].text()==choice:
                return "winner" 
   
        
    def StartGame(self):
            if self.radioButton.isChecked():
                self.user_ch=self.radioButton.text()
                self.cpu_ch=self.radioButton_2.text()
            elif self.radioButton_2.isChecked():
                self.user_ch=self.radioButton_2.text()
                self.cpu_ch=self.radioButton.text()
            print(self.user_ch,self.cpu_ch)
            
            self.frame.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
