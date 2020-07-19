# -*- coding: utf-8 -*-

'2019-06-17 Created by zhulk'


from page.basepage import basePage
import time

class formPage(basePage):
    global formNumber
    #填写单据
    @property
    def fillForm(self):
        return  self.find_element_css("#usuallyMenus > div > a:nth-child(1) > div")
    #101单据
    @property
    def fillForm_101(self):
        return  self.find_element_xpath('//*[@id="1000000010318193"]')
    #添加行程
    @property
    def addTripButton(self):
        return self.find_element_id('addtravelbuttonid')
    #提交审批按钮
    @property
    def submitApproval(self):
        return self.find_element_class('yn-yellow-submit')
    #确认按钮
    @property
    def closeButton(self):
        return self.find_element_css('#btnSubmit')

    #定位到系统管理
    @property
    def systemManeger(self):
        return self.find_element_css('#fist_0 > span')

    #定位管理员日常维护
    @property
    def sysMaintain(self):
        return self.find_element_xpath('//*[@id="menu"]/ul/li[2]/div/ul/li[1]/a')
    #定位定时任务管理
    @property
    def cornMission(self):
        return self.find_element_xpath('//*[@id="menu"]/ul/li[2]/div/ul/li[1]/div/ul/li[6]/a')

    #执行拉取订单定时任务
    @property
    def excuteMission(self):
        return self.find_element_xpath('//*[@id="tbl_tr_55"]/td[12]/a')
    #确认拉取
    @property
    def excuteComfirm(self):
        return self.find_element_xpath('//*[@id="closeBtn"]')

    #商旅商城
    @property
    def trip(self):
        return self.find_element_css('#fist_2 > span')

    #我的订单
    @property
    def myorder(self):
        return self.find_element_css('#menu > ul > li:nth-child(4) > div > ul > li:nth-child(2) > a')

    #我的行程
    @property
    def mytrip(self):
        return self.find_element_css('#menu > ul > li:nth-child(4) > div > ul > li:nth-child(1) > a')

    #单据提交成功标识
    @property
    def successFlag(self):
        return self.find_element_xpath('//*[@id="msgContentId"]')

    #去我的行程函数
    def toMyTrip(self):
        try:
            self.switch_frame("main")
            self.fillForm.click()
            time.sleep(2)
            self.switch_frame("formTree")
            self.fillForm_101.click()
            time.sleep(2)
            self.switch_to_default()
            self.switch_frame("main")
            self.switch_frame("formContent")
            time.sleep(1)
            self.addTripButton.click()
            self.log.info('行程页面进入成功')
            return True
        except Exception:
            return False

    #提交单据流程
    def submitFrom(self):
        time.sleep(3)
        self.switch_frame('main')
        self.switch_frame('formContent')
        self.submitApproval.click()
        time.sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.parent_frame()
        self.switch_frame("jd_iframe")
        time.sleep(2)
        self.closeButton.click()
        time.sleep(2)
        self.switch_to_default()
        time.sleep(4)
        self.switch_frame("jd_iframe")
        time.sleep(1)
        res = self.successFlag.text
        return res

    #共享拉取订单
    def system(self):
        try:
            self.systemManeger.click()
            self.sysMaintain.click()
            self.cornMission.click()
            self.switch_frame('main')
            self.switch_frame('ie_px')
            time.sleep(3)
            self.driver.execute_script('"arguments[0].scrollIntoView(false);", self.excutemission')
            time.sleep(3)
            self.excuteMission.click()
            time.sleep(2)
            self.switch_frame("jd_iframe")
            self.excuteComfirm.click()
            time.sleep(3)
            self.switch_frame('main')
            self.switch_frame('ie_px')
            self.switch_frame("jd_iframe")
            self.excuteComfirm.click()
            return True
        except Exception:
            return False

    #进入我的订单
    def frontOrder(self):
        try:
            self.trip.click()
            time.sleep(2)
            self.myorder.click()
            time.sleep(3)
            self.find_element_id('afls').click()
            time.sleep(1)
            return True
        except Exception:
            return False


    # 进入我的行程
    def frontMytrip(self):
        try:
            time.sleep(2)
            self.trip.click()
            self.mytrip.click()
            time.sleep(3)
            self.find_element_id('afls').click()
            time.sleep(1)
            return True
        except Exception:
            return False



