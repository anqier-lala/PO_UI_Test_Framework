from selenium import webdriver
from common.config_utils import config


def set_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(config.get_url)
    return driver


if __name__ == '__main__':
    set_driver()