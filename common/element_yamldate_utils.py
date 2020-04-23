#coding=gbk
import  os
import yaml

current_path=os.path.dirname(__file__)
yaml_path=os.path.join(current_path,'../element_info_datas/element_login_infos.yaml')

class ElementdataYamlUtils():

    def get_yaml_element_info(self,yaml_path):
        file = open(yaml_path, 'r', encoding="gbk")
        file_data = file.read()
        file.close()
        # 指定Loader
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    yaml_path = os.path.join(current_path, '../element_info_datas/element_login_infos.yaml')
    print(ElementdataYamlUtils().get_yaml_element_info(yaml_path))




