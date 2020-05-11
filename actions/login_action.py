#coding=gbk
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import config
from common.set_driver import set_driver

class LoginAction():
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        self.login_action(username,password)
        return MainPage( self.login_page.driver )

    def default_login(self):
        return self.login_success(config.get_user_name,config.get_password)


    def login_fail(self,username,password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()


if __name__=="__main__":
    driver=set_driver()
    login_action=LoginAction(driver)
    login_action.login_page.open_url(config.get_url)
    # login_action.login_action("admin","201314ANQIER1")
    # print(login_action.login_fail("admin1","201314ANQIER1"))
    login_action.default_login()
