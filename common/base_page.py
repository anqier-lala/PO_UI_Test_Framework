#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from selenium.webdriver.support.wait import WebDriverWait
from common.log_utils import logger
from selenium.webdriver.common.action_chains import ActionChains   ##������¼�����
from selenium.webdriver.common.keys import Keys # �Լ����¼�����


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

    # ------ ------------------------------------- Ԫ��ʶ��ķ�װ----------------------------------------------#
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

    # ------ -------------------------------------��ȡ���Է�װ-------------------------------------#
    #��ȡԪ�����Է�װ
    def get_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        value=element.get_attribute(attribute_name)
        logger.info('[%s]Ԫ�ص�%s��ֵΪ��%s'%(element_info['element_name'],attribute_name,value))
        return  value

    #��ȡԪ��text���Է�װ
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
    def moveto_element(self,element_info):
        mouse = ActionChains(self.driver)
        element = self.find_element(element_info)
        logger.info('������ƶ���[%s]Ԫ����' % element_info['element_name'])
        mouse.move_to_element(element).perform()

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
    def get_alert_content(self,driver):
        time.sleep(3)
        alert = driver.switch_to.alert  # �л���js����
        value = alert.text
        logger.info('��ǰ����������Ϊ��%s' % value)
        time.sleep(1)
        alert.accept()
        logger.info('���������ȷ����ť�ɹ�')
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

    # ------ -------------------------------------�л������װ-------------------------------------------#
    ##��ʽһ
    def switch_window_by_title(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(title):
                break
        logger.info('�л�����ҳ����Ϊ[%s]�ľ���ɹ�!'%title)

    #��ʽ��
    def switch_window_by_url(self,url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break
        logger.info('�л���URLΪ[%s]�ľ���ɹ�!' % url)


