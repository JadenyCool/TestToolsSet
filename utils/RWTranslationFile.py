# -*- encoding: utf-8 -*-

import os
import xlrd
import xlsxwriter
from CoreFun.Log.LogUtil import MyLog

getLog = MyLog.getLog()
log = getLog.logger


def readTransFile(filepath):
    wookbook = xlrd.open_workbook(filepath)
    getsheet = wookbook.sheets()[0]
    total_rows = getsheet.nrows
    list_huawei_Trans = getsheet.col_values(2, 1, total_rows)
    return list_huawei_Trans

def writeResult(data, resultfile, colnum, os):
    workbook = xlsxwriter.Workbook(resultfile)
    sheet = workbook.add_worksheet("Trans Result_{}".format(os))
    row = 0
    col = 0
    for i in range(len(data)):
        sheet.write(row, col, data[i])
        col = col + int(colnum)
        if col % int(colnum) == 0:
            row = row + int(colnum)
            col = 0

    workbook.close()


    log.info("测试结果已写入：{}".format(resultfile))