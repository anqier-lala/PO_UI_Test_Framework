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
from common.element_data_utils import ElementdataUtils
from common.element_yamldate_utils import ElementdataYamlUtils
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage

##调试代码1
# driver=webdriver.Chrome()
# main_page=MainPage(driver)
# main_page.goto_myzone()
# value=driver.find_element(By.XPATH,'//li[@data-id="index"]').text
# print(value)
# main_page.goto_product()
# time.sleep(1)
# element=driver.find_element(By.XPATH,'//div[@class="btn-group"]')
# value1=element.text
# print(value1)
# element.click()
# driver.quit()
# main_page.goto_project()
# value2=driver.find_element(By.XPATH,'//div[@class="btn-group"]').text
# print(value2)
# main_page.goto_test()
# value3=driver.find_element(By.XPATH,'//div[@class="btn-group"]').text
# print(value3)
# main_page.goto_file()
# value4=driver.find_element(By.XPATH,'//div[@class="btn-group angle-btn"]').text
# print(value4)

##调试代码2-20200504
driver=set_driver()
base_page = BasePage(driver)
driver.maximize_window()
driver.get(config.get_url)
login = LoginPage(driver)
login.input_username("admin")
login.ctrl_a(login.username_inputbox)
time.sleep(2)
login.ctrl_x(login.username_inputbox)
time.sleep(2)
login.ctrl_v(login.username_inputbox)

# login.back_space(login.username_inputbox)  ##删除
# login.clear_input(login.username_inputbox)  #清空
login.input_password('201314ANQIER1')
login.enter(login.login_button)  ##回车登录

