#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains   ##������¼�����
from selenium.webdriver.common.keys import Keys # �Լ����¼�����
from common import HTMLTestReportCN
from common.log_utils import logger
from common.config_utils import config



class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    # ------ -------------------------------------�����������װ----------------------------------------------#
    #����ҳ
    def open_url(self,url):
        self.driver.get(url)
        logger.info('��URL��ַ%s;'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info("��������������")

    def close_tab(self):
        self.driver.close()
        logger.info('�رյ�ǰ��tabҳǩ')


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

    def quit_brower(self):
        self.driver.quit()
        logger.info("�ر������")

    # ------ ------------------------------------- �ȴ���װ---------------------------------------------------#
    #����OK
    def implicitly_wait(self,seconds=config.get_timeout):
        self.driver.implicitly_wait(seconds)

    def wait(self,seconds=config.get_timeout):
        time.sleep(seconds)

    # ------ ------------------------------------- Ԫ��ʶ��ķ�װ----------------------------------------------#
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
            #  ʶ��Ԫ��
            element=WebDriverWait(self.driver,locator_timeout)\
                .until(lambda x:x.find_element(locator_type,locator_value_info))
            logger.info('[%s]Ԫ��ʶ��ɹ�'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s]Ԫ�ز���ʶ��ԭ����%s' % (element_info['element_name'], e.__str__()))
            self.screenshot_as_file()   #  ʧ�ܺ����
        return element

    # ------ -------------------------------------��ȡ���Է�װ----------------------------------------------#
    #��ȡԪ�����Է�װ-����OK
    def get_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        value=element.get_attribute(attribute_name)
        logger.info('[%s]Ԫ�ص�%s��ֵΪ��%s'%(element_info['element_name'],attribute_name,value))
        return  value

    #��ȡԪ��text���Է�װ-����OK
    def get_text(self,element_info):
        text=self.find_element(element_info).text
        logger.info('[%s]Ԫ�ص�textֵΪ��%s'%(element_info['element_name'],text))
        return  text

    #------ ------------------------------------- ����¼���װ----------------------------------------------#
    #Ԫ����������װ��-����OK
    def click(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ�ؽ��е������'%element_info['element_name'])
        element.click()

    #Ԫ�����������һ�-����OK
    def context_click(self,element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        logger.info('[%s]Ԫ�ؽ����һ�����' % element_info['element_name'])
        mouse.context_click(element).perform()

    #Ԫ�����������ƶ�����Ԫ����--����OK
    def move_to_element_by_mouse(self,element_info):
        element = self.find_element(element_info)
        mouse = ActionChains(self.driver)
        logger.info('������ƶ���[%s]Ԫ����' % element_info['element_name'])
        mouse.move_to_element(element).perform()

    def long_press_element(self,element_info,senconds):
        element = self.find_element(element_info)
        logger.info('����곤����[%s]Ԫ���Ϻ��ɿ�' % element_info['element_name'])
        mouse = ActionChains(self.driver)
        mouse.click_and_hold(element).pause(senconds).release(element)


    def scrollIntoView(self,element_info):
        element=self.find_element(element_info)
        logger.info('��������������[%s]Ԫ�ؿɼ�'%element_info['element_name'])
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        time.sleep(1)

    # ------ ------------------------------------- �����¼���װ-------------------------------------------#
    # #�����¼�������װ����������--OK
    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]Ԫ���������ݣ�%s'%(element_info['element_name'],content))

    #ɾ������-����OK
    def back_space(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ�ز���back_space' % (element_info['element_name']))
        element.send_keys(Keys.BACK_SPACE)

    #�������--����OK
    def clear_input(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ�������������' % (element_info['element_name']))
        element.clear()

    #���س�--����OK
    def enter(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ�ؽ��лس�������' % (element_info['element_name']))
        element.send_keys(Keys.ENTER)

    #ȫѡ  Ctrl+a--����OK
    def ctrl_a(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ����������ݽ���ȫѡ����' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'a')

    #ճ�� Ctrl +x--����OK
    def ctrl_x(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ����������ݽ��м��в���' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'x')

    #ճ�� Ctrl +v--����OK
    def ctrl_v(self,element_info):
        element=self.find_element(element_info)
        logger.info('[%s]Ԫ����������ݽ���ճ������' % (element_info['element_name']))
        element.send_keys(Keys.CONTROL, 'v')

    # ------ ------------------------------------- ������װ----------------------------------------------#
    #���������װ-����OK
    def get_alert_content(self,action='accept',timeout=config.get_timeout):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        value = alter.text
        logger.info('��ǰ����������Ϊ��%s' % value)
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return value

    # ------ -------------------------------------frame��װ-----------------------------------------------#
    #frame��װframe == > id/name   frameԪ�ض���
    #˼·һ
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]frameԪ���л��ɹ�' %(element_info["element_name"]))

    #˼·��
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
    def switch_to_frame_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('[%s]frameԪ���л��ɹ�' % (element_info["element_name"]))

    #------------------------------------seleniumִ��js��װ-----------------------------------------------#
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

    # ------ -------------------------------------�л������װ-------------------------------------------#
    ##��ʽһ--����OK
    def switch_window_by_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(title):
                break
        logger.info('�л�����ҳ����Ϊ[%s]�ľ���ɹ�!'%title)

    #��ʽ��--����OK
    def switch_window_by_url(self,url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break
        logger.info('�л���URLΪ[%s]�ľ���ɹ�!' % url)

    #----------------------------��ͼ��װ----------------------------------------------------------#
    #����OK
    # def screenshot_as_file_old(self, *screenshot_path):
    #     current_dir = os.path.dirname(__file__)
    #     if len(screenshot_path) == 0:
    #         screenshot_filepath = config.screenshot_path
    #     else:
    #         screenshot_filepath = screenshot_path[0]
    #     now = time.strftime('%Y_%m_%d_%H_%M_%S')
    #     screenshot_filepath_finally = os.path.join(current_dir, '../' ,screenshot_filepath, 'UITest_%s.png' % now)
    #     self.driver.get_screenshot_as_file(screenshot_filepath_finally)
    #     logger.info('ͼƬ��ȡ�ɹ�')

    #���Ҫ�ڲ��Ա����н�ͼ����Ҫʹ�������ͼ��װ
    def screenshot_as_file(self):
        report_path = os.path.join( os.path.abspath(os.path.dirname(__file__)) , '..', config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot( self.driver )





