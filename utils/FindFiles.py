# -*- encoding:utf-8 -*-

''' Need to code path, we will find files in code path '''

import os


class findFiles:
    def __init__(self, filename, codePath):
        ''' Accroding to file name to search file '''
        self.fname = filename
        self.cPath = codePath

    def serachFilebyFileName(self, **kwargs):
        '''Filesuffix -> you want to search file's suffix.
                    for example: xml, java, sh, h, m and so on

        :return those files which you find with path as list'''
        subfix = []
        for i in kwargs:
            subfix.append(kwargs[i])
        print(subfix)

        finalyfileList = []
        for root, dirs, files in os.walk(self.cPath):
            for file in files:
                allFilesPath = os.path.join(root, file)
                if os.path.splitext(allFilesPath)[1] in [".strings"]:

                    getFilename = os.path.splitext(allFilesPath)[0].split("\\")[-1]
                    if self.fname == getFilename:
                        finalyfileList.append(allFilesPath)
        return finalyfileList

# if __name__ == "__main__":
#     file_name = "Localizable"
#     code = "D:\Code\IOS\iCleanPower"
#
#     findFiles(file_name, code).serachFilebyFileName(oneargs=".strings")
