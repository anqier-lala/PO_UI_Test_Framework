from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def set_driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"": ""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    chrome_options.add_experimental_option("prefs", prefs)  ##关掉密码弹窗
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
    chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
    driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)


if __name__ == '__main__':
    set_driver()