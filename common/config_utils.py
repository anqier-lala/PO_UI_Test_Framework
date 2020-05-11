#coding=gbk
import  os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, "../conf/local_config.ini")


class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf=configparser.ConfigParser()  ##����˽��ʵ�����ԣ���������ڲ�ʹ�ã��ⲿ���ɷ��ʣ�Ҳ���ʹ�õļ���
        self.__conf.read(config_path, encoding="gbk")  #��Ϊ�༭�����õ���gbk,���������ļ���ȡ��ʱ������Ҳ��Ҫ����Ϊgbk

    def read_ini(self,sec,option):
        value=self.__conf.get(sec,option)
        return value

    @property    #�������ɽ����������������һ�������ԣ�ֱ�ӵ���������ԾͿ���
    def get_url(self):
        value=self.read_ini('default','url')
        return value


    @property    #�������ɽ����������������һ�������ԣ�ֱ�ӵ���������ԾͿ���
    def get_user_name(self):
        value=self.read_ini('user','user_name')
        return value

    @property
    def get_password(self):
        value = self.read_ini('user', 'password')
        return value

    @property
    def get_timeout(self):
        value = float(self.read_ini('default', 'timeout'))
        return value

    @property
    def screenshot_path(self):
        value = self.read_ini('default', 'screen_shot_path')
        return value

    @property
    def element_info_path(self):
        value = self.read_ini('default', 'element_info_path')
        return value

    @property
    def log_path(self):
        value = self.read_ini('default', 'log_path')
        return value

    @property
    def log_level(self):
        log_level_value = int(self.read_ini('default', 'log_level'))
        return log_level_value

    @property
    def testdata_path(self):
        testdata_path_value = self.read_ini('default', 'testdata_path')
        return testdata_path_value

    @property
    def case_path(self):
        case_path_value = self.read_ini('default', 'case_path')
        return case_path_value

    @property
    def report_path(self):
        report_path_value = self.read_ini('default', 'report_path')
        return report_path_value


    @property
    def smtp_server(self):
        smtp_server_value = self.read_ini('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.read_ini('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_password(self):
        smtp_password_value = self.read_ini('email', 'smtp_password')
        return smtp_password_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.read_ini('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.read_ini('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.read_ini('email', 'smtp_subject')
        return smtp_subject_value


# #ֱ�Ӷ���һ�����������ⲿֱ�ӵ��ø÷����Ϳ��ԣ�����Ҫ��ÿ�ζ�����һ������
config=ConfigUtils()


if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    cfgpath = os.path.join(current_path, "../conf/local_config.ini")
    config_u=ConfigUtils()
    print(config_u.get_url)
    print(config_u.get_user_name)
    print(config_u.testdata_path)
    print(config_u.case_path)
    print(config_u.report_path)
    print(config_u.log_path)
    print(config_u.element_info_path)



