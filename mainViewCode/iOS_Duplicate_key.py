# -*- encoding:utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from assets.APPlanguageinfomation import messageInfor
from View.iOSduplicateKeyCheckDialog_View import Ui_Dialog as duplicateKey_View
from CoreFun.InternationTest.iOSduplicateKeyCheck import iOSResDunlipcateModify as iResDupModify


class DuplicateKeyModify(duplicateKey_View, QDialog):
    pysigner = QtCore.pyqtSignal(str)

    def __init__(self):
        super(DuplicateKeyModify, self).__init__()
        self.setupUi(self)
        #self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowIcon(QIcon(messageInfor.windowIcon))

        self.pushButton.clicked.connect(self.but_1)
        self.pushButton_2.clicked.connect(self.but_2)
        self.pushButton_3.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.OK_but)

    def but_1(self):
        code_path = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(code_path)

    def but_2(self):
        result_path = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(result_path)

    def OK_but(self):
        code_path = self.lineEdit.text()
        result_path = self.lineEdit_2.text()
        if os.path.exists(code_path) and os.path.exists(result_path):
            QMessageBox.about(self, "IOS重复值正在处理", "IOS重复值正在处理, 在点击“确定”后，并等待结果")
            iResDupModify(code_path, result_path).compereDeplicateKey()

        else:
            replay = QMessageBox.warning(self, "IOS重复值正在处理", "路径设置错误， 请重新检查路径并设置", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            print(replay)
            self.pysigner.emit("No")
            self.lineEdit.selectAll()
            self.lineEdit.setFocus()
