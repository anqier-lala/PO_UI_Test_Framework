#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains   ##对鼠标事件操作
from selenium.webdriver.common.keys import Keys # 对键盘事件操作
from common import HTMLTestReportCN
from common.log_utils import logger
from common.config_utils import config



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

    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前的tab页签')


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

    # ------ ------------------------------------- 等待封装---------------------------------------------------#
    #测试OK
    def implicitly_wait(self,seconds=config.get_timeout):
        self.driver.implicitly_wait(seconds)

    def wait(self,seconds=config.get_timeout):
        time.sleep(seconds)

    # ------ ------------------------------------- 元素识别的封装----------------------------------------------#
    def find_element(self,element_info):
        try:
            locator_type_name=element_info['locator_type']
            locator_value_info=element_info['locator_value']
            locator_timeout=element_info['timeout']
            if locator_type_name =='id':
                locator_type=By.ID
            elif locator_type_name=='class':
                locator_type=By.CLASS_NAME
            elif locator_type_name=='xpath':
                locator_type=By.XPATH
            #  识别元素
            element=WebDriverWait(self.driver,locator_timeout)\
                .until(lambda x:x.find_element(locator_type,locator_value_info))
            logger.info('[%s]元素识别成功'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素不能识别，原因是%s' % (element_info['element_name'], e.__str__()))
            self.screenshot_as_file()   #  失败后截屏
        return element

    # ------ -------------------------------------获取属性封装----------------------------------------------#
    #获取元素属性封装-测试OK
    def get_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        value=element.get_attribute(attribute_name)
        logger.info('[%s]元素的%s的值为：%s'%(element_info['element_name'],attribute_name,value))
        return  value

    #获取元素text属性封装-测试OK
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
    def move_to_element_by_mouse(self,element_info):
        element = self.find_element(element_info)
        mouse = ActionChains(self.driver)
        logger.info('将鼠标移动到[%s]元素上' % element_info['element_name'])
        mouse.move_to_element(element).perform()

    def long_press_element(self,element_info,senconds):
        element = self.find_element(element_info)
        logger.info('将鼠标长按到[%s]元素上后松开' % element_info['element_name'])
        mouse = ActionChains(self.driver)
        mouse.click_and_hold(element).pause(senconds).release(element)


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
    def get_alert_content(self,action='accept',timeout=config.get_timeout):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        value = alter.text
        logger.info('当前弹窗的内容为：%s' % value)
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
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

    #------------------------------------selenium执行js封装-----------------------------------------------#
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

    def delete_element_attribute(self,element_info,attribute_name):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    def update_element_attribute(self, element_info, attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");' %(attribute_name,attribute_value), element)

    # ------ -------------------------------------切换句柄封装-------------------------------------------#
    ##方式一--测试OK
    def switch_window_by_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(title):
                break
        logger.info('切换到网页标题为[%s]的句柄成功!'%title)

    #方式二--测试OK
    def switch_window_by_url(self,url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break
        logger.info('切换到URL为[%s]的句柄成功!' % url)

    #----------------------------截图封装----------------------------------------------------------#
    #测试OK
    # def screenshot_as_file_old(self, *screenshot_path):
    #     current_dir = os.path.dirname(__file__)
    #     if len(screenshot_path) == 0:
    #         screenshot_filepath = config.screenshot_path
    #     else:
    #         screenshot_filepath = screenshot_path[0]
    #     now = time.strftime('%Y_%m_%d_%H_%M_%S')
    #     screenshot_filepath_finally = os.path.join(current_dir, '../' ,screenshot_filepath, 'UITest_%s.png' % now)
    #     self.driver.get_screenshot_as_file(screenshot_filepath_finally)
    #     logger.info('图片截取成功')

    #如果要在测试报告中截图，需要使用这个截图封装
    def screenshot_as_file(self):
        report_path = os.path.join( os.path.abspath(os.path.dirname(__file__)) , '..', config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot( self.driver )





