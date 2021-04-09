# -*- encoding : utf-8 -*-

from enum import Enum, unique

@unique
class Release_version(Enum):

    B010 = '1335'
    B020 = '1340'
    B030 = '1352'
    B050 = '1353'
    B060 = '1354'
    B070 = '1364'
    B080 = '1365'
    B090 = '1366'

@unique
class Severity(Enum):
    Critical = 1
    Major = 2
    Minor = 3
    Tips = 4

@unique
class Task(Enum):
    BBT = 162
    SINT = 163
    Other = 0    # Exception, need modify to BBT or SINT
    WBIT = 164   #exinclude



#bug超期人员对应
# @unique
# class DevlopPerson(Enum):
#     #测试人员列表
#     PG02005 = '辜林杰'
#     P00609 = '陈正伟'
#     P00761 = '邓智明'
#     P00571 = '张进伟'
#
#
#     #开发人员列表
#     P00708 = '王国庆'
#     P00507 = '宋平'
#     P00517 = '赵宇凤'
#     P00468 = "许必成"
#     P00848 = '张弛'

@unique
class DevlopPerson(Enum):
    #测试人员列表
    PG02005 = '辜林杰'
    P00609 = '陈正伟'
    P00761 = '邓智明'
    P00571 = '张进伟'


    #开发人员列表
    P00708 = '王国庆'
    P00507 = '宋平'
    P00756 = '梁勇'
    P00922 = "谢杰"
    P00848 = '张弛'

# print(DevlopPerson["P00848"].value)