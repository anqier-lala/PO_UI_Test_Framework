#coding=gbk
# @Time : 2020/5/9 21:18
# @Author : lifangfang



import unittest
from common.set_driver import set_driver
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils



class LinkTest(SeleniumBaseCase):

    def setUp(self) -> None:
        super().setUp()
        self.test_class_data = TestDataUtils('main_suite', 'main_test', 'LinkTest').convert_exceldata_to_testdata()

    def test_goto_myzone(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_myzone']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_myzone()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'goto_myzone用例执行失败')


if __name__ == '__main__':
    unittest.main()


