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
from common.element_data_utils import ElementdataUtils


class MainPage(BasePage):   #object 是所有类的父类
    def __init__(self, driver):
        super().__init__(driver)  # 子类调用父类的属性
        ##主页一定要先登录，才能进入这些操作，所以先引入登录类,且登录成功
        login_page = LoginPage(driver)
        login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
        self.set_browser_max()

        # self.companyname_showbox ={'element_name':'公司名称',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//h1[@id="companyname"]',
        #                         'timeout':2}
        #
        # self.username_showspan = {'element_name': '用户名',
        #                      'locator_type': 'xpath',
        #                      'locator_value': "//span[@class='user-name']",
        #                      'timeout': 1}

        elements = ElementdataUtils('main_page').get_element_info()
        self.companyname_showbox =elements['companyname_showbox']
        self.myzone_menu=elements['myzone_menu']
        self.product_menu=elements['product_menu']
        self.username_showspan=elements['username_showspan']
        self.project_menu=elements['project_menu']
        self.test_menu=elements['test_menu']
        self.file_menu=elements['file_menu']
        ##以下控件元素识别以后用于校验点击后进入对应页面
        self.myzone_menu_homepage=elements['myzone_menu_homepage']
        self.product_menu_productpage=elements['product_menu_productpage']
        self.project_menu_projectpage=elements['project_menu_projectpage']
        self.test_menu_testpage=elements['test_menu_testpage']
        self.file_menu_filepage=elements['file_menu_filepage']

    def get_companyname(self):   #方法===>控件的操作
        value=self.get_element_attribute(self.companyname_showbox,'title')
        return value

    def goto_myzone(self):   #进入我的地盘
        self.click(self.myzone_menu)
        value=self.get_text(self.myzone_menu_homepage)
        return value

    def goto_product(self):   #进入产品
        self.click(self.product_menu)
        value=self.get_text(self.product_menu_productpage)
        return value

    def get_username(self):  #获取用户名
        value = self.get_text(self.username_showspan)
        return value

    def goto_project(self):   #进入项目后获取项目主页标识
        self.click(self.project_menu)
        value = self.get_text(self.project_menu_projectpage)
        return value

    def goto_test(self):   #进入测试后获取测试主页文案标识
        self.click(self.test_menu)
        value = self.get_text(self.test_menu_testpage)
        return value

    def goto_file(self):  #进入文档获取文档主页标识
        self.click(self.file_menu)
        value = self.get_text(self.file_menu_filepage)
        return value



if __name__ == '__main__':
    driver = webdriver.Chrome()
    main_page=MainPage(driver)
    time.sleep(1)
    print(main_page.get_companyname())
    time.sleep(1)
    print(main_page.get_username())
    time.sleep(1)
    print(main_page.goto_myzone())
    time.sleep(1)
    print(main_page.goto_product())
    time.sleep(1)
    print(main_page.goto_project())
    time.sleep(1)
    print(main_page.goto_test())
    time.sleep(1)
    print(main_page.goto_file())


