# coding=utf-8
import unittest
from selenium import webdriver
from page.loginpage import Loginpage
from page.homepage import Homepage
import time

class Testhome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.dianpingmedia.com/framework/OOH@XSystem-v.1.2/login/login.html")
        self.login_driver = Loginpage(self.driver)
        self.home_driver = Homepage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_clik_ordermanage(self):
        self.login_driver.input_user("username")
        self.login_driver.input_pwd("pwd")
        self.login_driver.click_login()
        time.sleep(10)
        self.home_driver.click_ordermanage()
        time.sleep(3)
        r = self.home_driver.is_success_click_ordermanage(u"执行中订单")
        self.assertTrue(r,msg=u"页面跳转到订单管理页面失败")

if __name__ == '__main__':
    unittest.main()