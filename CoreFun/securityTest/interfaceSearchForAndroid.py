# -*- encoding:utf-8 -*-

'''Android 代码中的接口搜索'''

import os

#androidCode = "D:\\Code\\Android\\app\\src"


class searchAndroidInterface:

    def __init__(self, codePath, resPath):
        '''CodePath: Android code path;
        resPath: save result of search '''
        self.androidCodePath = codePath
        self.resultPath = resPath

    def searchJavaFile(self):
        javaFile = []
        for root, dirs, files in os.walk(self.androidCodePath):
            for file in files:
                javaFilePath = os.path.join(root, file)
                if os.path.splitext(javaFilePath)[1] in [".java"]:
                    javaFile.append(javaFilePath)
        return javaFile

    def readFile(self, java_file):
        Final_interface = []
        interface_start_keyword = ["String URL_", '"/']
        interface_end_keyword = ['";', '")', '",', '" +']

        with open(java_file, 'r', encoding="utf-8") as f:
            for line in f:
                if interface_start_keyword[0] in line:
                    interface = line.split("=")[1].lstrip(";")
                    # print(interface)
                    Final_interface.append(interface)
                elif interface_start_keyword[1] in line:
                    getinterface = line.split('"/')[1]
                    for i in interface_end_keyword:
                        if i in getinterface:
                            interface = getinterface.split(i)[0]
                            Final_interface.append(interface)
                            break
        return Final_interface

    def run(self):
        result_path = self.resultPath + "\\androidInterfaceRes.txt"
        result = []
        java_path = self.searchJavaFile()
        for i in range(len(java_path)):
            print(java_path[i])
            get_interface = self.readFile(java_path[i])
            if get_interface:
                result.append(get_interface)
            else:
                pass
        # new_result = set(result)
        print(result)
        for j in range(len(result)):
            for h in range(len(result[j])):
                if result[j][h]:
                    with open(result_path, 'a', encoding="utf-8") as f:
                        f.write(result[j][h] + "\n")
        print("\n + Result of interface in the code by search save to {}".format(result_path))


# if __name__ == "__main__":
#     android = "D:\\Code\\Android\\app\\src"
#     res = "D:\\ddd"
#     a = searchAndroidInterface(codePath=android, resPath=res)
#     a.run()
