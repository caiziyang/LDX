from Fxm.data.rwYaml import readYaml


def getUrl():
    url = readYaml("urls.yaml")

    return url

def getHeaders():

    header = readYaml("headers.yaml")

    return header

