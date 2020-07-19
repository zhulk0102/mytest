# -*- coding: utf-8 -*-

'2019-06-28 Created by zhulk'


from page.basepage import basePage
import time
import datetime
import random

class airPage(basePage):

    #选择出发地
    @property
    def departurePlace(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[3]/div[1]/div[2]')

    #选择到达地
    @property
    def arrivalPlace(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[3]/div[3]/div[2]')

    #选择城市列表输入
    @property
    def cityList(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[1]/span[2]/input')

    #选择第一个城市
    @property
    def comfirmCity(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[2]/div')

    @property
    def isToAndFrom(self):
        return self.find_element_css('#container > div > div:nth-child(2) > div.index-content > div.nav-bar-container > div > span:nth-child(2)')
    #日期控件
    @property
    def chooseDate(self):
        return self.find_element_css('#container > div > div:nth-child(2) > div.index-content > div.flight-date-field > div > div.in-date')

    #编辑人员
    @property
    def editPerson(self):
        return self.find_element_css('#container > div > div:nth-child(2) > div.index-content > div:nth-child(5) > a > div.mint-cell-wrapper > div.mint-cell-value > span.ykb-icon.person-box > img')

    #添加乘机人
    @property
    def addPerson(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[3]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div[1]/span/label/span/img')

    #确认添加乘机人
    @property
    def addPersonComfirm(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[3]/div/div[5]/div[1]/button')

    #不带订单
    @property
    def noSubmitButton(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]')

    #去预订
    @property
    def submit(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[2]/div[2]')

    #提示框
    @property
    def prompt(self):
        return self.find_element_css('body > div.mint-msgbox-wrapper > div > div.mint-msgbox-btns > button.mint-msgbox-btn.mint-msgbox-confirm')

    #加载loading
    @property
    def loading(self):
        return 'body > div.mint-indicator > div.mint-indicator-wrapper > span.mint-indicator-text'

    #去程航班
    @property
    def toCityFlightline(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[1]')

    #预订航班
    @property
    def bookTicket(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[1]/ul/li[1]/div[2]/div[1]')

    #确定按钮
    @property
    def submitBook(self):
        return self.find_element_css('#container > div > div.flight-list-box > div.footer > span.booking > button')

    #往返确认按钮
    @property
    def submitBookToAndFrom(self):
        return self.find_element_css('#container > div > div.train-list-box > div.footer > span.booking > button')

    #确认提交行程
    @property
    def comfirmTrip(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div[2]')

    #定位筛选
    @property
    def fliter(self):
        return self.find_element_css('#container > div > div.mint-navbar-wrap.fixed-headers-bottom > div.order-search-box.fixed-headers-bottom > div.order-search > div.search-select')

    #机票订单
    @property
    def flightOrder(self):
        return self.find_element_css('#container > div > div.mint-navbar-wrap.fixed-headers-bottom > div.order-search-box.fixed-headers-bottom > div.selectWrapper > div.orderSelect > div.selectButton > ul > li:nth-child(2)')

    #筛选确认
    @property
    def fliterComfirm(self):
        return self.find_element_css('#container > div > div.mint-navbar-wrap.fixed-headers-bottom > div.order-search-box.fixed-headers-bottom > div.selectWrapper > div.orderSelect > div.bottomButton > div.sure')

    #改签按钮
    @property
    def changeFlight(self):
        return self.find_element_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/button[2]')

    #改签确认
    @property
    def changeComfirm(self):
        return self.find_element_xpath('/html/body/div[3]/div/div[2]/button[2]')
    #改签提交
    @property
    def changeSubmit(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[1]/div[4]/span[2]/button')

    #改签提示
    @property
    def changePrompt(self):
        return self.find_element_xpath('/html/body/div[3]/div/div[3]/button[2]')

    #退票按钮
    @property
    def refundFlight(self):
        return self.find_element_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div/button[1]')

    #退票确认
    @property
    def refundComfirm(self):
        return self.find_element_xpath('/html/body/div[3]/div/div[2]/button[2]')

    #退票原因确认
    @property
    def refundReasonComfirm(self):
        return self.find_element_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/section[3]/div/button[2]')

    #行程筛选
    @property
    def tripFliter(self):
        return self.find_element_css('#container > div > div.search-area > div.filter > span')

    #行程筛选机票
    @property
    def tripFliterFlight(self):
        return self.find_element_css('#container > div > div.search-area > div.filterListArea > div.mint-popup.mint-popup-top > div.triptypearea > div:nth-child(1)')

    #行程筛选确定
    @property
    def tripFliterComfirm(self):
        return self.find_element_css('#container > div > div.search-area > div.filterListArea > div.mint-popup.mint-popup-top > div.btnarea > div.surebtn')

    #行程改签确认
    @property
    def tripChangeComfrim(self):
        return self.find_element_css('body > div.mint-msgbox-wrapper > div > div.mint-msgbox-btns > button.mint-msgbox-btn.mint-msgbox-confirm')

    #改签成功标识
    @property
    def successFlag(self):
        return self.find_element_xpath('//*[@id="msgContentId"]')

    #退票成功标识
    @property
    def refundSueceeFlag(self):
        return self.find_element_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/span[2]')

    #行程退票理由
    @property
    def tripRefundReasonComfirm(self):
        return self.find_element_css('#container > div > div.list-panel > div > div > div > div.content-panel > div.schedule-list-panel > div > div > div.action-btn.change-refund-detail-panel > div > div:nth-child(1) > div > div.mint-popup.popup-for-refund-passenger.mint-popup-bottom > div > section.foot > div > button.confirm-button')

    #行程退票成功标识
    @property
    def refundSueceeFlagTrip(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div/div[2]/div[5]/div/div/div[1]/div[1]/div[2]/span')
    #行程输入框
    @property
    def tripFliterInput(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/input')

    #点击全部订单
    @property
    def headOrders(self):
        return self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/div[1]/div[1]/form/input')
    #行程时间的封装
    def getTime(self):
        ran = random.randint(1,32)
        yearMonth = (datetime.datetime.now()+ datetime.timedelta(days=ran)).strftime("%Y-%m")
        monthDate = (datetime.datetime.now()+ datetime.timedelta(days=ran)).strftime("%d")
        monthLength = len(self.find_elements_xpath('//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div'))
        for i in range(1, monthLength):
            yearMonthIfo =self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div[%d]/div'%(i))
            if yearMonthIfo.text == yearMonth:
                dateLength = len(self.find_elements_xpath('//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/span'))
                for j in range(1,dateLength):
                    dateIfo = self.find_element_xpath('//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div[%d]/span[%d]'%(i,j))
                    if dateIfo.text == monthDate:
                        dateIfo.click()
                        break
                break

    #选择航班封装
    def chooseFlight(self,type):
        try:
            if type == '出票失败':
                self.toCityFlightline.click()
                time.sleep(2)
                self.bookTicket.click()
                time.sleep(3)
            elif type == '出票成功':
                self.find_element_xpath('//*[@id="container"]/div/div[3]/div[1]/a[3]').click()
                flightList = len(self.find_elements_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div'))
                for i in range(1,flightList):
                    price = int(self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[%d]/div/div[2]/div[1]'%(i)).text.replace("¥","").strip())
                    if price >= 800 and price <= 1500:
                        self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[%d]'%(i)).click()
                        time.sleep(2)
                        self.find_element_xpath('//*[@id="container"]/div/div[1]/div[2]/article/div[%d]/ul/li[1]/div[2]/div[1]'%(i)).click()
                        time.sleep(3)
                        break
            else:
                self.log.error("类型错误")
                raise Exception
        except Exception:
            self.log.error("没有在800-1500以内的航班")
            return False

    #遍历符合条件的订单
    def findOrder(self,list):
        orderLength = len(self.find_elements_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div/ul/li'))
        for i in range(1,orderLength):
            flag = False
            status = self.find_elements_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div/ul/li[%d]/div/div/div/div[3]/p[2]'%(i))
            for j in status:
                if j.text in list:
                    j.click()
                    flag = True
                    break
            if flag == True:
                break

    # 遍历符合条件的行程
    def findTrip(self,list,type):
        try:
            tripLength = len(self.find_elements_xpath('//*[@id="container"]/div/div[2]/div/div'))
            for i in range(1,tripLength):
                flag = False
                status = self.find_element_xpath('//*[@id="container"]/div/div[2]/div/div[%d]/div/div[2]/div[5]/div/div/div[1]/div[1]/div[2]'%(i))
                for j in list:
                    if j == status.text.strip():
                        if type == '重选':
                            buttonReselect = self.find_element_xpath('//*[@id="container"]/div/div[2]/div/div[%d]/div/div[2]/div[5]/div/div/div[2]/button' % (i))
                            buttonReselect.click()
                        elif type == '改签':
                            buttonChange  = self.find_element_xpath('//*[@id="container"]/div/div[2]/div/div[%d]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/div/div[1]'% (i))
                            buttonChange.click()
                        elif type =='退票':
                            buttonRefund = self.find_element_xpath(
                                '//*[@id="container"]/div/div[2]/div/div[%d]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/div/div[2]' % (
                                    i))
                            buttonRefund.click()
                        else:
                            self.log.error("类型异常")
                            raise Exception
                        tripnumber = self.find_element_xpath(
                            '//*[@id="container"]/div/div[2]/div/div[%i]/div/div[2]/div[1]/div[1]/span[2]' % (i)).text[0:23]
                        flag = True
                        break
                if flag == True:
                    break
            return tripnumber
        except Exception:
            self.log.error('未找到指定的行程状态')
            return False


    #选择城市
    def chooseCity(self):
        city = [['上海', '北京'], ['北京', '上海'], ['上海', '广州'], ['广州', '上海'], ['深圳', '上海'], ['上海', '深圳'],
                ['北京', '广州'], ['广州', '北京'], ['北京', '深圳'], ['深圳', '北京'],
                ['北京', '武汉'], ['武汉', '北京'], ['广州', '武汉'], ['武汉', '广州'], ['宁波', '北京'], ['北京', '宁波']
            , ['上海', '长春'], ['长春', '上海'], ['北京', '长春'], ['长春', '北京']]
        ran = random.randint(0, len(city) - 1)
        self.departurePlace.click()
        time.sleep(2)
        self.cityList.send_keys(city[ran][0])
        time.sleep(2)
        self.comfirmCity.click()
        time.sleep(2)
        self.arrivalPlace.click()
        self.cityList.send_keys(city[ran][1])
        time.sleep(2)
        self.comfirmCity.click()
        time.sleep(3)

    #封装带订单行程前置的操作
    def frontTripOne(self):
        try:
            time.sleep(3)
            self.switch_to_default()
            self.switch_frame("jd_iframe")
            time.sleep(5)
            self.chooseCity()
            self.wait_element_disappear_true(self.loading)
            self.chooseDate.click()
            time.sleep(2)
            self.getTime()
            time.sleep(3)
            self.submit.click()
            time.sleep(3)
            self.prompt.click()
            self.log.info('进入机票列表')
            return True
        except Exception:
            return False


    #不带订单行程前置的操作
    def frontTripTwo(self):
        try:
            time.sleep(3)
            self.switch_to_default()
            self.switch_frame("jd_iframe")
            time.sleep(5)
            self.chooseCity()
            self.wait_element_disappear_true(self.loading)
            self.chooseDate.click()
            time.sleep(2)
            self.getTime()
            time.sleep(3)
            self.noSubmitButton.click()
            time.sleep(4)
            self.comfirmTrip.click()
            return True
        except Exception:
            return False

    #多人往返的机票行程
    def frontTripThree(self):
        try:
            time.sleep(3)
            self.switch_to_default()
            self.switch_frame("jd_iframe")
            time.sleep(5)
            self.chooseCity()
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.chooseDate.click()
            time.sleep(3)
            self.getTime()
            time.sleep(3)
            self.isToAndFrom.click()
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(2)
            self.editPerson.click()
            time.sleep(2)
            self.addPerson.click()
            self.addPersonComfirm.click()
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(2)
            self.submit.click()
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.prompt.click()
            return True
        except Exception:
            return False


    #选择航班
    def chooseToAirline(self):
        try:
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.chooseFlight('出票成功')
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.submitBook.click()
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(2)
            self.comfirmTrip.click()
            time.sleep(3)
            return True
        except Exception:
            return False

    #选择往返航班
    def chooseToAirlineToAndFrom(self):
        try:
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.chooseFlight('出票失败')
            self.wait_element_disappear_true(self.loading)
            time.sleep(3)
            self.chooseFlight('出票成功')
            self.wait_element_disappear_true(self.loading)
            time.sleep(2)
            self.submitBookToAndFrom.click()
            time.sleep(2)
            self.wait_element_disappear_true(self.loading)
            time.sleep(2)
            self.comfirmTrip.click()
            time.sleep(3)
            return True
        except Exception:
            return False

        #我的订单
    def order(self):
        try:
            time.sleep(2)
            self.switch_frame('main')
            self.switch_frame('myorder')
            time.sleep(1)
            self.actionmouse(self.fliter)
            time.sleep(2)
            self.fliter.click()
            self.flightOrder.click()
            time.sleep(2)
            self.fliterComfirm.click()
            time.sleep(3)
            return True
        except Exception:
            return False
    #订单改签
    def orderByChange(self):
        self.order()
        self.findOrder(list=["改签失败","改签成功","出票成功"])
        time.sleep(3)
        self.changeFlight.click()
        time.sleep(4)
        self.changeComfirm.click()
        time.sleep(5)
        self.wait_element_disappear_true(self.loading)
        time.sleep(2)
        self.chooseFlight('出票成功')
        time.sleep(2)
        self.wait_element_disappear_true(self.loading)
        time.sleep(2)
        self.changeSubmit.click()
        time.sleep(3)
        self.changePrompt.click()
        time.sleep(5)
        self.switch_to_default()
        time.sleep(1)
        self.switch_frame("jd_iframe")
        time.sleep(2)
        res = self.successFlag.text
        return res

    #订单退票
    def orderByRefund(self):
        self.order()
        self.findOrder(list=["改签失败", "改签成功", "出票成功", '退票失败'])
        time.sleep(3)
        self.refundFlight.click()
        time.sleep(3)
        self.refundComfirm.click()
        time.sleep(2)
        self.refundReasonComfirm.click()
        time.sleep(1)
        self.wait_element_disappear_true(self.loading)
        time.sleep(2)
        res = self.refundSueceeFlag.text
        return res

    #行程重选
    def tripByReselect(self):
        time.sleep(5)
        self.switch_frame('main')
        self.switch_frame('myorder')
        time.sleep(2)
        self.tripFliter.click()
        time.sleep(2)
        self.tripFliterFlight.click()
        time.sleep(1)
        self.tripFliterComfirm.click()
        time.sleep(2)
        self.findTrip(list=["出票失败","退票成功"],type='重选')
        time.sleep(5)
        self.wait_element_disappear_true(self.loading)
        time.sleep(3)
        self.chooseFlight('出票成功')
        self.wait_element_disappear_true(self.loading)
        time.sleep(3)
        self.submitBook.click()
        time.sleep(3)
        self.switch_to_default()
        time.sleep(1)
        self.switch_frame("jd_iframe")
        time.sleep(1)
        res = self.successFlag.text
        return res


        #行程改签

    #行程改签
    def tripByChange(self):
        time.sleep(5)
        self.switch_frame('main')
        self.switch_frame('myorder')
        time.sleep(2)
        self.tripFliter.click()
        time.sleep(2)
        self.tripFliterFlight.click()
        time.sleep(1)
        self.tripFliterComfirm.click()
        time.sleep(2)
        self.findTrip(list=["出票成功", "改签成功"],type='改签')
        time.sleep(2)
        self.tripChangeComfrim.click()
        time.sleep(2)
        self.wait_element_disappear_true(self.loading)
        time.sleep(3)
        self.chooseFlight('出票成功')
        self.wait_element_disappear_true(self.loading)
        time.sleep(2)
        self.changeSubmit.click()
        time.sleep(3)
        self.changePrompt.click()
        time.sleep(3)
        self.switch_to_default()
        time.sleep(2)
        self.switch_frame("jd_iframe")
        time.sleep(2)
        res = self.successFlag.text
        return res

        #行程退票
    def tripByRefund(self):
        time.sleep(5)
        self.switch_frame('main')
        self.switch_frame('myorder')
        time.sleep(2)
        self.tripFliter.click()
        time.sleep(2)
        self.tripFliterFlight.click()
        time.sleep(2)
        self.tripFliterComfirm.click()
        time.sleep(2)
        self.wait_element_disappear_true(self.loading)
        time.sleep(2)
        number = self.findTrip(list=["出票成功", "改签成功"],type='退票')
        time.sleep(2)
        self.tripChangeComfrim.click()
        time.sleep(2)
        self.tripRefundReasonComfirm.click()
        time.sleep(4)
        self.switch_to_default()
        self.switch_frame('main')
        self.switch_frame('myorder')
        time.sleep(2)
        self.tripFliterInput.send_keys(number)
        time.sleep(2)
        res = self.refundSueceeFlagTrip.text
        return res

