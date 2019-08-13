import yaml
import os

def get_yaml_data(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    # 将字符串转化为字典或列表
    data = yaml.load(file_data)
    return data

def get_secret_key():
    current_path = "/".join(os.path.abspath(".").split("/")[:-1])+"/config/config.yml"
    return get_yaml_data(current_path)['secret_key']

def get_access_key():
    current_path = "/".join(os.path.abspath(".").split("/")[:-1])+"/config/config.yml"
    return get_yaml_data(current_path)['access_key']

