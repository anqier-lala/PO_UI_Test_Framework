#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    #�����������װ
    def open_url(self,url):
        self.driver.get(url)
        logger.info('��URL��ַ%s;'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info("��������������")

    def set_brower_min(self):
        self.driver.minimize_window()
        logger.info("�������������С��")

    def brower_refresh(self):
        self.driver.refresh()
        logger.info("�������ˢ�²���")

    def get_title(self):
        value=self.driver.title
        logger.info("��ȡ��ҳ�ı���Ϊ��%s"%value)
        return value

    #...
    #Ԫ��ʶ��ķ�װ
    def find_element(self,element_info):
        locator_type_name=element_info['locator_type']
        locator_value_info=element_info['locator_value']
        locator_timeout=element_info['timeout']
        if locator_type_name =='id':
            locator_type=By.ID
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        #ʶ��Ԫ��
        element=WebDriverWait(self.driver,locator_timeout)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]Ԫ��ʶ��ɹ�'%element_info['element_name'])
        return element

    #Ԫ�ز�����װ�������װ
    def click(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ�ؽ��е������'%element_info['element_name'])
        element.click()

    # #Ԫ�ز�����װ����������
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]Ԫ���������ݣ�%s'%(element_info['element_name'],content))

    #��ȡԪ��title���Է�װ
    # ��ȡԪ�����Է�װ
    def get_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        value = element.get_attribute(attribute_name)
        logger.info('[%s]Ԫ�ص�%s��ֵΪ��%s' % (element_info['element_name'], attribute_name, value))
        return value

    #��ȡԪ��text���Է�װ
    def get_text(self,element_info):
        text=self.find_element(element_info).text
        logger.info('[%s]Ԫ�ص�titleֵΪ��%s'%(element_info['element_name'],text))
        return text




