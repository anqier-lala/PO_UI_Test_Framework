#coding=gbk
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import config

class QuitAction:
    def __init__(self,driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        print("点击用户名成功")
        self.main_page.click_quit_button()
        print("点击退出按钮成功")
        return LoginPage( self.main_page.driver )

