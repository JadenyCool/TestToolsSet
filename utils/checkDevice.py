# -*- encoding:utf-8 -*-

import os


def checkDevices():
    d_SN = "未检测到可用手机"
    getContent = os.popen("adb devices")
    SN = str(getContent.read()).split("attached")[-1].split("device")[0].strip()
    if SN:
        return SN
    else:
        return d_SN
