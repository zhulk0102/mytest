# -*- coding: utf-8 -*-

'2019-07-01 Created by zhulk'

import datetime
import os
import xlrd
import xlwt
import pymysql
from public.log import Log

log = Log()
def NOW():
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return now

#不支持xlsx！！！
class Excel(object):
    os.chdir('../data')
    filename = './apicase.xls'
    print(os.getcwd())
    def writecontent(self,x,y,content,sheetName):
        try:
            file = xlwt.Workbook()
            table = file.add_sheet(sheetName)
            table.write(x,y,content)
            file.save(self.filename)
            log.info('写入成功')
        except FileNotFoundError:
            log.info('未找到此文件')

    #读取EXCEL(表名，行，列)
    def redexcel(self,sheet,x,y):
        data = xlrd.open_workbook(self.filename, "utf-8")
        self.table = data.sheet_by_name(sheet)
        return self.table.cell_value(x.y)
    #返回行
    def redexcelrows(self,sheet, x):
        data = xlrd.open_workbook(self.filename, "utf-8")
        self.table = data.sheet_by_name(sheet)
        return self.table.row_values(x)
    #返回列
    def redexcelcols(self,sheet,y):
        data = xlrd.open_workbook(self.filename, "utf-8")
        self.table = data.sheet_by_name(sheet)
        return self.table.col_values(y)

#数据库的操作,默认本机可修改
def mysql_commit(sql):
    try:
        db = pymysql.connect(host='192.168.32.100', port=3306, user='root', passwd='123456', db='ceshi',
                             charset='utf8')
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
    except Exception:
        log.error('执行异常')









