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


class MainPage(BasePage):   #object ��������ĸ���
    def __init__(self, driver):
        super().__init__(driver)  # ������ø��������
        ##��ҳһ��Ҫ�ȵ�¼�����ܽ�����Щ�����������������¼��,�ҵ�¼�ɹ�
        login_page = LoginPage(driver)
        login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
        self.set_browser_max()

        # self.companyname_showbox ={'element_name':'��˾����',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//h1[@id="companyname"]',
        #                         'timeout':2}
        #
        # self.myzone_menu ={'element_name':'�ҵĵ���',
        #                     'locator_type':'xpath',
        #                     'locator_value':"//li[@data-id='product']",
        #                     'timeout':3}
        #
        # self.product_menu ={'element_name':'����',
        #                     'locator_type':'xpath',
        #                     'locator_value':"//li[@data-id='product']",
        #                     'timeout':3}
        #
        #
        # self.username_showspan = {'element_name': '�û���',
        #                      'locator_type': 'xpath',
        #                      'locator_value': "//span[@class='user-name']",
        #                      'timeout': 1}

        elements = ElementdataUtils('main_page').get_element_info()
        print(elements)
        self.companyname_showbox =elements['companyname_showbox']
        self.myzone_menu=elements['myzone_menu']
        self.product_menu=elements['product_menu']
        self.username_showspan=elements['username_showspan']


    def get_companyname(self):   #����===>�ؼ��Ĳ���
        value=self.get_element_attribute(self.companyname_showbox,'title')
        return value

    def goto_myzone(self):   #�����ҵĵ���
        self.click(self.myzone_menu)

    def goto_product(self):   #�����Ʒ
        self.click(self.product_menu)

    def get_username(self):  #��ȡ�û���
        value = self.get_text(self.username_showspan)
        return value


if __name__ == '__main__':
    driver = webdriver.Chrome()
    main_page=MainPage(driver)
    time.sleep(1)
    print(main_page.get_companyname())
    time.sleep(1)
    print(main_page.get_username())
    main_page.goto_myzone()
    main_page.goto_product()

