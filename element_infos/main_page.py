#coding=gbk
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.config_utils import config
from common import login
from common.set_driver import set_driver
from element_infos.login_page import LoginPage


class MainPage(BasePage):   #object 是所有类的父类
    def __init__(self, driver):
        super().__init__(driver)  # 子类调用父类的属性
        ##主页一定要先登录，才能进入这些操作，所以先引入登录类,且登录成功

        login_page = LoginPage(driver)
        login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
        self.set_browser_max()


        self.companyname_showbox ={'element_name':'公司名称',
                                'locator_type':'xpath',
                                'locator_value':'//h1[@id="companyname"]',
                                'time_out':2}

        self.myzone_menu ={'element_name':'我的地盘',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}

        self.product_menu ={'element_name':'产品',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}


        self.username_showspan = {'element_name': '用户名',
                             'locator_type': 'xpath',
                             'locator_value': "//span[@class='user-name']",
                             'time_out': 1}


    def get_companyname(self):   #方法===>控件的操作
        value=self.get_title(self.companyname_showbox)
        return value

    def goto_myzone(self):   #进入我的地盘
        self.click(self.myzone_menu)

    def goto_product(self):   #进入产品
        self.click(self.product_menu)

    def get_username(self):  #获取用户名
        value = self.get_text(self.username_showspan)
        return value


if __name__ == '__main__':
    driver = webdriver.Chrome()
    main_page=MainPage(driver)
    time.sleep(3)
    print(main_page.get_companyname())   ##目前输出的值为空，待解决!
    time.sleep(3)
    print(main_page.get_username())
    main_page.goto_myzone()
    main_page.goto_product()

