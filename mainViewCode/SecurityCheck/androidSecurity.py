# -*- encoding:utf-8 -*-

'''^^^^^^^^^^^^^^^^^^^^^----------------------^^^^^^^^^^^^^^^^^^^^^^^^^
manifest.xml for security check
'''

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from assets.APPlanguageinfomation import messageInfor
from View.manifestCheck_rc import Ui_securityTest
from CoreFun.securityTest.MainifestCheck import ManifestCheck as mTest
from CoreFun.securityTest.interfaceSearchForAndroid import searchAndroidInterface as SAndrInterface

class securityCheck(Ui_securityTest, QDialog):

    def __init__(self):
        super(securityCheck, self).__init__()
        self.setupUi(self)
        #self.setWindowIcon(QIcon(".\\assets\\testTools.ico"))
        self.setWindowTitle("Android安全辅助工具")
        self.setWindowIcon(QIcon(messageInfor.windowIcon))

        self.browserfile.clicked.connect(self.bowserManifestFile)
        self.pushButton_2.clicked.connect(self.runCheck)
        self.pushButton_2.clicked.connect(self.hide)

        self.setCode_button.clicked.connect(self.setCodePath)
        self.setResult_button.clicked.connect(self.setResultPath)
        self.startSearch_button.clicked.connect(self.searchBut)
        self.startSearch_button.clicked.connect(self.hide)

    def bowserManifestFile(self):
        #getfile = QFileDialog.getOpenFileName(filter="*.xml")
        fileName, getfile = QFileDialog.getOpenFileName(self, "选择文件", "/", filter="*.xml")
        print(fileName)
        self.lineEdit.setText(fileName)

    def runCheck(self):
        getpath = self.lineEdit.text()
        if getpath:
            mTest(getpath).manifestSecurityCheck()
        else:
            QMessageBox.warning(self, "文件选择提醒", "未选择manifest.xml文件，请重新选择")

    def setCodePath(self):
        getCodePath = QFileDialog.getExistingDirectory()
        self.interface_textEdit.setText(getCodePath)


    def setResultPath(self):
        getResultPath = QFileDialog.getExistingDirectory()
        self.interface_textEdit_2.setText(getResultPath)

    def searchBut(self):
        codePath = self.interface_textEdit.text()
        resPath = self.interface_textEdit_2.text()

        if codePath and resPath:
            SAndrInterface(codePath=codePath, resPath=resPath).run()
        else:
            QMessageBox.warning(self, "Execute Tips", "Sorry! 'code Addr.' or 'res Addr.' cannot be empty")

