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


class MainPage(BasePage):   #object ��������ĸ���
    def __init__(self, driver):
        super().__init__(driver)  # ������ø��������
        ##��ҳһ��Ҫ�ȵ�¼�����ܽ�����Щ�����������������¼��,�ҵ�¼�ɹ�

        login_page = LoginPage(driver)
        login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
        self.set_browser_max()


        self.companyname_showbox ={'element_name':'��˾����',
                                'locator_type':'xpath',
                                'locator_value':'//h1[@id="companyname"]',
                                'time_out':2}

        self.myzone_menu ={'element_name':'�ҵĵ���',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}

        self.product_menu ={'element_name':'��Ʒ',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}


        self.username_showspan = {'element_name': '�û���',
                             'locator_type': 'xpath',
                             'locator_value': "//span[@class='user-name']",
                             'time_out': 1}


    def get_companyname(self):   #����===>�ؼ��Ĳ���
        value=self.get_title(self.companyname_showbox)
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
    time.sleep(3)
    print(main_page.get_companyname())   ##Ŀǰ�����ֵΪ�գ������!
    time.sleep(3)
    print(main_page.get_username())
    main_page.goto_myzone()
    main_page.goto_product()

