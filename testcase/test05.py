# -*- coding: utf-8 -*-

'2019-07-08 Created by zhulk'

import unittest
from page.loginpage import loginPage
from page.formpage import formPage
from page.airpage import airPage
from config.url import e7_Url
from public.mytest import airTicketClassRemote

class trip(airTicketClassRemote):
    '''行程机票不带订单测试用例'''
    def test_airTicket(self):
        loginpage = loginPage(self.driver)
        formpage = formPage(self.driver)
        airpage = airPage(self.driver)
        self.driver.get(e7_Url)
        login = loginpage.login('y1','1')
        self.assertTrue(login, "登陆失败")
        mytrip = formpage.toMyTrip()
        self.assertTrue(mytrip, "进入行程失败")
        frontTripTwo = airpage.frontTripTwo()
        self.assertTrue(frontTripTwo, "行程提交失败")
        res = formpage.submitFrom()
        self.assertIn(res,"提交成功")





