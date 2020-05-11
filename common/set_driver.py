from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def set_driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"": ""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    chrome_options.add_experimental_option("prefs", prefs)  ##�ص����뵯��
    chrome_options.add_argument('--disable-gpu')  # �ȸ��ĵ��ᵽ��Ҫ����������������bug
    chrome_options.add_argument('lang=zh_CN.UTF-8')  # ����Ĭ�ϱ���Ϊutf-8
    chrome_options.add_experimental_option('useAutomationExtension', False)  # ȡ��chrome���Զ�������ʾ
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # ȡ��chrome���Զ�������ʾ

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def __get_remote_driver(self):  # selenium֧�ֲַ�ʽ grid == > ���ã����Լ��Ĵ����д�����ã�
    driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)


if __name__ == '__main__':
    set_driver()