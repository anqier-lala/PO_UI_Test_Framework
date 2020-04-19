import  os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, "../conf/local_config.ini")
print(cfgpath)


class ConfigUtils:
    def __init__(self,config_path=cfgpath):
        self.__conf=configparser.ConfigParser()  ##做成私有实例属性，仅在类的内部使用，外部不可访问，也提高使用的简洁度
        self.__conf.read(config_path, encoding="utf-8")

    def read_ini(self,sec,option):
        value=self.__conf.get(sec,option)
        return value

    @property    #添加这个可将该类的这个方法变成一个类属性，直接调用类的属性就可以
    def get_url(self):
        value=self.read_ini('default','url')
        return value


    @property    #添加这个可将该类的这个方法变成一个类属性，直接调用类的属性就可以
    def get_user_name(self):
        value=self.read_ini('user','user_name')
        return value

    @property
    def get_password(self):
        value = self.read_ini('user', 'password')
        return value

config=ConfigUtils()   #直接定义一个方法，在外部直接调用该方法就可以，不需要再每次都创建一个对象


if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    cfgpath = os.path.join(current_path, "../conf/local_config.ini")
    config_u=ConfigUtils()
    print(config_u.get_user_name)
    print(config_u.get_password)

