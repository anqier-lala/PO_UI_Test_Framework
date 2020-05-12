#coding=gbk
import unittest
from common.set_driver import set_driver
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.config_utils import config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class QuitTest(SeleniumBaseCase):

    test_class_data = TestDataUtils('main_suite', 'main_test', 'QuitTest').convert_exceldata_to_testdata()
    def setUp(self) -> None:
        super().setUp()

    @unittest.skipIf(test_class_data['test_quit']['isnot'], '')
    def test_quit(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        test_function_data = self.test_class_data['test_quit']
        self._testMethodDoc = test_function_data['test_name']
        quit_action = QuitAction( main_page.driver )
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result, test_function_data['excepted_result'], 'test_quit用例不通过')


if __name__=='__main__':
    unittest.main()





