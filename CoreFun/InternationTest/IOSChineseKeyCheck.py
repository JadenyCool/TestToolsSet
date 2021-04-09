# -*- encoding : utf-8 -*-

# 1. 寻找代码中带有@的并取出
# 2.到string文件中去找，是否存在该key，存在就pass，不存在就留下，并记录
import os
import re
from utils import RWTranslationFile as wf

from CoreFun.Log.LogUtil import MyLog


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return


class iOSchinesecheck:
    def __init__(self, codePath, resultPath, TestLangeList):
        self.cp = codePath
        self.rP = resultPath
        self.TLPlist = TestLangeList
        self.Mylog = MyLog.getLog()
        self.log = self.Mylog.logger

    def searchIOScode(self):
        find_files = []
        for root, dirs, files in os.walk(self.cp):  #
            for file in files:
                pathWithFile = os.path.join(root, file)
                # 分离文件名与扩展名
                try:
                    if os.path.splitext(pathWithFile)[1] in [".m"]:
                        find_files.append(pathWithFile)
                    else:
                        pass
                        # print("不存在.m结尾的文件，请确定路径选择是否正确")
                except FileExistsError as fee:
                    self.log.error(fee)

        return find_files

    def iOS_Resource(self):
        resource_files = []
        file_res = {}
        Tag = False
        for root, dirs, files in os.walk(self.cp):  #
            for file in files:
                pathWithFile = os.path.join(root, file)
                keyword_URL = ["AddStation", "GlobleFile", "view", "HomePage", "NearSide", "ThirdPlug", "Mine",
                               "Operation", "Base.lproj", "en-GB.lproj"]
                if os.path.splitext(pathWithFile)[1] in [".strings"]:
                    for j in range(len(keyword_URL)):
                        if keyword_URL[j] in pathWithFile:
                            # print(pathWithFile)
                            Tag = False
                            break
                        else:
                            Tag = True

                    if Tag == True:
                        if pathWithFile.split("\\")[-1] == "Localizable.strings":
                            resource_files.append(pathWithFile)
                            res_value = pathWithFile.split("\\")[-2].split(".")[0]
                            res_key = pathWithFile
                            file_res.update({res_value: res_key})

        return file_res

    # def getValueCheck(self):
    #     templist = []
    #
    #     pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
    #     files = self.searchIOScode()
    #     for i in range(len(files)):
    #         with open(files[i], 'r', encoding='utf-8') as f:
    #             for line in f:
    #                 if "NSLocalizedString" or 'showInforMessage' in line:
    #                     if "//" not in line:
    #                         print(line)
    #                         CH_Key = pchinese.findall(line, re.MULTILINE)
    #                         if CH_Key:
    #                             print(CH_Key)
    #                             templist.extend(CH_Key)
    #     finalResult = list(set(templist))
    #     finalResult.sort(key=templist.index)
    #     for j in range(len(finalResult)):
    #         print(finalResult[j])
    #     self.log.info(finalResult)
    #     return finalResult

    # def getValueCheck(self):
    #     checkRepeat = []
    #     finalResult = []
    #     key = ['NSLocalizedString(@"', 'NSLocalizedString( @"', 'NSLocalizedString( @"']
    #
    #     files = self.searchIOScode()
    #     for file in range(len(files)):
    #         # print("正在读取第{0}个文件：{1}".format(file, files[file]))
    #         with open(files[file], 'r', encoding='utf-8') as f:
    #             for lines in f:
    #                 line = re.sub(" ", '', lines)
    #                 for m in range(len(key)):
    #                     if key[m] in line:
    #                         if 'NSLocalizedString(@"' == key[m]:
    #                             pass
    #                             # print(lines)
    #                         values = lines.split(key[m])
    #                         zifu = ['",nil', '" ,nil', '" , nil', '",  nil', '", nil']
    #                         for i in range(len(values)):
    #                             for j in range(len(zifu)):
    #                                 if zifu[j] in values[i]:
    #                                     keyva = values[i].split(zifu[j])[0]
    #                                     if keyva != "":
    #                                         checkRepeat.append(keyva)
    #
    #     # set后，返回后为集合，需要转换成list，再进行处理
    #     finalResult.append(set(checkRepeat))
    #     return finalResult
    def getValueCheck(self):
        checkRepeat = []
        finalResult = []
        key = ['NSLocalizedString(@"', 'NSLocalizedString( @"', 'NSLocalizedString( @"']

        files = self.searchIOScode()
        for file in range(len(files)):
            # print("正在读取第{0}个文件：{1}".format(file, files[file]))
            with open(files[file], 'r', encoding='utf-8') as f:
                for lines in f:
                    line = re.sub(' ', '', lines)
                    if not line.startswith("//"):
                        if "imageNamed:NSLocalizedString" not in line:
                            values = line.split('NSLocalizedString(@"')
                            for i in range(len(values)):
                                if '",nil' in values[i] and is_contain_chinese(values[i]):
                                    CH_KEY = values[i].split('",nil')[0]
                                    if CH_KEY != "":
                                        checkRepeat.append(CH_KEY)

        # set后，返回后为集合，需要转换成list，再进行处理
        finalResult.extend(list(set(checkRepeat)))
        # print(finalResult)
        return finalResult

    def compString(self, resource_url):
        codekey = self.getValueCheck()

        dictkey = {}
        result = []
        with open(resource_url, 'r', encoding='utf-8') as r:
            for i in r:
                lines = i.strip()
                if lines.startswith('"'):
                    line = lines.split("=")
                    local_key = line[0].strip()
                    KeyValue = re.sub(' ', '', local_key)
                    local_value = line[1]
                    dictkey.update({KeyValue: local_value})
                else:
                    pass

        for j in range(len(codekey)):
            strcode = '"{}"'.format(codekey[j])
            if strcode in dictkey:
                pass
            else:
                # print(strcode)
                formatkey = strcode + " " + "=" + " " + '"";'
                result.append(formatkey)
        return list(set(result))

    def main(self):
        '''CheckBox_lag is a list'''

        # 获取资源文件
        res_file = self.iOS_Resource()
        test_lang = {}

        # 根据checkbox_lag查看需要扫描的翻译文件

        for i in range(len(self.TLPlist)):
            if self.TLPlist[i] in res_file:
                test_lang.update({self.TLPlist[i]: res_file.get(self.TLPlist[i])})
        self.log.info(test_lang)

        for k, v in test_lang.items():
            resultf = self.rP + "\Test_{}.xlsx".format(k)
            chinesekey = self.compString(resource_url=v)
            if chinesekey:
                wf.writeResult(chinesekey, resultf, colnum=1, os=k)
            else:
                self.log.info(k + " 恭喜你，翻译测试验证已OK，暂时无中文存在")
        else:
            return 1


if __name__ == '__main__':
    codePath = "D:\Code\IOS\iCleanPower"
    reuslt = "D:\ddd\Result"
    tagetLanguage = ['ja']
    iOSchinesecheck(codePath, resultPath=reuslt, TestLangeList=tagetLanguage).main()
