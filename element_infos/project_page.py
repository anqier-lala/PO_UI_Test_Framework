import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger
from common.base_page import BasePage

class ProjectPage(LoginPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.input_username('admin')
        self.input_password('admin123456')
        self.click_login()

        self.project_link = {'element_name':'项目链接',
                            'locator_type':'xpath',
                            'locator_value':'//li[@data-id="project"]',
                            'timeout': 5 }
        self.task_link = {'element_name':'任务链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="task"]',
                          'timeout': 5 }
        self.kanban_link = {'element_name':'看板链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="kanban"]',
                          'timeout': 5 }
        self.burn_link = {'element_name':'燃尽图链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="burn"]',
                          'timeout': 5 }
        self.story_link = {'element_name':'需求链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="story"]',
                          'timeout': 5 }
        self.qa_link = {'element_name':'测试链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="qa"]',
                          'timeout': 5 }
        self.doc_link = {'element_name':'文档链接',
                          'locator_type':'xpath',
                          'locator_value':'//nav[@id="subNavbar"]//li[@data-id="doc"]',
                          'timeout': 5 }
        self.team_link = {'element_name':'团队链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="team"]',
                          'timeout': 5 }
        self.effort_link = {'element_name':'日志链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="effort"]',
                          'timeout': 5 }
        self.action_link = {'element_name':'动态链接',
                          'locator_type':'xpath',
                          'locator_value':'//li[@data-id="action"]',
                          'timeout': 5 }
        self.product_link = {'element_name':'产品链接',
                          'locator_type':'xpath',
                          'locator_value':'//nav[@id="subNavbar"]//li[@data-id="product"]',
                          'timeout': 5 }
        self.view_link = {'element_name': '概况链接',
                             'locator_type': 'xpath',
                             'locator_value': '//li[@data-id="view"]',
                             'timeout': 5}
        self.add_project_button = {'element_name':'添加项目按钮',
                          'locator_type':'xpath',
                          'locator_value':'//div[@id = "pageActions"]',
                          'timeout': 5 }
        self.add_project_link = {'element_name':'添加项目链接',
                          'locator_type':'xpath',
                          'locator_value':'//div[@class="table-empty-tip"]//a[text()=" 添加项目"]',
                          'timeout': 5 }

    def goto_project_link(self):
        self.click(self.project_link)

    def goto_task_link(self):
        self.click(self.task_link)

    def goto_kanban_link(self):
        self.click(self.kanban_link)

    def goto_burn_link(self):
        self.click(self.burn_link)

    def goto_story_link(self):
        self.click(self.story_link)

    # 待更新，qa link是下拉选项
    # def goto_qa_link(self):
    #     self.click(self.qa_link)

    def goto_doc_link(self):
        self.click(self.doc_link)

    def goto_team_link(self):
        self.click(self.team_link)

    def goto_effort_link(self):
        self.click(self.effort_link)

    def goto_action_link(self):
        self.click(self.action_link)

    def goto_product_link(self):
        self.click(self.product_link)

    def goto_view_link(self):
        self.click(self.view_link)

    def click_add_project_button(self):
        self.click(self.add_project_button)

    def click_add_project_link(self):
        self.click(self.add_project_link)

if __name__=='__main__':

    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
    projectpage = ProjectPage(driver)
    projectpage.goto_project_link()
    projectpage.goto_task_link()
    projectpage.goto_kanban_link()
    projectpage.goto_burn_link()
    projectpage.goto_story_link()
    projectpage.goto_doc_link()
    projectpage.goto_team_link()
    projectpage.goto_effort_link()
    projectpage.goto_product_link()
    projectpage.goto_view_link()
    driver.close()


        