# -*- coding: utf-8 -*-

'2019-06-18 Created by zhulk'

import unittest
import os
from config.url import caseDir
from HTMLTestRunner_cn import HTMLTestRunner
from public.common import NOW
from config.url import reportDir
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
import smtplib

#创建测试用例
def createTestsuite():
    #改变路径到测试路径到testcase并筛选
    os.chdir(caseDir)
    suite = []
    test_unit = unittest.TestSuite()
    discover_suites = unittest.defaultTestLoader.discover(os.getcwd(), pattern='*.py')
    for testsuite in discover_suites:
        for testcase in testsuite:
            test_unit.addTest(testcase)
    suite.append(test_unit)
    return suite

#执行测试用例并生成报告
def excuteTestcase(suite):
    os.chdir(reportDir)
    filename = os.getcwd()+'\\'+ NOW() + ".html"
    fp = open(filename,'wb')
    for testcase in suite:
        runner = HTMLTestRunner(
            title='测试报告',
            description='E7商旅测试',
            stream=fp,
            verbosity=2,retry=0,save_last_try=True
        )
        runner.run(testcase)

#获取最新的报告
def newReport():
    lists = os.listdir(reportDir)
    lists.sort(key=lambda fn: os.path.getmtime(reportDir + '\\' + fn))
    # 获取最新文件的绝对路径
    newpath = os.path.join(reportDir, lists[-1])
    return newpath


#发送邮件
def sendEmail(filename):
    mailfrom = 'zlk_0102@163.com'
    mailto = '517122472@qq.com'
    f = open(filename, 'rb')
    mailcontent = f.read()
    f.close()
    msg = MIMEMultipart()
    msg.attach(MIMEText(mailcontent, _subtype='html', _charset='utf-8'))
    att = MIMEText(mailcontent, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=' + filename
    msg.attach(att)
    msg['Subject'] = Header(u'商旅测试自动化测试报告', 'utf-8')
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg['From'] = mailfrom
    msg['to'] = mailto
    username = 'zlk_0102@163.com'
    password = 'nicaiya01'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(mailfrom, mailto, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    excuteTestcase(createTestsuite())
    sendEmail(newReport())


