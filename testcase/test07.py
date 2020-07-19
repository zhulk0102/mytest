# -*- coding: utf-8 -*-

'2019-06-14 Created by zhulk'

from page.loginpage import loginPage
from page.formpage import formPage
from page.airpage import airPage
from config.url import e7_Url
from public.mytest import airTicketClassRemote

class airTicketToAndFrom(airTicketClassRemote):
    '''多人往返出票测试用例'''
    def test_airTicket(self):
        loginpage = loginPage(self.driver)
        formpage = formPage(self.driver)
        airpage = airPage(self.driver)
        self.driver.get(e7_Url)
        login = loginpage.login('y1','1')
        self.assertTrue(login, "登陆失败")
        mytrip = formpage.toMyTrip()
        self.assertTrue(mytrip, "进入行程失败")
        frontTripThree = airpage.frontTripThree()
        self.assertTrue(frontTripThree, "往返行程创建失败")
        chooseToAirlineToAndFrom = airpage.chooseToAirlineToAndFrom()
        self.assertTrue(chooseToAirlineToAndFrom, "往返航班预订失败")
        res = formpage.submitFrom()
        self.assertIn(res,"提交成功")





