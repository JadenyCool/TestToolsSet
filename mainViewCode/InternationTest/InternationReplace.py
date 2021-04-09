# -*- encoding:utf-8 -*-

import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from CoreFun.InternationTest.InternationLagReplace import InterReplace as iOSInterReplace
from View.TranslationReplaceView_rc import Ui_Translation
from assets.APPlanguageinfomation import messageInfor

codePath = "D:\code"
huaweiExcel = "D:\\test.xlsx"
startLineNo = 1139


class transReplace(Ui_Translation, QDialog):
    def __init__(self):
        super(transReplace, self).__init__()
        self.setupUi(self)

        self.iOSReplaceThread = iOSReplaceThread()

        self.setWindowTitle("国际化翻译替换")
        self.setWindowIcon(QIcon(messageInfor.windowIcon))
        self.code_but.clicked.connect(self.codePathSelect)
        self.excel_but.clicked.connect(self.huaweiTranExcel)
        self.pushButton.clicked['bool'].connect(self.RunReplace)

    def codePathSelect(self):
        cPathSelect = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(cPathSelect)

    def huaweiTranExcel(self):
        huaweiexcelName, gethuaweiExcel = QFileDialog.getOpenFileName(self, "选择翻译文件xlsx", "/", filter="*.xlsx")
        self.lineEdit_2.setText(huaweiexcelName)
        print("You chose file is {}".format(huaweiexcelName))

    def RunReplace(self):
        global codePath, huaweiExcel, startLineNo, targetOS, file_abbreviated, Excelcoloum
        startLineNo = self.lineEdit_3.text()
        codePath = self.lineEdit.text()
        targetOS = self.lineEdit_5.text()
        file_abbreviated = self.lineEdit_6.text()
        Excelcoloum = self.lineEdit_4.text()
        huaweiExcel = self.lineEdit_2.text()
        if os.path.exists(codePath) and os.path.exists(huaweiExcel):
            if startLineNo:
                self.iOSReplaceThread.start()
                # QMessageBox.information(self, "参数设置", "请输入Huawei 翻译excel中需要替换翻译的起始行", QMessageBox.Yes | QMessageBox.No,
                #                         QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "参数设置", "Huawei翻译方文档起始行必须是数字,且代码路径与excel文档路径不能为空",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        # if startLineNo:
        #     self.iOSReplaceThread.run()
        # else:
        #         QMessageBox.information(self, "参数设置", "请输入Huawei 翻译excel中需要替换翻译的起始行", QMessageBox.Yes | QMessageBox.No,
        #                                 QMessageBox.Yes)
        # else:
        #     QMessageBox.information(self, "参数设置", "Huawei翻译方文档起始行必须是数字,且代码路径与excel文档路径不能为空",
        #                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        #     self.lineEdit.selectAll()


from PyQt5.QtCore import QThread


class iOSReplaceThread(QThread):
    def __init__(self):
        super(iOSReplaceThread, self).__init__()

    def run(self):
        iOSInterReplace(codepath=codePath, excel_file=huaweiExcel, goalOS=targetOS, Excelcoloum=Excelcoloum,
                        file_abbreviated=file_abbreviated, excel_row_start=startLineNo, ).replaceTranslateLanguage()
