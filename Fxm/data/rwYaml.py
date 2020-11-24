import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件当前路径

def readYaml(file):

    yamlpath = os.path.join(curpath, file)  # 获取yaml文件地址
    with open(yamlpath, 'r', encoding='utf-8') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        return d


def writeDate(data, file):
    yamlpath = curpath + '//Data' + file + '.yaml'
    with open(yamlpath, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


