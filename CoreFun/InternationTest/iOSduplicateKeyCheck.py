# -*- encoding : utf-8 -*-
'''delete duplicate Key value in Localizable.strings
   date: 2019-04-30
   author: Gulinjie
'''
import os


class iOSResDunlipcateModify:
    def __init__(self, codePath, resultPath):

        self.respath = codePath
        self.resultpath = resultPath

    def iOS_Resource(self):
        resource_files = []
        file_res = {}
        Tag = False
        for root, dirs, files in os.walk(self.respath):  #
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

    def readLocalizablefile(self, resourcefile):
        Key = []
        Allvalue = {}
        with open(resourcefile, 'r', encoding='utf-8') as f:
            for i in f:
                lines = i.strip()
                if lines.startswith('"'):
                    line = lines.split("=")
                    getkey = line[0].rstrip()
                    getkey.replace('"', "")
                    getvalue = line[1]
                    Key.append(getkey)
                    Allvalue.update({getkey: getvalue})
        # delect duplicate key
        noduplicateKey = list(set(Key))
        noduplicateKey.sort(key=Key.index)
        return noduplicateKey, Allvalue

    def compereDeplicateKey(self):
        newStringKey = []
        testFile = self.iOS_Resource()

        for k, v in testFile.items():
            result_File_Path = self.resultpath + "\\DelectDuplicateKey_{}.txt".format(k)
            if os.path.exists(result_File_Path):
                os.remove(result_File_Path)
            listkey, dicAllkey = self.readLocalizablefile(resourcefile=v)
            if listkey:
                print(len(listkey))
                for i in range(len(listkey)):
                    if listkey[i] in dicAllkey:
                        newString = '{}'.format(listkey[i]) + "=" + dicAllkey.get(listkey[i])
                        newStringKey.append(newString)
                print(len(newStringKey))
                for j in range(len(newStringKey)):
                    with open(result_File_Path, 'a', encoding='utf-8') as f:
                        f.write(newStringKey[j] + "\n")
                else:
                    newStringKey.clear()
                    print("重复值已筛选完成：{}".format(result_File_Path))
