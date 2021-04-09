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
        self.excelColoum = int(Excelcoloum) - 1  # start in 1 column

        cpath = codepath

    def ReadExcel(self):

        openfile = openpyxl.load_workbook(filename=self.InterationExcelFile, data_only=True)
        getSheetName = openfile.get_sheet_by_name("String")

        excelChineseList = []
        excel_chinese_key_List = []

        # 读取excel中的中文
        excelChiKeyfuhao = ["。", ":", "：", ".", ";"]
        for ChineseCol in list(getSheetName.columns)[0]:
            Ckey_value = ChineseCol.value
            for i in range(len(excelChiKeyfuhao)):
                if Ckey_value.endswith("{}".format(excelChiKeyfuhao[i])):
                    Ckey_value = Ckey_value.replace("{}".format(excelChiKeyfuhao[i]), "")
                    print(Ckey_value)
                    break

            excelChineseList.append(Ckey_value)

        # 将中文词条添加的ChineseList中
        excel_chinese_key_List = excelChineseList[excelStart::1]
        # print(excel_chinese_key_List)

        # 获取excel表中的国际化语言
        excelTransKeyfuhao = ["。", ":", "：", ".", ";"]
        excel_Translation_key = []
        for excel_translate in list(getSheetName.columns)[self.excelColoum]:
            excel_value = excel_translate.value
            if excel_value is None:
                excel_value = "Jerry"
            for j in range(len(excelTransKeyfuhao)):
                if excel_value.endswith("{}".format(excelTransKeyfuhao[j])):
                    excel_value = excel_value.replace('{}'.format(excelTransKeyfuhao[j]), "")
                    break

        excel_translate_key_list = excel_Translation_key[excelStart::1]

        print(len(excel_translate_key_list))

        # all languages -> dict
        excel_chi_otherLang = {}

        for i in range(len(excel_translate_key_list)):
            excel_chi_otherLang.update({excel_chinese_key_List[i]: excel_translate_key_list[i]})
        print(len(excel_chi_otherLang))

        return excel_chi_otherLang

    # 查询代码中的国际化.string结尾的文件， 并获取该文件的内容
    def readCodeString(self):
        '''get to search files convert a dict
        :return a dict needReplaceStringFiles'''

        # selectCondition = ["Utility", "Base.lproj", "en-GB.lproj", "zh-Hans"]
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
        # 从代码中读取需要替换的国际化文件的名称，如：en -> 对应的文件路径
        for j in range(len(getNewStringfiles)):
            VarityLanguageName = getNewStringfiles[j].split(".")[0].split("\\")[-1]

            needReplaceStringFiles.update({VarityLanguageName: getNewStringfiles[j]})
        # print(needReplaceStringFiles)
        return needReplaceStringFiles

    # 做文件替换工作
    def replaceTranslateLanguage(self):
        Excelcontent = self.ReadExcel()  # 读取 excel 表中的国际化内容

        CodeReplaceFilesPath = self.readCodeString()
        FromUserfileAbbr = {
            # "en": englishReplace,
            # "nl": DutchReplace,
            # "de": GermanReplace,
            # "it": ItalianReplace,
            # "ja": JapanReplace,
            # "pt": PortuguesesReplace,
            # 'fr': FrenchReplace,
            '{}'.format(self.fileAbbr): Excelcontent  # fileAbbr, 用户传入的名称：en, pl, de, fr ....
        }
        formatCode_Key_Value_String = {}
        afterReplaceDict = {}

        for trconKey, trconValue in FromUserfileAbbr.items():  # 用户传入的需要替换的文件缩写的key
            for code_string_file_Key, code_string_file_value in CodeReplaceFilesPath.items():  # 读取对应需要替换的国际化资源文件路径下内容

                if trconKey == code_string_file_Key:
                    print("Replacing [{}] file".format(trconKey))
                    with open(code_string_file_value, "r", encoding="utf-8") as f:
                        for line in f:
                            if "=" in line:
                                line = line.replace('" =', '"=')
                                resoucefileKey = line.split('\"=')[0].lstrip('"')
                                resoucefilevalue = line.split("=")[1].strip().replace('"', "").rstrip()
                                formatCode_Key_Value_String.update({resoucefileKey: resoucefilevalue})

                    # 开始替换
                    man_replace = []  # 找出需要人工手动替换的项目

                    for codeKey, codeValue in formatCode_Key_Value_String.items():
                        # specily_charactor = ['：', ":", "1、", "2、", "3、"]
                        code_specily_charactor = ['：', ":", " ", "  ", "。", ";"]
                        for i in range(len(code_specily_charactor)):
                            if code_specily_charactor[i] in codeKey:
                                tempKeycode = codeKey.rstrip("{}".format(code_specily_charactor[i]))
                            else:
                                tempKeycode = codeKey
                        # print("--------------------Jerry----------{}-----------{}-".format(tempKeycode, trconValue[tempKeycode]))
                        if tempKeycode in trconValue:
                            if trconValue[tempKeycode] != "Jerry":
                                afterReplaceDict.update({tempKeycode: trconValue[tempKeycode]})
                        elif tempKeycode not in trconValue:
                            if tempKeycode.startswith('//'):
                                temp_key = tempKeycode.lstrip('//"')
                                if temp_key in trconValue and "Jerry" not in trconValue[temp_key]:

                                    # print("--------------------Jerry----------{}-----------{}-".format(temp_key,trconValue[temp_key]))
                                    afterReplaceDict.update({temp_key: trconValue[temp_key]})
                                else:
                                    afterReplaceDict.update({tempKeycode: codeValue})
                            else:
                                afterReplaceDict.update({codeKey: codeValue})

                    formatCode_Key_Value_String.clear()

                    # # 写回到代码中的资源文件
                    print('*' * 100)
        # for k, v in afterReplaceDict.items():
        #     print("{} ===>>>>>>>>>>>>>===== {}".format(k, v))

        # with open(CodeReplaceFilesPath[self.fileAbbr], 'w+', encoding="utf-8") as fw:
        #     for k, v in afterReplaceDict.items():
        #         if k.startswith('//"'):
        #             line = '{}" = "{}";'.format(k, "")
        #         elif '//留空' in v:
        #             line = '"{}" = "{}";//留空'.format(k, "")
        #         elif '// 百度翻译' in v:
        #             line = '"{}" = "{}"; // 百度翻译后面需修改'.format(k, v.strip().replace(';', '').replace(
        #                 "// 百度翻译后面需修改", "").strip())
        #         elif '//还没翻译' in v:
        #             line = '"{}" = "{}";//还没翻译'.format(k, "")
        #         else:
        #             line = '"{}" = "{}";'.format(k, v.strip().replace(';', ''))
        #
        #         print(line)
        #
        #         fw.write(line + "\n")
        print('*' * 80)
        print('*' * 80)
        print('写入完成。')
        print("{}-> translation is OK !".format(trconKey))

        print('*' * 40 + "以下内容需要人工进行手动替换" + "*" * 40)
        print('*' * 80)


if __name__ == "__main__":
    filepath = "D:/ddd/7tran/tranOne/tranOne.xlsx"
    codepath = "D:/Code/fusionsolar_7/iCleanPower"
    # InterReplace(filepath, excel_start=1584).ReadInterFileContent()
    InterReplace(excel_file=filepath, codepath=codepath, goalOS='ios', Excelcoloum=3, file_abbreviated='de',
                 excel_row_start=2).replaceTranslateLanguage()
