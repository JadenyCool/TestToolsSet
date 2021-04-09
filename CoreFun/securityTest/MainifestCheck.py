# -*- encoding:utf-8 -*-

'''Security Test
1. Check permission in AndroidManifest.xml
2. check protectLevel
3. check allowBack (the Value must be set False)
4. Check android:exported (the Value must be set False, otherwise, print Activity to analysis)
'''

from CoreFun.Log.LogUtil import MyLog
import xml.dom.minidom as xmldom


class ManifestCheck:
    def __init__(self, manifestFile):
        self.manifestFile = manifestFile
        self.Mylog = MyLog.getLog()
        self.log = self.Mylog.logger

    # parse manifest file
    def parseFile(self):
        checklist = []
        dom = xmldom.parse(self.manifestFile)
        subpermission = dom.getElementsByTagName("permission")
        subUserPermission = dom.getElementsByTagName("uses-permission")
        subApplication = dom.getElementsByTagName("application")
        subactivity = dom.getElementsByTagName("activity")
        subService = dom.getElementsByTagName("service")
        subProvider = dom.getElementsByTagName("provider")

        checklist.append(subpermission)
        checklist.append(subUserPermission)
        checklist.append(subApplication)
        checklist.append(subactivity)
        checklist.append(subService)
        checklist.append(subProvider)

        return checklist

    def allowBackUpCheck(self):
        xmllist = self.parseFile()
        for m in xmllist[2]:
            checkBackup = m.getAttribute("android:allowBackup")
            if checkBackup == "true":
                #print("android:allowBackup=\"{}\"".format(checkBackup))
                self.log.info("android:allowBackup=\"{}\"".format(checkBackup))
                print("<<<<<<<赶紧提单，别磨蹭了>>>>>>")
            else:
                print("\n<<<<<<<<<<<***allowBackup***安全****>>>>>>>>")

    def permissionCheck(self):
        permissionList = self.parseFile()
        print("(((**(((**(((** 权限级别申请 **))**))**))**))")
        for j in permissionList[0]:
            defindPermission_name = j.getAttribute("android:name")
            defindPermission = j.getAttribute("android:protectionLevel")
            if defindPermission != "signature" or "signatureOrSystem":
                print(defindPermission_name)
                print("android:protectionLevel={}".format(defindPermission))

        print("\n")
        print("(((**(((**(((** 权限列表 **))**))**))**))")
        for i in permissionList[1]:
            permission = i.getAttribute("android:name")
            print(permission)

    def exprotedCheck(self):
        '''Check android:exported (the Value must be set False, otherwise, print Activity to analysis)'''
        a = self.parseFile()
        b = a[3:6:1]

        for i in range(len(b)):
            for n in b[i]:
                if n.getAttribute("android:exported"):
                    getExported = n.getAttribute("android:exported")
                    if getExported == "true":
                        getActivity = n.getAttribute("android:name")
                        print(getActivity)
                else:
                    getActivity = n.getAttribute("android:name")
                    print(getActivity)

    def manifestSecurityCheck(self):

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("|||||")
        print("*********************备份检查(allowBackup)******************")
        print("检查程序是否允许备份：android:allowBackup=\"false\"")
        print("|||||")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.allowBackUpCheck()

        print("\n\n")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("|||||")
        print("**************权*************限************列***********表**")
        print("|||||")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.permissionCheck()

        print("\n\n")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("|||||")
        print("Activity, Service, Provider组件未设置Android:exported=false")
        print("|||||")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.exprotedCheck()

#
# if __name__ == "__main__":
#     path = "D:\\Code\\Android\\app\\src\\main\\AndroidManifest.xml"
#
#     ManifestCheck(path).manifestSecurityCheck()
