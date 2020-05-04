#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger
from selenium.webdriver.common.action_chains import ActionChains   ##对鼠标事件操作
from selenium.webdriver.common.keys import Keys # 对键盘事件操作


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    # ------ -------------------------------------浏览器操作封装----------------------------------------------#
    #打开网页
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
    def quit_brower(self):
        self.driver.quit()
        logger.info("关闭浏览器")

    # ------ ------------------------------------- 元素识别的封装----------------------------------------------#
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

    # ------ -------------------------------------获取属性封装-------------------------------------#
    #获取元素属性封装
    def get_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        value=element.get_attribute(attribute_name)
        logger.info('[%s]元素的%s的值为：%s'%(element_info['element_name'],attribute_name,value))
        return  value

    #获取元素text属性封装
    def get_text(self,element_info):
        text=self.find_element(element_info).text
        logger.info('[%s]元素的text值为：%s'%(element_info['element_name'],text))
        return  text

    #------ ------------------------------------- 鼠标事件封装----------------------------------------------#
    #元素鼠标操作封装：-测试OK
    def click(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素进行点击操作'%element_info['element_name'])
        element.click()

    #元素鼠标操作：右击-测试OK
    def context_click(self,element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        logger.info('[%s]元素进行右击操作' % element_info['element_name'])
        mouse.context_click(element).perform()

    #元素鼠标操作：移动到该元素上--测试OK
    def moveto_element(self,element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        logger.info('将鼠标移动到[%s]元素上' % element_info['element_name'])
        mouse.move_to_element(element).perform()

    def scrollIntoView(self,element_info):
        element=self.find_element(element_info)
        logger.info('将滚动条滚动至[%s]元素可见'%element_info['element_name'])
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        time.sleep(1)

    # ------ ------------------------------------- 键盘事件封装-------------------------------------------#
    # #键盘事件操作封装：输入内容--OK
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s'%(element_info['element_name'],content))

    #删除内容-测试OK
    def back_space(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素操作back_space' % (element_info['element_name']))
        element.send_keys(Keys.BACK_SPACE)

    #清空内容--测试OK
    def clear_input(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素输入框操作清空' % (element_info['element_name']))
        element.clear()

    #按回车--测试OK
    def enter(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素进行回车键操作' % (element_info['element_name']))
        element.send_keys(Keys.ENTER)

    #全选  Ctrl+a--测试OK
    def ctrl_a(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素输入框内容进行全选操作' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'a')

    #粘贴 Ctrl +x--测试OK
    def ctrl_x(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素输入框内容进行剪切操作' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'x')

    #粘贴 Ctrl +v--测试OK
    def ctrl_v(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]元素输入框内容进行粘贴操作' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'v')

    # ------ ------------------------------------- 弹窗封装----------------------------------------------#
    #弹窗处理封装-测试OK
    def get_alert_content(self,driver):
        time.sleep(3)
        alert = driver.switch_to.alert  # 切换到js弹窗
        value = alert.text
        logger.info('当前弹窗的内容为：%s' % value)
        time.sleep(1)
        alert.accept()
        logger.info('点击弹窗的确定按钮成功')
        return value

    # ------ -------------------------------------frame封装-----------------------------------------------#
    #frame封装frame == > id/name   frame元素对象
    #思路一
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]frame元素切换成功' %(element_info["element_name"]))

    #思路二
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
    def switch_to_frame_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]frame元素切换成功' % (element_info["element_name"]))

    # ------ -------------------------------------切换句柄封装-------------------------------------------#
    ##方式一
    def switch_window_by_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(title):
                break
        logger.info('切换到网页标题为[%s]的句柄成功!'%title)

    #方式二
    def switch_window_by_url(self,url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break
        logger.info('切换到URL为[%s]的句柄成功!' % url)


