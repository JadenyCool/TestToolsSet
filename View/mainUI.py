# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel, QDialog
from PyQt5.QtGui import QIcon

from View import iOScheckLagConfig_View_old as iosConfig


class mainUI(QWidget):

    def __init__(self):
        super(mainUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FusionSolar Test Tools")
        self.setGeometry(500, 250, 300, 220)

        # 设置窗口大小，并禁止窗口最大化
        self.setFixedSize(760, 550)

        # label
        self.label1 = QLabel(self)
        self.label1.setText("Name:")
        # setGeometry的4个参数: （label在窗口中的位置x, y, lable自身的宽，高）
        self.label1.setGeometry(300, 60, 60, 10)
        self.label1.setStyleSheet("font: 75 12pt \"Agency FB\";\n"
                                  "font: 75 9pt \"微软雅黑\";")

        # text
        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(500, 50, 150, 30)

        # button
        self.button1 = QPushButton(self)
        self.button1.setText("Test")
        self.button1.setGeometry(60, 100, 100, 30)
        self.button1.clicked.connect(self.showMessage)

        # button2
        self.but_iosCheck = QPushButton(self)
        self.but_iosCheck.setText("Test1")
        self.but_iosCheck.setGeometry(170, 100, 100, 30)
        self.but_iosCheck.clicked.connect(self.iOSChineseCheck)

        # button3
        self.but_about = QPushButton(self)
        self.but_about.setText("About")
        self.but_about.setGeometry(200, 150, 100, 30)
        self.but_about.clicked.connect(self.new_about)

    def iOSChineseCheck(self):
        # getText = self.text.text()
        # if getText == "1":
        #     iosCheck.main()
        # else:
        #     print("test is fail")
        self.dialog = iosConfig.Ui_iOSInternationalTest()
        self.dialog.mySignal.connect(self.getSignalData)

    def getSignalData(self, codePath, resultPath, testLag):
        c_path = codePath
        r_path = resultPath
        t_lang = testLag
        print(c_path, r_path, t_lang)

    def showMessage(self):
        getText = self.text.text()
        print(getText)
        if getText == "gulinjie":
            QMessageBox.information(self, "成功", "测试成功", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            self.text.setFocus()
        else:
            QMessageBox.warning(self, "失败", "测试失败", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            self.text.clear()
            self.text.setFocus()

    def About(self):
        pass
        # self.about = About_rc.Ui_About()
        # self.about.show()

    def new_about(self):
        QMessageBox.about(self, "关于",
                          ''' FusionSolar APP测试，功能点如下
                          1、iOS国际化检查：该功能只检查iOS中各语言是否包含了还有中文显示，并生成excel结果
                          2、Bug超期检查:检查当前Bug超过1周依然未解决的列表，并以邮件的方式发出
                          3、其它''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainUI = mainUI()
    MainUI.show()
    sys.exit(app.exec_())
