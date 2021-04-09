# -*- encoding:utf-8 -*-

import os
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QDialog, QFileDialog
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from assets.APPlanguageinfomation import messageInfor
from View.iOScheckLagConfig_View_old import Ui_iOSInternationalTest as language_Test_view
from CoreFun.InternationTest import IOSChineseKeyCheck as iOSCheck


class iOSCheckConf(language_Test_view, QDialog):
    def __init__(self):
        super(iOSCheckConf, self).__init__()
        self.setupUi(self)
        #self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowIcon(QIcon(messageInfor.windowIcon))

        # button事件：

        self.pushButton.clicked.connect(self.browerCode)
        self.pushButton_2.clicked.connect(self.browerResult)
        self.but_sure.clicked['bool'].connect(self.hide)
        self.but_sure.clicked['bool'].connect(self.sure_but)
        # self.but_sure.clicked['bool'].connect(iOSInternationalTest.hide)
        self.but_cancel.clicked['bool'].connect(self.close)

        # CheckBox_lag
        self.checkBox.stateChanged.connect(self.selectBox_lag)
        self.checkBox_2.stateChanged.connect(self.selectBox_lag)
        self.checkBox_3.stateChanged.connect(self.selectBox_lag)
        self.checkBox_4.stateChanged.connect(self.selectBox_lag)
        self.checkBox_5.stateChanged.connect(self.selectBox_lag)
        self.checkBox_6.stateChanged.connect(self.selectBox_lag)
        self.checkBox_7.stateChanged.connect(self.selectBox_lag)
        self.checkBox_8.stateChanged.connect(self.selectBox_lag)
        self.checkBox_9.stateChanged.connect(self.selectBox_lag)
        self.checkBox_10.stateChanged.connect(self.selectBox_lag)

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

        # 复选择框的处理Qt.Checked

    def selectBox_lag(self):
        lag_box = []

        if self.checkBox.isChecked():
            lag_box.append("pl")
        if self.checkBox_2.isChecked():
            lag_box.append("en")
        if self.checkBox_3.isChecked():
            lag_box.append("de")
        if self.checkBox_4.isChecked():
            lag_box.append("fr")
        if self.checkBox_5.isChecked():
            lag_box.append("xb")
        if self.checkBox_6.isChecked():
            lag_box.append("pt")
        if self.checkBox_7.isChecked():
            lag_box.append("it")
        if self.checkBox_8.isChecked():
            lag_box.append("ja")
        if self.checkBox_9.isChecked():
            lag_box.append("nl")
        if self.checkBox_10.isChecked():
            lag_box.append("er")

        else:
            pass
            # QMessageBox.about(self, "选择", "没选中了", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return lag_box

        # 开始执行按钮事件

    def sure_but(self):
        code_path = self.lineEdit.text()
        result_path = self.lineEdit_2.text()
        lag_list = self.selectBox_lag()
        if os.path.exists(code_path) and os.path.exists(result_path):
            if lag_list:
                QMessageBox.information(self, "运行", "iOS国际化测试：{}, 正在运行检查，请稍后查看结果".format(lag_list),
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                iOSCheck.iOSchinesecheck(code_path, result_path, lag_list).main()
            else:
                QMessageBox.warning(self, "参数配制不正确", "请选择需要测试的语言")
        else:
            QMessageBox.warning(self, "路径设置不正确", "请设置正确的路径")
