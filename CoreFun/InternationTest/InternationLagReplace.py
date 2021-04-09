# -*- encoding:utf-8 -*-
# Author: Gulinjie


# According to HUAWEI's document to modify "Localizable.strings" files
# Table's format will be modified by manual before running this , such as: A:A -> Chinese; B:B -> English; C:C -> Japan;


import os
import openpyxl
from utils.FindFiles import findFiles
import unicodedata
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
        excel_chi_otherLang = {}
        openfile = openpyxl.load_workbook(filename=self.InterationExcelFile, data_only=True)
        getSheetName = openfile.get_sheet_by_name("Sheet1")

        # 将中文符号都转成英文符号，然后再处理符号问题， 只处理中文Key，国际外的Value不处理
        excel_table = {ord(f): ord(t) for f, t in zip(
            u'，。！？【】（）％＃＠＆１２３４５６７８９０',
            u',.!?[]()%#@&1234567890')}
        # excelfuhao = ["。", ":", "：", ".", ";", "！"]
        excelfuhao = [".", ":", ";", "!"]
        j = excelStart
        for excel_translate in list(getSheetName.columns)[self.excelColoum]:
            excel_value = excel_translate.value  # 小语种
            if excel_value is None:
                j = j + 1
            else:
                Ckey_value = getSheetName.cell(row=j, column=1).value
                if Ckey_value:
                    for i in range(len(excelfuhao)):
                        if Ckey_value.endswith("{}".format(excelfuhao[i])):
                            Ckey_value = Ckey_value.rstrip("{}".format(excelfuhao[i]))
                        if excel_value.endswith("{}".format(excelfuhao[i])):
                            excel_value = excel_value.rstrip("{}".format(excelfuhao[i]))
                    excel_chi_otherLang.update({Ckey_value: excel_value})
                    j = j + 1
                else:
                    j = j + 1
        #
        for k, v in excel_chi_otherLang.items():
            print("-{}-Jerry-------{}---------{}".format(j, k, v))
        print(excel_chi_otherLang['zh-CN'])
        return excel_chi_otherLang

    # 查询代码中的国际化.string结尾的文件， 并获取该文件的内容
    def getCodeReplacedFiles(self):
        '''get to search files convert a dict
        :return a dict needReplaceStringFiles'''

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

        return needReplaceStringFiles

    # 格式化代码文件中的字符串
    def formatCodeString(self):
        formatCode_Key_Value_String = {}
        CodeReplaceFilesPath = self.getCodeReplacedFiles()
        code_specily_charactor = ['：', ":", "。", ";", "；", "！"]  # 去掉Key中的特殊符号
        with open(CodeReplaceFilesPath[self.fileAbbr], 'r', encoding='utf-8') as f:
            for cline in f:
                if "=" in cline:
                    line = cline.replace('" =', '"=')
                    resoucefilekey = line.split('\"=')[0].lstrip('"')
                    resoucefilevalue = line.split("=")[1].strip().replace('"', "").rstrip()
                    for i in range(len(code_specily_charactor)):
                        if resoucefilekey.endswith("{}".format(code_specily_charactor[i])):
                            tempKeycode = resoucefilekey.rstrip("{}".format(code_specily_charactor[i]))
                        else:
                            tempKeycode = resoucefilekey

                    formatCode_Key_Value_String.update({tempKeycode: resoucefilevalue})
        return formatCode_Key_Value_String, CodeReplaceFilesPath[self.fileAbbr]

    # 做替换工作
    def replaceTranslateLanguage(self):
        _after_replace_dict = {}  # 定义一个更新后存放元素的字典
        Excelcontent = self.ReadExcel()  # excel表中的对应中文->国际化
        Codekey, stringpath = self.formatCodeString()  # code String文件中的 key----> value

        # 单独处理：1. 替换所有中文符号；2. 去掉所有空格；处理后的Key只能用于搜索，不能用于添加到最后需要更新的字典。
        table = {ord(f): ord(t) for f, t in zip(
            u'，。:！？【】（）％＃＠＆１２３４５６７８９０',
            u',.:!?[]()%#@&1234567890')}
        fuhao_code = [":", ".", "。"]
        for code_k, code_v in Codekey.items():
            _temp_key = code_k.translate(table).replace(" ", "")
            for i in range(len(fuhao_code)):
                if code_k.endswith("{}".format(fuhao_code[i])):
                    _temp_key = _temp_key.translate(table).rstrip("{}".format(fuhao_code[i]))

            if _temp_key in Excelcontent:
                _after_replace_dict.update({code_k: Excelcontent[_temp_key]})
            else:
                if _temp_key.startswith('//'):
                    _temp_key = _temp_key.lstrip('//"')
                    if _temp_key in Excelcontent:
                        code_keys_deal = code_k.lstrip('//"')
                        _after_replace_dict.update({code_keys_deal: Excelcontent[_temp_key]})
                    else:
                        _after_replace_dict.update({code_k: code_v})
                else:
                    _after_replace_dict.update({code_k: code_v})

        # 写回到代码中的资源文件

        print('*' * 100)
        with open(stringpath, 'w+', encoding="utf-8") as fw:
            for k, v in _after_replace_dict.items():
                if k.startswith('//"'):
                    line = '{}" = "{}";'.format(k, "")
                elif '//留空' in v:
                    line = '"{}" = "{}";//留空'.format(k, "")
                elif '// 百度翻译' in v:
                    line = '"{}" = "{}"; // 百度翻译后面需修改'.format(k, v.strip().replace(';', '').replace(
                        "// 百度翻译后面需修改", "").strip())
                elif '//还没翻译' in v:
                    line = '"{}" = "{}";//还没翻译'.format(k, "")
                else:
                    line = '"{}" = "{}";'.format(k, v.strip().replace(';', ''))
                # print(line)
                fw.write(line + "\n")
        print('*' * 80)
        print('*' * 80)
        print('写入完成。')
        print("{}-> translation is OK !".format(stringpath))
        print('*' * 80)


if __name__ == "__main__":
    filepath = "D:/ddd/7tran/tranOne/tranOne.xlsx"
    codepath = "D:/Code/fusionsolar_7/iCleanPower"
    InterReplace(excel_file=filepath, codepath=codepath, goalOS='ios', Excelcoloum=3, file_abbreviated='de',
                 excel_row_start=2).replaceTranslateLanguage()
