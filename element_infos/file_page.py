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


class FilePage(BasePage):
    def __init__(self,driver):
        login_page = LoginPage(driver)
        login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
        self.driver = login_page.driver  # 把login_page的对象转移到filepage
        time.sleep(1)  ##这里一定要加上等待时间，否则获取不到元素
        self.file_menu = self.driver.find_element(By.XPATH,'//a[@href="/zentao/doc/"]')


    def goto_file_menu(self):  # 进入文档菜单
        self.file_menu.click()


if __name__=="__main__":
    driver = set_driver()
    file_page =  FilePage(driver)
    file_page.goto_file_menu()








