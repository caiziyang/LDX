from Fxm.data.rwYaml import readYaml


def getUrl():
    url = readYaml("urls.yaml")

    return url

def getHeaders():
    header = readYaml("headers.yaml")

    return header


def test():
    r = getUrl()
    print(r[0]["url"])
