# coding=utf-8
from common.base import Base
from selenium import webdriver

class Loginpage(Base):

    username_loc = ("xpath",".//*[@id='login']/div[2]/div/div[2]/div[1]/input")
    pwd_loc = ("xpath",".//*[@id='login']/div[2]/div/div[2]/div[2]/input")
    loginbutton_loc = ("xpath",".//*[@id='login']/div[2]/div/div[2]/div[4]/input")
    forgotpwd_loc = ("xpath",".//*[@id='login']/div[2]/div/div[2]/div[3]/a")
    zhuce_loc = ("xpath",".//*[@id='login']/div[2]/div/div[1]/span[2]/a")
    login_name = ("xpath",".//*[@id='header']/div[4]/div[3]/div[2]/div[2]/div[1]")

    def input_user(self,text):
        '''输入用户名'''
        self.my_send_keys(self.username_loc,text)

    def input_pwd(self,text):
        '''输入密码'''
        self.my_send_keys(self.pwd_loc,text)

    def click_login(self):
        '''点击登陆'''
        self.my_click(self.loginbutton_loc)

    def click_forgotpwd(self):
        '''点击忘记密码'''
        self.my_click(self.forgotpwd_loc)

    def click_zhuce(self):
        '''点击注册'''
        self.my_click(self.zhuce_loc)

    def is_success_login(self,text):
        '''验证是否登陆成功'''
        r = self.is_text(self.login_name,text)
        return r






if __name__ == '__main__':
    driver = webdriver.Firefox()
    login = Loginpage(driver)
    login.get("http://www.dianpingmedia.com/framework/OOH@XSystem-v.1.2/login/login.html")
    login.click_forgotpwd()
    login.click_zhuce()


