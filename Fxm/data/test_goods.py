from Fxm.test.TestCase import TestCase
import yaml
import os

def test_qq():

    # 获取当前脚本所在文件夹路径
    curPath = os.getcwd()
    print(curPath)
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "urls.yaml")

    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    print(type(cfg))  # 读出来是字符串
    # print(cfg)

    d = yaml.load(cfg)  # 用load方法转字典
    print(d)
    print(type(d))