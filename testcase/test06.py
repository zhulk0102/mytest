# -*- coding: utf-8 -*-

'2019-07-10 Created by zhulk'


from page.loginpage import loginPage
from page.formpage import formPage
from page.airpage import airPage
from config.url import e7_Url
from public.mytest import airTicketClassRemote

class reselectTicket(airTicketClassRemote):
    '''行程机票重选测试用例'''
    def test_airTicket(self):
        loginpage = loginPage(self.driver)
        formpage = formPage(self.driver)
        airpage = airPage(self.driver)
        self.driver.get(e7_Url)
        login = loginpage.login('y1','1')
        self.assertTrue(login, "登陆失败")
        frontMytrip = formpage.frontMytrip()
        self.assertTrue(frontMytrip, "我的行程进入失败")
        try:
            res = airpage.tripByReselect()
            self.assertIn(res, "操作成功， 正在预订， 请稍后...")
        except Exception:
            res = formpage.submitFrom()
            self.assertIn(res,"提交成功")


