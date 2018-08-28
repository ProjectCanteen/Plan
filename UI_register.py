# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zzy\Desktop\file\食堂点餐系统v0.5\GUI\canteen.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(335, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(120, 330, 112, 34))
        self.login.setObjectName("login")
        self.id_p = QtWidgets.QLabel(self.centralwidget)
        self.id_p.setGeometry(QtCore.QRect(20, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.id_p.setFont(font)
        self.id_p.setObjectName("id_p")
        self.passw = QtWidgets.QLabel(self.centralwidget)
        self.passw.setGeometry(QtCore.QRect(50, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.passw.setFont(font)
        self.passw.setObjectName("passw")
        self.id_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(110, 40, 181, 25))
        self.id_input.setObjectName("id_input")
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(110, 80, 181, 25))
        self.pass_input.setObjectName("pass_input")
        self.iden = QtWidgets.QLabel(self.centralwidget)
        self.iden.setGeometry(QtCore.QRect(80, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.iden.setFont(font)
        self.iden.setObjectName("iden")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(120, 210, 99, 24))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.modify = QtWidgets.QPushButton(self.centralwidget)
        self.modify.setGeometry(QtCore.QRect(120, 290, 112, 34))
        self.modify.setObjectName("modify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 30))
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
        self.login.setText(_translate("MainWindow", "登录"))
        self.id_p.setText(_translate("MainWindow", "用户名："))
        self.passw.setText(_translate("MainWindow", "密码："))
        self.iden.setText(_translate("MainWindow", "请选择您的登陆身份"))
        self.comboBox.setItemText(0, _translate("MainWindow", "普通用户"))
        self.comboBox.setItemText(1, _translate("MainWindow", "厨师"))
        self.comboBox.setItemText(2, _translate("MainWindow", "管理员"))
        self.modify.setText(_translate("MainWindow", "修改密码"))

