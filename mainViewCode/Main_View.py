# -*- encoding:utf-8 -*-

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox

from CoreFun.Log import OutPut as ot
from View.MainView_rc import Ui_TestTools
from assets.APPlanguageinfomation import messageInfor
# from mainViewCode.IOSCheckLangConfig_old import iOSCheckConf
from mainViewCode.IOSTranslationCheck import iOSCheckConf
from mainViewCode.MonkeyTest import MonkeyTest, MonkeyRun_Thread
from mainViewCode.SecurityCheck.androidSecurity import securityCheck
from mainViewCode.iOS_Duplicate_key import DuplicateKeyModify
from mainViewCode.InternationTest.InternationReplace import transReplace

class ToolMainWindow(Ui_TestTools, QMainWindow):
    def __init__(self):
        super(ToolMainWindow, self).__init__()
        self.setupUi(self)
        self.textEdit.setReadOnly(True)
        #self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowIcon(QIcon(messageInfor.windowIcon))
        self.setWindowTitle("APP测试工具")

        self.ioscheck_config = iOSCheckConf()
        self.ios_duplicate_key = DuplicateKeyModify()
        self.monkey_test = MonkeyTest()
        self.monThread = MonkeyRun_Thread()
        self.maniTest = securityCheck()
        self.transReplace_iOS = transReplace()


        # menu bar各功能事件
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)
        self.actionQuite.triggered.connect(self.close)
        # 下面将输出重定向到textEdit中
        sys.stderr = ot.EmittingStream(textWritten=self.outputWritten)
        sys.stdout = ot.EmittingStream(textWritten=self.outputWritten)



        # button事件
        self.pushButton.clicked.connect(self.ioscheck_config.show)
        self.pushButton_2.clicked.connect(self.ios_duplicate_key.show)
        self.pushButton_4.clicked.connect(self.monkey_test.show)
        self.pushButton_5.clicked.connect(self.maniTest.show)
        self.pushButton_3.clicked.connect(self.transReplace_iOS.show)

        # 信号点
        self.ios_duplicate_key.pysigner.connect(self.test)
        self.monkey_test.path_signer.connect(self.test)


        self.monThread.exec_signal.connect(self.test)

    def test(self, string):
        if string == "No":
            self.statusbar.showMessage("正在执行：文件重复Key检查")
        elif string == "MonkeyRun":
            self.statusbar.showMessage("正在进行Monkey测试.......")
        elif string == "MonkeyEnd":
            self.statusbar.showMessage("Monkey 测试已完成！")

    def but_2(self):
        self.textEdit.clear()
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "输入IOS代码地址：")
        if ok:
            self.textEdit.setText(text)

    def help(self):

        QMessageBox.about(self, "帮助", "{}".format(messageInfor.help_infor))

    def about(self):
        QMessageBox.about(self, "关于", messageInfor.about_infor)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showmessage(self):
        QMessageBox.information(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     ui = ToolMainWindow()
#     ui.show()
#     sys.exit(app.exec_())
