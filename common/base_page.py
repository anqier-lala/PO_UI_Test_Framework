#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    #浏览器操作封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开URL地址%s;'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info("设置浏览器的最大化")

    def set_brower_min(self):
        self.driver.minimize_window()
        logger.info("设置浏览器的最小化")

    def brower_refresh(self):
        self.driver.refresh()
        logger.info("浏览器的刷新操作")

    def get_title(self):
        value=self.driver.title
        logger.info("获取网页的标题为：%s"%value)
        return value

    #...
    #元素识别的封装
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
        #识别元素
        element=WebDriverWait(self.driver,locator_timeout)\
            .until(lambda x:x.find_element(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        return element

    #元素操作封装：点击封装
    def click(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素进行点击操作'%element_info['element_name'])
        element.click()

    # #元素操作封装：输入内容
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s'%(element_info['element_name'],content))

    #获取元素title属性封装
    # 获取元素属性封装
    def get_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        value = element.get_attribute(attribute_name)
        logger.info('[%s]元素的%s的值为：%s' % (element_info['element_name'], attribute_name, value))
        return value

    #获取元素text属性封装
    def get_text(self,element_info):
        text=self.find_element(element_info).text
        logger.info('[%s]元素的title值为：%s'%(element_info['element_name'],text))
        return text




