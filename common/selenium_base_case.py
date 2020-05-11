#coding=gbk
import unittest
from common.base_page import BasePage
from common.set_driver import set_driver
from common.config_utils import config
from common.log_utils import logger

class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('')
        logger.info('==============�����࿪ʼִ��=============')


    def setUp(self) -> None:
        logger.info('---------���Է�����ʼִ��-----------')
        self.base_page = BasePage(set_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(config.get_url)

    def tearDown(self) -> None:
        # ��������ʧ�ܽ�ͼ
        errors = self._outcome.errors
        for test,exc_info in errors:
            if exc_info:
                self.base_page.wait()
                self.base_page.screenshot_as_file()
        self.base_page.close_tab()
        logger.info('---------���Է���ִ�����-----------')


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('==============������ִ�����=============')


