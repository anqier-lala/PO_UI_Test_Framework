#coding=gbk
import time
from selenium import webdriver
from common.base_page import BasePage
from common.config_utils import config
from common.element_data_utils import ElementdataUtils
from element_infos.login.login_page import LoginPage
# from actions.login_action import LoginAction
from common.set_driver import set_driver


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # 子类调用父类的属性
        elements = ElementdataUtils('main','main_page').get_element_info()
        self.companyname_showbox =elements['companyname_showbox']
        self.myzone_menu=elements['myzone_menu']
        self.product_menu=elements['product_menu']
        self.username_showspan=elements['username_showspan']
        self.project_menu=elements['project_menu']
        self.test_menu=elements['test_menu']
        self.file_menu=elements['file_menu']
        self.user_menu=elements['user_menu']
        self.quit_button=elements['quit_button']
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

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):
        self.click( self.quit_button )


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
    from actions.login_action import LoginAction
    driver =set_driver()
    driver.get(config.get_url)
    main_page = LoginAction(driver).default_login()
    main_page.wait()   #调试调用封装的等待方法
    print(main_page.get_companyname())
    main_page.wait(1)
    print(main_page.get_username())
    main_page.wait(1)
    print(main_page.goto_myzone())
    main_page.wait(1)
    print(main_page.goto_product())
    main_page.wait(1)
    print(main_page.goto_project())
    main_page.wait(1)
    print(main_page.goto_test())
    main_page.wait(1)
    print(main_page.goto_file())




