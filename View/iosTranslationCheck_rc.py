# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iosTranslationCheck.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_iOSInternationalTest(object):
    def setupUi(self, iOSInternationalTest):
        iOSInternationalTest.setObjectName("iOSInternationalTest")
        iOSInternationalTest.resize(632, 439)
        iOSInternationalTest.setMinimumSize(QtCore.QSize(0, 13))
        self.label = QtWidgets.QLabel(iOSInternationalTest)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(iOSInternationalTest)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 581, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 15))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.but_sure = QtWidgets.QPushButton(iOSInternationalTest)
        self.but_sure.setGeometry(QtCore.QRect(60, 360, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.but_sure.setFont(font)
        self.but_sure.setObjectName("but_sure")
        self.but_cancel = QtWidgets.QPushButton(iOSInternationalTest)
        self.but_cancel.setGeometry(QtCore.QRect(370, 360, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.but_cancel.setFont(font)
        self.but_cancel.setObjectName("but_cancel")

        self.retranslateUi(iOSInternationalTest)
        QtCore.QMetaObject.connectSlotsByName(iOSInternationalTest)

    def retranslateUi(self, iOSInternationalTest):
        _translate = QtCore.QCoreApplication.translate
        iOSInternationalTest.setWindowTitle(_translate("iOSInternationalTest", "iOS-国际化测试配制"))
        self.label.setText(_translate("iOSInternationalTest", "iOS国际化测试配制信息"))
        self.pushButton_2.setText(_translate("iOSInternationalTest", "浏览"))
        self.pushButton.setText(_translate("iOSInternationalTest", "浏览"))
        self.label_2.setText(_translate("iOSInternationalTest", "IOS代码路径："))
        self.label_4.setText(_translate("iOSInternationalTest", "国际化语言缩写："))
        self.label_3.setText(_translate("iOSInternationalTest", "测试输出结果路径："))
        self.lineEdit_3.setPlaceholderText(_translate("iOSInternationalTest", "such as: pl, es, fr, ....."))
        self.but_sure.setText(_translate("iOSInternationalTest", "开始检查"))
        self.but_cancel.setText(_translate("iOSInternationalTest", "取 消"))
