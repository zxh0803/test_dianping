# coding=utf-8
from selenium import webdriver
from common.base import Base
from page.loginpage import Loginpage

class Homepage(Base):

    ordermanage_loc = ("xpath",".//*[@id='open-nav']/li[2]/a/div/div[2]")
    bokongmanage_loc = ("xpath",".//*[@id='open-nav']/li[3]/a/div/div[2]")
    ziyuanmanage_loc = ("xpath",".//*[@id='open-nav']/li[4]/a/div/div[2]")
    caiwumanage_loc = ("xpath",".//*[@id='open-nav']/li[5]/a/div/div[2]")
    shujutongji_loc = ("xpath",".//*[@id='open-nav']/li[6]/a/div/div[2]")
    success_click_ordermanage_loc = ("xpath",".//*[@id='open-nav']/li[2]/div/ul/li[1]/a/div[2]")

    def click_ordermanage(self):
        '''点击订单管理'''
        self.my_click(self.ordermanage_loc)

    def click_bokongmanage(self):
        '''点击播控管理'''
        self.my_click(self.bokongmanage_loc)

    def click_ziyuanmanage(self):
        '''点击资源管理'''
        self.my_click(self.ziyuanmanage_loc)

    def click_cawumanage(self):
        '''点击财务管理'''
        self.my_click(self.caiwumanage_loc)

    def click_shujutongji(self):
        '''点击播数据统计'''
        self.my_click(self.shujutongji_loc)

    def is_success_click_ordermanage(self,text):
        '''验证页面是否跳转到订单管理页面'''
        r = self.is_text(self.success_click_ordermanage_loc,text)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.dianpingmedia.com/framework/OOH@XSystem-v.1.2/login/login.html")
    login = Loginpage(driver)
    login.input_user()
    login.input_pwd()
    login.click_login()
    home = Homepage(driver)
    home.click_cawumanage()
    home.click_bokongmanage()
    home.click_ordermanage()
    home.click_ziyuanmanage()
    home.click_shujutongji()