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
        self.set_browser_max()
        self.input_username('admin')
        self.input_password('admin123456')
        self.click_login()

        # 页面各链接跳转（不含下拉选项链接）
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
        # 新增项目页面
        self.add_project_button = {'element_name':'添加项目按钮',
                          'locator_type':'xpath',
                          'locator_value':'//div[@id="pageActions"]//a[text()=" 添加项目"]',
                          'timeout': 5 }
        self.add_project_link = {'element_name':'添加项目链接',
                          'locator_type':'xpath',
                          'locator_value':'//div[@class="table-empty-tip"]//a[text()=" 添加项目"]',
                          'timeout': 5 }
        self.project_name = {'element_name':'项目名称',
                          'locator_type':'xpath',
                          'locator_value':'//input[@id="name"]',
                          'timeout': 5 }
        self.project_code = {'element_name':'项目代号',
                          'locator_type':'xpath',
                          'locator_value':'//input[@id="code"]',
                          'timeout': 5 }
        self.start_end_date = {'element_name':'起始日期',
                          'locator_type':'xpath',
                          'locator_value':'//input[@id="delta7"]',
                          'timeout': 5 }
        self.project_save_button = {'element_name':'保存按钮',
                          'locator_type':'xpath',
                          'locator_value':'//button[@id="submit"]',
                          'timeout': 5 }

        # 新增任务页面
        self.add_task_button = {'element_name': '所属项目',
                                    'locator_type': 'xpath',
                                    'locator_value': '//div[@id="mainMenu"]//a[text()=" 建任务"]',
                                    'timeout': 5}
        self.task_project_select = {'element_name': '所属项目',
                                   'locator_type': 'xpath',
                                   'locator_value': '//div[@id="project_chosen"]',
                                   'timeout': 5}
        self.task_project_select_result = {'element_name':'所属项目选项',
                                          'locator_type':'xpath',
                                          'locator_value':'//ul[@class="chosen-results"]',
                                          'timeout': 5 }
        self.task_type_select = {'element_name': '任务类型',
                                 'locator_type': 'xpath',
                                 'locator_value': '//td[@class="required"]//div[@id="type_chosen"]',
                                 'timeout': 5}
        self.task_type_result = {'element_name': '任务类型选项',
                            'locator_type': 'xpath',
                            'locator_value': '//ul[@class="chosen-results"]',
                            'timeout': 5}
        self.task_name = {'element_name': '任务名称',
                            'locator_type': 'xpath',
                            'locator_value': '//input[@id="name"]',
                            'timeout': 5}
        self.task_save_button = {'element_name': '保存按钮',
                                    'locator_type': 'xpath',
                                    'locator_value': '//button[@id="submit"]',
                                    'timeout': 5}

    # 项目页面各链接跳转
    def goto_project_link(self):
        self.click(self.project_link)
        logger.info("跳转到首页-项目链接")

    def goto_task_link(self):
        self.click(self.task_link)
        logger.info("跳转到首页-项目-任务链接")

    def goto_kanban_link(self):
        self.click(self.kanban_link)
        logger.info("跳转到首页-项目-看板链接")

    def goto_burn_link(self):
        self.click(self.burn_link)
        logger.info("跳转到首页-项目-燃尽图链接")

    def goto_story_link(self):
        self.click(self.story_link)
        logger.info("跳转到首页-项目-需求链接")

    # 待更新，qa link是下拉选项
    # def goto_qa_link(self):
    #     self.click(self.qa_link)

    def goto_doc_link(self):
        self.click(self.doc_link)
        logger.info("跳转到首页-项目-文档链接")

    def goto_team_link(self):
        self.click(self.team_link)
        logger.info("跳转到首页-项目-团队链接")

    def goto_effort_link(self):
        self.click(self.effort_link)
        logger.info("跳转到首页-项目-日志链接")

    def goto_action_link(self):
        self.click(self.action_link)
        logger.info("跳转到首页-项目-动态链接")

    def goto_product_link(self):
        self.click(self.product_link)
        logger.info("跳转到首页-项目-产品链接")

    def goto_view_link(self):
        self.click(self.view_link)
        logger.info("跳转到首页-项目-概况链接")

    # 新增项目页面操作
    def click_add_project_button(self):
        self.click(self.add_project_button)
        logger.info("点击新增项目按钮")

    def click_add_project_link(self):
        self.click(self.add_project_link)
        logger.info("点击页面中新增项目的链接")

    def input_project_name(self,project_name):
        self.input(self.project_name, project_name)
        logger.info("输入项目名称"+project_name)

    def input_project_code(self, project_code):
        self.input(self.project_code, project_code)
        logger.info("输入项目代码" + project_code)

    def input_start_end_date(self):
        self.click(self.start_end_date)
        logger.info("选择起始日期=一星期")

    def click_save_project_button(self):
        self.scroll_to_element(self.project_save_button)
        self.click(self.project_save_button)
        logger.info("点击保存项目按钮")

    # 新增任务页面操作
    def click_add_task_button(self):
        self.click(self.add_task_button)
        logger.info("点击新增任务按钮")

    def input_task_project(self,project_name):
        self.click(self.task_project_select)
        task_project = self.task_project_select_result['locator_value']+'//li[text()="'+str(project_name)+'"]'
        self.task_project_select_result['locator_value'] = task_project
        time.sleep(2)
        self.click(self.task_project_select_result)
        logger.info("选择所属项目")

    def input_task_type(self,task_type):
        self.click(self.task_type_select)
        task_type = self.task_type_result['locator_value']+'//li[text()="'+str(task_type)+'"]'
        self.task_type_result['locator_value'] = task_type
        time.sleep(2)
        self.click(self.task_type_result)
        logger.info("选择任务类型")

    def input_task_name(self,task_name):
        self.input(self.task_name, task_name)
        logger.info("输入任务名称"+task_name)

    def click_save_task_button(self):
        self.scroll_to_element(self.task_save_button)
        self.click(self.task_save_button)
        logger.info("点击任务保存按钮")


if __name__=='__main__':

    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
    projectpage = ProjectPage(driver)

    # 各页面链接跳转
    # projectpage.goto_project_link()
    # projectpage.goto_task_link()
    # projectpage.goto_kanban_link()
    # projectpage.goto_burn_link()
    # projectpage.goto_story_link()
    # projectpage.goto_doc_link()
    # projectpage.goto_team_link()
    # projectpage.goto_effort_link()
    # projectpage.goto_product_link()
    # projectpage.goto_view_link()

    # 新增项目
    # projectpage.goto_project_link()
    # projectpage.click_add_project_button()
    # projectpage.input_project_name("项目名称01")
    # projectpage.input_project_code("project01")
    # projectpage.input_start_end_date()
    # projectpage.click_save_project_button()

    # 新增任务
    projectpage.goto_project_link()
    projectpage.goto_task_link()
    projectpage.click_add_task_button()
    projectpage.input_task_project("项目名称01")
    projectpage.input_task_type("设计")
    projectpage.input_task_name("任务名称01")
    projectpage.click_save_task_button()

    driver.close()


        