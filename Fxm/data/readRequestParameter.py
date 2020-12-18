from Fxm.config.rwYaml import readYaml


def get_Url():
    params = readYaml("../config/updateProductCity")

    return params[0]["url"]
# 获取请求头


def get_Headers():
    params = readYaml("../config/updateProductCity")
    return params[0]["headers"]


def get_json():
    ...


if __name__ == '__main__':
    print(get_Url())
    print(get_Headers())

