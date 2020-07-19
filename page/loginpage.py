# -*- coding: utf-8 -*-

'2019-06-14 Created by zhulk'


from page.basepage import basePage
import time


class loginPage(basePage):
    #用户名
    @property
    def username(self):
        return self.find_element_xpath('//*[@id="usernameInput"]')
    #密码
    @property
    def password(self):
        return self.find_element_xpath('//*[@id="passwordInput"]')
    #登录按钮
    @property
    def loginButton(self):
        return self.find_element_xpath('//*[@id="submitButton"]')
    #选择语言，docker环境默认英文
    @property
    def language(self):
        return self.find_element_xpath('//*[@id="languageSelect"]')

    # 选择中文语言，docker环境默认英文
    @property
    def languageChinese(self):
        return self.find_element_xpath('//*[@id="languageSelect"]/option[1]')
    #登录
    def login(self,username,passwd):
        try:
            self.language.click()
            time.sleep(1)
            self.languageChinese.click()
            time.sleep(1)
            self.username.send_keys(username)
            time.sleep(2)
            self.password.send_keys(passwd)
            time.sleep(2)
            self.loginButton.click()
            time.sleep(1)
            return True
        except Exception:
            return False






