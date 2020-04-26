from selenium import  webdriver
from element_infos.login_page import LoginPage
from common.config_utils import config
from common.set_driver import set_driver

def test_login(url, username, password, driver):
    driver.get(url)
    login = LoginPage(driver)
    login.input_username(username)
    login.input_password(password)
    login.click_login()

