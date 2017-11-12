# coding=utf-8

import unittest
from selenium import webdriver
from page.loginpage import Loginpage
import time


class Testlogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_driver = Loginpage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_01(self):
        self.driver.get("http://www.dianpingmedia.com/framework/OOH@XSystem-v.1.2/login/login.html")
        self.login_driver.input_user('yijia')
        self.login_driver.input_pwd('zhongfq')
        self.login_driver.click_login()
        time.sleep(5)
        r = self.login_driver.is_success_login("yijia")
        self.assertTrue(r,msg=u"登陆失败")


if __name__ == '__main__':
    unittest.main()

