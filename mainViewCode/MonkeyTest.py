# -*- encoding:utf-8 -*-

'''P00031
 Test Android Apk by monkey
'''

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
import threading

from CoreFun.otherFun.MonkeyRun import MonkeyRun, EndMonekyrun
from View.MonkeyView_rc import Ui_MonkeyView as mv
from utils.checkDevice import checkDevices
from assets.APPlanguageinfomation import messageInfor

final_string = "test"


class MonkeyTest(mv, QDialog):
    path_signer = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MonkeyTest, self).__init__()
        self.setupUi(self)
        # self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowIcon(QIcon(messageInfor.windowIcon))

        # 定义个线程
        self.thread = MonkeyRun_Thread()
        # 先自动检查，如没有再手动检查
        self.D_SN = checkDevices()
        self.label_7.setText(self.D_SN)

        self.pushButton_3.clicked.connect(self.check_DSN)
        self.pushButton.clicked.connect(self.br_btton)
        # 运行button
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.run_order)
        self.pushButton_4.clicked.connect(self.endMonkeyPid)

        self.checkBox.stateChanged.connect(self.checkEven)
        self.checkBox_2.stateChanged.connect(self.checkEven)
        self.checkBox_3.stateChanged.connect(self.checkEven)
        self.checkBox_4.stateChanged.connect(self.checkEven)
        self.checkBox_5.stateChanged.connect(self.checkEven)
        self.checkBox_6.stateChanged.connect(self.checkEven)
        self.checkBox_7.stateChanged.connect(self.checkEven)
        self.checkBox_8.stateChanged.connect(self.checkEven)


    # Brower button
    def br_btton(self):
        text = QFileDialog.getExistingDirectory()
        if text:
            self.lineEdit_2.setText(text)
        else:
            QMessageBox.warning(self, "结果存放路径", "结果存放路径不能为空")
            self.lineEdit_2.selectAll()
            self.lineEdit_2.setFocus()

    def check_DSN(self):
        self.label_7.clear()
        self.D_SN = checkDevices()
        self.label_7.setText(self.D_SN)

    # Monkey's order
    '''
adb shell monkey -p com.huawei.solarsafe --throttle 3 --pct-touch 40 --pct-motion 25 --pct-syskeys 10 --pct-majornav 0  --pct-nav 0 --pct-trackball 0 --ignore-crashes --ignore-timeouts --ignore-native-crashes -v-v-v 10000 > D:\monkey.txt
'''

    def checkEven(self):
        event = []

        if self.lineEdit_11.text():
            order = "--throttle {}".format(self.lineEdit_11.text())
            event.append(order)
        if self.checkBox.isChecked():
            order_1 = "--pct-touch {}".format(self.lineEdit_3.text())
            event.append(order_1)
        if self.checkBox_2.isChecked():
            order_2 = "--pct-motion {}".format(self.lineEdit_4.text())
            event.append(order_2)
        if self.checkBox_3.isChecked():
            order_3 = "--pct-trackball {}".format(self.lineEdit_5.text())
            event.append(order_3)
        if self.checkBox_4.isChecked():
            order_4 = "--pct-syskeys {}".format(self.lineEdit_6.text())
            event.append(order_4)
        if self.checkBox_5.isChecked():
            order_5 = "--pct-nav {}".format(self.lineEdit_7.text())
            event.append(order_5)
        if self.checkBox_6.isChecked():
            order_6 = "--ptc-majornav {}".format(self.lineEdit_8.text())
            event.append(order_6)
        if self.checkBox_7.isChecked():
            order_7 = "--pct-appswitch {}".format(self.lineEdit_9.text())
            event.append(order_7)
        if self.checkBox_8.isChecked():
            order_8 = "--ptc-anyevent {}".format(self.lineEdit_10.text())
            event.append(order_8)

        final_order = " ".join(event)
        print(final_order)

        return final_order

    # 执行命令：

    def run_order(self):
        global final_string
        getContent = self.checkEven()
        start_order = "adb -s {0} shell monkey -p {1} ".format(self.D_SN, self.lineEdit.text())
        other_order = " --ignore-crashes --ignore-timeouts --ignore-native-crashes -v-v-v -s {0} {1} -> {2}\monkey_{3}.txt".format(
            self.lineEdit_13.text(),
            self.lineEdit_12.text()
            , self.lineEdit_2.text(), self.lineEdit.text())
        final_string = "{} {} {}".format(start_order, getContent, other_order)
        self.path_signer.emit("MonkeyRun")
        t1 = threading.Thread(target=MonkeyRun, args=(final_string,))
        t1.start()
        #self.thread.start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.label_7.clear()
            event.accept()
        else:
            event.ignore()

    # end monkey by kill monkey's pid
    def endMonkeyPid(self):
        EndMonekyrun()


#Moneky thread
from PyQt5.QtCore import QThread

class MonkeyRun_Thread(QThread):
    exec_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MonkeyRun_Thread, self).__init__()

    def run(self):
        print(final_string)
        MonkeyRun(final_string)
        self.exec_signal.emit("MonkeyEnd")
