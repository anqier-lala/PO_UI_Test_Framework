#coding=gbk
# @Time : 2020/5/8 20:30
# @Author : lifangfang


import unittest
from common.set_driver import set_driver
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils



class LoginTest(SeleniumBaseCase):
    test_class_data = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()

    @unittest.skipIf(test_class_data['test_login_success']['isnot'],'')  ##类属性给方法用
    def test_login_success(self):
        test_function_data = self.test_class_data['test_login_success']   #  把登录成功的参数传入进来
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction( self.base_page.driver )
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        actual_result = main_page.get_username()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'test_login_success用例执行失败')

    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        # print('actual:%s'%actual_result)
        self.assertEqual(actual_result,test_function_data['excepted_result'])


if __name__ == '__main__':
    unittest.main()




