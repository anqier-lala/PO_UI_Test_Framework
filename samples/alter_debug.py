#coding=gbk
import  os
import time
from selenium  import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from common.base_page import BasePage



curent_path=os.path.dirname(__file__)
driver=webdriver.Chrome()
page_path=os.path.join(curent_path,'./pages/element_samples.html')
driver.implicitly_wait(10)
driver.get('file://'+page_path)

handle=driver.current_window_handle  #��ȡ��ǰ���ھ��
print(handle)
handles=driver.window_handles   #��ȡ���д��ھ��
print(handles)


base_page=BasePage(driver)
e=driver.find_element(By.XPATH,'//select[@name="jumpMenu"]')
Select(e).select_by_visible_text("���������")
base_page.switch_window_by_title("�����н���������")  ##�л���������
# base_page.switch_window_by_url('http://jtj.kaifeng.gov.cn/')
driver.find_element(By.XPATH,'//a[text()="�������"]').click()