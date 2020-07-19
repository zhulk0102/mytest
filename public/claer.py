'''
用于清理日志，截图和报告
'''

import os
from config import url

log = url.logDir
report = url.reportDir
picture = url.pictureDir

def delFile(path):
    ls = os.listdir(path)
    for i in ls:
        pathDetail = os.path.join(path, i)
        os.remove(pathDetail)

delFile(log)
delFile(report)
delFile(picture)