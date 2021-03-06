# -*- coding: utf-8 -*-

'2019-06-14 Created by zhulk'

from page.loginpage import loginPage
from page.formpage import formPage
from page.airpage import airPage
from config.url import e7_Url
from public.mytest import airTicketClassRemote


class refundTicket(airTicketClassRemote):
    '''订单退票测试用例'''
    def test_airTicket(self):
        loginpage = loginPage(self.driver)
        formpage = formPage(self.driver)
        airpage = airPage(self.driver)
        self.driver.get(e7_Url)
        login = loginpage.login('y1','1')
        self.assertTrue(login, "登陆失败")
        frontOrder = formpage.frontOrder()
        self.assertTrue(frontOrder,"进入我的订单失败")
        res = airpage.orderByRefund()
        self.assertIn("退票",res)
