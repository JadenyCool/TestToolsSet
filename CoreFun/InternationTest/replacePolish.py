# -*- encoding:utf-8 -*-
# Author: Gulinjie


# According to HUAWEI's document to modify "Localizable.strings" files
# Table's format will be modified by manual before running this , such as: A:A -> Chinese; B:B -> English; C:C -> Japan;


import os
import openpyxl
from utils.FindFiles import findFiles
import string


class InterReplace:
    def __init__(self, excel_file, codepath, goalOS, Excelcoloum, file_abbreviated, excel_row_start):
        '''excel_start: start location in excel file
        excel_file: international translation file;
        codepath: code path which android or iOS
        goalIOS:  android or ios, if iOS, we will replace *.string resource file , otherwise, android files will replace
        Excelcoloum: Will replace international language which one column in excel
        file_abbreviated: will find file which replace language file in code path, such as : pl -> Polish; fr -> French as so on
        excel_row_start: Start which one row in excel'''
        global excelStart, cpath
        excelStart = int(excel_row_start) - 1  # start in 1 row

        if os.path.exists(excel_file):
            self.InterationExcelFile = excel_file
        else:
            print("Sorry, File path is not exist, please ensure that again")

        if not goalOS and not Excelcoloum and not excel_row_start and not file_abbreviated:
            print("cannot be empty!!!!")
        self.fileAbbr = file_abbreviated.strip()
        self.goalOS = goalOS
        self.excelColoum = Excelcoloum - 1  # start in 1 column

        cpath = codepath

    def ReadInterFileContent(self):

        openfile = openpyxl.load_workbook(self.InterationExcelFile)
        getSheetName = openfile.get_sheet_by_name("String")

        EngDit = {}
        tmpChineseList = []
        tmpEnglistList = []

        # get chinese
        for ChinseCol in list(getSheetName.columns)[0]:
            tmpChineseList.append(ChinseCol.value)
        print(tmpChineseList)

        # get English value
        for Engcol in list(getSheetName.columns)[1]:
            tmpEnglistList.append(Engcol.value)

        englistList = tmpEnglistList[excelStart::1]
        chineseList = tmpChineseList[excelStart::1]

        # get Polish
        PolishList = []
        tmpPolish = []
        for Polish in list(getSheetName.columns)[self.excelColoum]:
            value = Polish.value
            tmpPolish.append(value)
        PolishList = tmpPolish[excelStart::1]

        # all languages -> dict
        PolishDict = {}

        for i in range(len(chineseList)):
            PolishDict.update({chineseList[i]: PolishList[i]})
            # EngDit.update({chineseList[i]: englistList[i]})

        return PolishDict


   # accroding to ios or android to read goal files
    def getReplaceFiles(self):
        '''get to search files convert a dict
        :return a dict needReplaceStringFiles'''

        selectCondition = ["Utility", "Base.lproj", "en-GB.lproj", "zh-Hans"]
        getNewStringfiles = []
        reciverResult = findFiles(filename="Localizable", codePath=cpath).serachFilebyFileName(key1=".strings")
        for i in range(len(reciverResult)):
            if "Utility" in reciverResult[i]:
                pass
            elif "Base.lproj" in reciverResult[i]:
                pass
            elif "en-GB.lproj" in reciverResult[i]:
                pass
            elif "zh-Hans" in reciverResult[i]:
                pass
            else:
                getNewStringfiles.append(reciverResult[i])

        print("*" * 80)
        needReplaceStringFiles = {}
        for j in range(len(getNewStringfiles)):
            VarityLanguageName = getNewStringfiles[j].split(".")[0].split("\\")[-1]

            needReplaceStringFiles.update({VarityLanguageName: getNewStringfiles[j]})
        # print(needReplaceStringFiles)
        return needReplaceStringFiles

    def replaceTranslateLanguage(self):
        PolishReplace = self.ReadInterFileContent()
        ReplaceFilesPath = self.getReplaceFiles()
        translatecontent = {
            # "en": englishReplace,
            # "nl": DutchReplace,
            # "de": GermanReplace,
            # "it": ItalianReplace,
            # "ja": JapanReplace,
            # "pt": PortuguesesReplace,
            # 'fr': FrenchReplace,
            '{}'.format(self.fileAbbr): PolishReplace
        }
        tempDict = {}
        afterReplaceDict = {}
        AReplaceList = []

        for trconKey, trconValue in translatecontent.items():
            for reKey, revalue in ReplaceFilesPath.items():

                if trconKey == reKey:
                    print("Replacing {} file".format(trconKey))
                    with open(revalue, "r", encoding="utf-8") as f:
                        # print(revalue)
                        for line in f:
                            resoucefileKey = line.split("=")[0].replace('"', "").rstrip()

                            if len(line.split("=")) > 1:
                                resoucefilevalue = line.split("=")[1].replace('"', "").rstrip()
                                tempDict.update({resoucefileKey: resoucefilevalue})

                    # 开始替换
                    for tempKey, tempValue in tempDict.items():
                        for huaweiKey, huaweiValue in trconValue.items():
                            # print(huaweiKey, huaweiValue)
                            # 去掉结尾的冒号： Colon: 冒号

                            if tempKey.endswith(":"):
                                tempKeyColon = tempKey.strip(string.punctuation)

                            else:
                                tempKeyColon = tempKey
                            if tempKeyColon == huaweiKey and huaweiValue is not None:
                                if tempKey.endswith(':'):
                                    newHuaweiKey = huaweiValue + ":"
                                    afterReplaceDict.update({tempKey: newHuaweiKey})
                                    break
                                else:
                                    afterReplaceDict.update({tempKey: huaweiValue})
                            else:
                                afterReplaceDict.update({tempKey: tempValue})
                    tempDict.clear()

                    # print(len(afterReplaceDict))
                    for afterRepKey, afterRepValue in afterReplaceDict.items():
                        removefenhao = afterRepValue.replace(";", "")
                        line = '"{}"="{}";'.format(afterRepKey, removefenhao)
                        AReplaceList.append(line)
                        # print(AReplaceList)
                    print(AReplaceList)
                    afterReplaceDict.clear()

                    print(len(AReplaceList))
                    with open(revalue, 'w+', encoding="utf-8") as fw:
                        print(revalue)
                        for n in range(len(AReplaceList)):
                            fw.write(AReplaceList[n] + "\n")
                    AReplaceList.clear()
                    print("{}-> translation is OK !".format(trconKey))


if __name__ == "__main__":
    # filepath = "D:\ddd\PVMS830+UI+String-Polish.xlsx"
    # codepath = "D:\Code\IOS\iCleanPower"
    # # InterReplace(filepath, excel_start=1584).ReadInterFileContent()
    # InterReplace(filepath, 2, codepath).replaceTranslateLanguage()

    # filepath = "D:\ddd\PVMS830+UI+String-all.xlsx"
    filepath = "D:/ddd/7tran/tranOne/tranOne.xlsx"
    codepath = "D:/Code/fusionsolar_7/iCleanPower"
    # InterReplace(filepath, excel_start=1584).ReadInterFileContent()
    InterReplace(excel_file=filepath, codepath=codepath, goalOS='ios', Excelcoloum=6, file_abbreviated='ja',
                 excel_row_start=2).replaceTranslateLanguage()

