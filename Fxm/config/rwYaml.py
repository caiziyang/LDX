import yaml


def readYaml(file):
    # 获取yaml文件地址
    with open(file, 'r', encoding='utf-8') as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        return d


def writeDate(data, file):
    with open(file, 'a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)


