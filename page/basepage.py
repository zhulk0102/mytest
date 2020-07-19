# -*- coding: utf-8 -*-

'2019-06-11 Created by zhulk'

from public.log import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from config.url import pictureDir
from public.common import NOW
import time


class basePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.log = Log()

    def find_element_xpath(self,xpath):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.log.info(xpath+"，xpath定位成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+xpath)
            self.save_screen_picture()
            return False

    def find_element_id(self,id):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_element_located((By.ID,id)))
            self.log.info(id+"，id定位成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+id)
            self.save_screen_picture()
            return False

    def find_element_class(self,CLASS):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME,CLASS)))
            self.log.info(CLASS+"，class定位成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+CLASS)
            self.save_screen_picture()
            return False

    def find_element_css(self,css):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))
            self.log.info(css+"，css定位成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+css)
            self.save_screen_picture()
            return False

    def find_elements_xpath(self,xpath):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            self.log.info("，xpath定位列表成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+xpath)
            self.save_screen_picture()
            return False

    def find_elements_css(self,css):
        try:
            element = WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,css)))
            self.log.info("，css定位列表成功")
            return element
        except TimeoutException:
            self.log.error("请重新定位，"+"原始定位是："+css)
            self.save_screen_picture()
            return False

    def quit(self):
        self.driver.quit()
        self.log.info('退出浏览器')

    def switch_frame(self, frame):
        try:
            self.log.info('切换frame')
            return self.driver.switch_to_frame(frame)
        except Exception:
            self.log.error("切换farme失败,"+frame+"定位不到")
            return False

    def switch_to_default(self):
        try:
            self.log.info('退出frame')
            return self.driver.switch_to_default_content()
        except Exception:
            self.log.error('切换默认失败')
            return False

    def switch_to_fatheriframe(self):
        try:
            self.log.info('切换到上一级frame')
            return self.driver.switch_to.parent_frame()
        except Exception:
            self.log.error('切换上一级farme失败')
            return False

    def comfirm(self,type):
        self.log.info("寻找弹窗")
        try:
            if type in 'yes':
                self.driver.switch_to_alert().accept()
            elif type in 'no':
                self.driver.switch_to_alert().dismiss()
            else:
                self.log.error("选择类型错误")
                raise Exception
        except Exception:
            self.log.error("没有找到弹窗")
            self.save_screen_picture()
            return False

    def save_screen_picture(self):  # 获取存放图片的文件夹路径
        picture_path = pictureDir + '\\'+ NOW() + '.png'
        try:
            self.driver.get_screenshot_as_file(picture_path)
        except Exception :
            self.log.error("截图失败")
            return False

    def switch_currenthandles(self):
        all_handles = self. driver.window_handles
        handler = self.driver.current_window_handle
        self.log.info("开始切换窗口")
        for i in all_handles:
            if i != handler:
                self.driver.switch_to.window(i)
                self.log.error("切换成功")


    def actionmouse(self,element):
        try:
            ActionChains(self.driver).move_to_element(element).perform()
            self.log.info('移动鼠标成功')
        except Exception:
            self.log.error("移动失败")
            self.save_screen_picture()
            return False

    def rollto(self, x):
        try:
            self.driver.execute_script('var q=document.documentElement.scrollTop=%s' %x)
            self.log.info('向下滚动了'+str(x))
        except Exception:
            self.log.error('滚动失败')
            return False

    #css定位loading页
    def wait_element_disappear_true(self, element, waittime=1,maxTime=30):
        timeTotal = 0
        try:
            while self.driver.find_element_by_css_selector(
                element).is_displayed() is True:
                time.sleep(waittime)
                timeTotal = waittime + timeTotal
                self.log.info('等待中： '+ element )
                if timeTotal > maxTime:
                    self.log.info("等待总时长" + timeTotal)
                    break
        except Exception:
            self.log.error("等待异常")

    # 执行js
    def execute(self, js, *args):
        try:
            self.driver.execute_script(js, *args)
            self.log.info('执行成功')
        except Exception:
            self.log.error('执行失败')







