# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manifestCheck.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_securityTest(object):
    def setupUi(self, securityTest):
        securityTest.setObjectName("securityTest")
        securityTest.resize(684, 352)
        self.gridLayoutWidget = QtWidgets.QWidget(securityTest)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 671, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.browserfile = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.browserfile.setFont(font)
        self.browserfile.setObjectName("browserfile")
        self.gridLayout.addWidget(self.browserfile, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(securityTest)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 671, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.interface_textEdit = QtWidgets.QLineEdit(self.groupBox)
        self.interface_textEdit.setGeometry(QtCore.QRect(100, 30, 401, 31))
        self.interface_textEdit.setObjectName("interface_textEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.setCode_button = QtWidgets.QPushButton(self.groupBox)
        self.setCode_button.setGeometry(QtCore.QRect(530, 30, 81, 31))
        self.setCode_button.setObjectName("setCode_button")
        self.interface_textEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.interface_textEdit_2.setGeometry(QtCore.QRect(100, 90, 401, 31))
        self.interface_textEdit_2.setObjectName("interface_textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label_3.setObjectName("label_3")
        self.setResult_button = QtWidgets.QPushButton(self.groupBox)
        self.setResult_button.setGeometry(QtCore.QRect(530, 90, 81, 31))
        self.setResult_button.setObjectName("setResult_button")
        self.startSearch_button = QtWidgets.QPushButton(self.groupBox)
        self.startSearch_button.setGeometry(QtCore.QRect(520, 140, 131, 31))
        self.startSearch_button.setObjectName("startSearch_button")

        self.retranslateUi(securityTest)
        QtCore.QMetaObject.connectSlotsByName(securityTest)

    def retranslateUi(self, securityTest):
        _translate = QtCore.QCoreApplication.translate
        securityTest.setWindowTitle(_translate("securityTest", "Dialog"))
        self.browserfile.setText(_translate("securityTest", "选 择"))
        self.label.setText(_translate("securityTest", "ManifestChek"))
        self.pushButton_2.setText(_translate("securityTest", "执 行"))
        self.groupBox.setTitle(_translate("securityTest", "Interface Search（Android）"))
        self.label_2.setText(_translate("securityTest", "Code Addr."))
        self.setCode_button.setText(_translate("securityTest", "Select"))
        self.label_3.setText(_translate("securityTest", "Result Addr."))
        self.setResult_button.setText(_translate("securityTest", "Select"))
        self.startSearch_button.setText(_translate("securityTest", "START SEARCH"))

