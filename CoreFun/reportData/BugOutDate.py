# -*- encoding: utf-8 -*-

# bug解决超期提醒，一般不超过10天，如果超过10天将给对应的同学邮件提醒。
# 目的：很多之前的老bug一直没有解决，导致后面因找环境回归困难
# sql = select id, title, severity, openedDate , openedBuild, assignedTo from zt_bug WHERE project = 67 and  `status` = "active"

import time
from utils.bugEmailFormat import emailFormat as sendMail
import utils.connectMysql as queryData
from datetime import date, datetime, timedelta
from utils.Test_Report_emuValues import Severity, DevlopPerson


def getNowTime():
    day = date.today()
    now = datetime.now()
    delta = timedelta(days=0)  # days可以为正负数，当为负数时，n_days_after 与n_days_forward 的值与正数时相反；
    # n_days_after = now + delta  # 当前日期推迟n天之后的时间
    n_days_forward = now - delta  # 当前日期向前推n天的时间
    return n_days_forward


def DevoutDateBug(sqlstatment):
    outDateBugs = []
    outdateBugs = queryData.connectDatabases().queryData(sqlstatment)
    outDate = getNowTime().strftime("%Y-%m-%d %H:%M:%S")

    if outdateBugs:
        for i in range(len(outdateBugs)):
            creatDate = outdateBugs[i]['openedDate']
            odate = getNowTime() - creatDate
            if odate.days > 0:
                outdateBugs[i].update(assignedTo=DevlopPerson[outdateBugs[i]['assignedTo']].value)
                outdateBugs[i].update(severity=Severity(outdateBugs[i]['severity']).name)
                outdateBugs[i]["outDate"] = odate.days
                outDateBugs.append(outdateBugs[i])
    return outDateBugs

if __name__ == "__main__":
    sql = 'select id, title, severity, openedDate , openedBuild, assignedTo from zt_bug WHERE project = 85 and  `status` = "active" and deleted != "1" '
    content = DevoutDateBug(sql)
    sendMail(content)
