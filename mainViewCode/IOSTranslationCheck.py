# -*- encoding:utf-8 -*-

import os
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QDialog, QFileDialog
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from assets.APPlanguageinfomation import messageInfor
# from View.iOScheckLagConfig_View_old import Ui_iOSInternationalTest as language_Test_view
from CoreFun.InternationTest import IOSChineseKeyCheck as iOSCheck
from View.iosTranslationCheck_rc import Ui_iOSInternationalTest as IOS_Translate_Test_View
import re


class iOSCheckConf(IOS_Translate_Test_View, QDialog):
    def __init__(self):
        super(iOSCheckConf, self).__init__()
        self.setupUi(self)
        # self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowIcon(QIcon(messageInfor.windowIcon))

        # button事件：

        self.pushButton.clicked.connect(self.browerCode)
        self.pushButton_2.clicked.connect(self.browerResult)


        self.but_sure.clicked['bool'].connect(self.hide)

        self.but_sure.clicked['bool'].connect(self.sure_but)
        # self.but_sure.clicked['bool'].connect(iOSInternationalTest.hide)
        self.but_cancel.clicked['bool'].connect(self.close)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        # 浏览Code文件

    def browerCode(self):
        apppath = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(apppath)

        # 浏览Code文件

    def browerResult(self):
        resultPath = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(resultPath)

        # 开始执行按钮事件

    def sure_but(self):
        code_path = self.lineEdit.text()
        result_path = self.lineEdit_2.text()

        TestLanguage = self.lineEdit_3.text()
        # 将用户所输入的转成列表：
        # 用户输入的信息为：fr, es, pl , nl, de
        # [fr, es, pl, nl, de]
        language_List = re.sub(" ", "", TestLanguage).split(",")

        if os.path.exists(code_path) and os.path.exists(result_path):
            if language_List:
                QMessageBox.information(self, "运行", "iOS国际化测试：{}, 正在运行检查，请稍后查看结果".format(language_List),
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                iOSCheck.iOSchinesecheck(code_path, result_path, language_List).main()
            else:
                QMessageBox.warning(self, "参数配制不正确", "请输入要测试的语言")
        else:
            QMessageBox.warning(self, "路径设置不正确", "请设置正确的路径")
