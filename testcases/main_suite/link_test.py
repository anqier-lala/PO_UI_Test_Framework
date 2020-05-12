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
    test_class_data = TestDataUtils('main_suite', 'main_test', 'LinkTest').convert_exceldata_to_testdata()

    def setUp(self) -> None:
        super().setUp()

    @unittest.skipIf(test_class_data['goto_myzone']['isnot'], '')
    def test_goto_myzone(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_myzone']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_myzone()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'goto_myzone用例执行失败')

    @unittest.skipIf(test_class_data['goto_product']['isnot'], '')
    def test_goto_product(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_product']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_product()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'goto_product用例执行失败')

    @unittest.skipIf(test_class_data['goto_project']['isnot'], '')
    def test_goto_project(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_project']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_project()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'goto_project用例执行失败')

    @unittest.skipIf(test_class_data['goto_test']['isnot'], '')
    def test_goto_test(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_test']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_test()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'goto_test用例执行失败')


    @unittest.skipIf(test_class_data['goto_file']['isnot'], '')
    def test_goto_file(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['goto_file']
        self._testMethodDoc = test_function_data['test_name']
        actual_result = main_page.goto_file()
        self.assertEqual(actual_result, test_function_data['excepted_result'], 'goto_file用例执行失败')


if __name__ == '__main__':
    unittest.main()


