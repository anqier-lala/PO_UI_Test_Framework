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


if __name__ == '__main__':
    driver=webdriver.Chrome()
    test_login(config.get_url,config.get_user_name,config.get_password,driver)
