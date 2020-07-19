#coding=utf-8

'2019-06-14 Created by zhulk'
import os

#测试地址
e7_Url= 'http://192.168.64.12:9000/pages/login.jsp'
#工作路径
basePath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
#用例路径
caseDir = os.path.abspath(os.path.join(basePath,"testcase"))
#截图路径
pictureDir = os.path.abspath(os.path.join(basePath,"screen_picture"))
#报告路径
reportDir = os.path.abspath(os.path.join(basePath,"report"))
#接口数据表路径
apiDir = os.path.abspath(os.path.join(basePath,"data/api_case.xlsx"))
#接口数据表路径
apiDirRes = os.path.abspath(os.path.join(basePath,"data/api_case_result.xlsx"))
#日志路径
logDir = os.path.abspath(os.path.join(basePath,"log"))
#远程HUB
HOST =  '192.168.66.128:4444/wd/hub'


