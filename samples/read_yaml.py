#coding=gbk

import yaml
import os

current_path=os.path.dirname(__file__)
yaml_path=os.path.join(current_path,'../element_info_datas/element_login_infos.yaml')

file = open(yaml_path, 'r', encoding="gbk")
#读取文件中的所有数据
file_data = file.read()
file.close()

#指定Loader
data = yaml.load(file_data,Loader=yaml.FullLoader)
print(data)

