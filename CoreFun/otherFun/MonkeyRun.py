# -*- encoding:utf-8 -*-

import os


def MonkeyRun(order):
    c = os.popen(order)
    print(c.read())


def getProcessPid():
    # Other Devices:adb shell ps | grep monkey
    # root      1988  260   1362220 53752 futex_wait b7309fd2 S com.android.commands.monkey

    # mate 20 Pro:  adb shell ps -A | grep monkey
    # shell        20503 13513 4440040  99408 binder_ioctl_write_read 0 S com.android.commands.monkey
    forwardPidList = forwardMate20Pid = None
    MonkeyPidOrder = "adb shell ps | grep monkey"
    mate20Pro = "adb shell ps -A | grep monkey"
    pidCheck = os.popen(MonkeyPidOrder)
    mate20Pid = os.popen(mate20Pro)

    # Common devices
    pidlist = pidCheck.readlines()
    mate20PidList = mate20Pid.readlines()
    #print(len(mate20PidList))

    if len(pidlist) >= 1:
        forwardPidList = pidlist[0].split(" ")

    elif len(mate20PidList) >= 1:
        forwardMate20Pid = mate20PidList[0].split(" ")
    else:
        print("Monkey has not run on this device!!")
    return forwardPidList, forwardMate20Pid


def EndMonekyrun():
    getCommonDevicePid, get_Mate20Pid = getProcessPid()
    #print(getCommonDevicePid, get_Mate20Pid)
    if getCommonDevicePid != None:
        getPid = sorted(set(getCommonDevicePid), key=getCommonDevicePid.index)
        killMonkey = "adb shell kill {}".format(getPid[2])
        print("Monkey PID: {}".format(getPid[2]))
        os.popen(killMonkey)
        print("Monkey has been stopped!!!")

    if get_Mate20Pid != None:
        getmate20Pid = sorted(set(get_Mate20Pid), key=get_Mate20Pid.index)
        killMonkey = "adb shell kill {}".format(getmate20Pid[2])
        print("Monkey PID: {}".format(getmate20Pid[2]))
        os.popen(killMonkey)
        print("Monkey has been stopped!!!")
