# -*- coding: utf-8 -*-

'2019-06-14 Created by zhulk'


from page.loginpage import loginPage
from page.formpage import formPage
from config.url import e7_Url
from public.mytest import airTicketClassRemote

class mission(airTicketClassRemote):
    '''拉取定时任务测试用例'''
    def test_airTicket(self):
        loginpage = loginPage(self.driver)
        formpage = formPage(self.driver)
        self.driver.get(e7_Url)
        login = loginpage.login('y1','1')
        self.assertTrue(login, "登陆失败")
        sys = formpage.system()
        self.assertTrue(sys,"进入定时任务失败")
