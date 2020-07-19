# -*- coding: utf-8 -*-

'2019-08-15 Created by zhulk'

import unittest
from public.log import Log
from selenium import webdriver
from config.url import HOST



class airTicketClassRemote(unittest.TestCase):
    log =Log()
    def setUp(self):
        self.log.info("开始测试")
        self.driver = webdriver.Remote(command_executor=HOST,
                        desired_capabilities={'platform': 'ANY',
                                              'browserName': 'chrome',
                                              'version': '',
                                              'javascriptEnabled': True
                                              }
                        )
        self.driver.maximize_window()

    def tearDown(self):
        self.log.info("测试完成")


class airTicketClass(unittest.TestCase):
    log =Log()
    def setUp(self):
        self.log.info("开始测试")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.log.info("测试完成")


if __name__ == '__main__':
    unittest.main()





