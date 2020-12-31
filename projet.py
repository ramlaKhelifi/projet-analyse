# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1372, 800)
        MainWindow.setStyleSheet("*{\n"
"font: 87 12pt \"Cooper Std Black\";\n"
"color:rgb(0, 0, 0);\n"
" \n"
"\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QPushButton#pushButton_3{\n"
"border-image: url(:/img/btn2.png);\n"
"border:0;\n"
"background:0;\n"
"\n"
"}\n"
"QPushButton#pushButton_4{\n"
"border-image: url(:/img/btn2.png);\n"
"border:0;\n"
"background:0;\n"
"\n"
"}\n"
"QPushButton#pushButton_5{\n"
"border-image: url(:/img/btn2.png);\n"
"border:0;\n"
"background:0;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton{\n"
"border-image: url(:/img/btn2.png);\n"
"border:0;\n"
"background:0;\n"
"\n"
"}\n"
"QPushButton#pushButton_2{\n"
"border-image: url(:/img/btn2.png);\n"
"border:0;\n"
"background:0;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QPushButton#pushButton_4:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QPushButton#pushButton_5:pressed{\n"
"\n"
"    border-image: url(:/img/btn3.png);\n"
"\n"
" }\n"
"\n"
"QMainWindow{\n"
"border-image: url(:/img/602.png);\n"
"\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 520, 241, 51))
        self.pushButton_2.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/sta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 590, 241, 51))
        self.pushButton_3.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../../../les interfaces1/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 50, 181, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 340, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 390, 55, 61))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 170, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Std Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 250, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 400, 241, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 330, 241, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(499, 139, 611, 581))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet Python"))
        self.pushButton_2.setText(_translate("MainWindow", "calculer"))
        self.pushButton_3.setText(_translate("MainWindow", "quitter"))
        self.pushButton_5.setText(_translate("MainWindow", "Effacer"))
        self.label_2.setText(_translate("MainWindow", "Fonction"))
        self.label_3.setText(_translate("MainWindow", "a"))
        self.label_4.setText(_translate("MainWindow", "b"))
        self.comboBox.setItemText(0, _translate("MainWindow", "point fixe"))
        self.comboBox.setItemText(1, _translate("MainWindow", "rectangle gauche"))
        self.label_5.setText(_translate("MainWindow", "Méthode"))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

