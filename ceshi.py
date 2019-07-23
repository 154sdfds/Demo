import urllib.request
import urllib.parse
import json


def get_data(words):
    data = {}
    data["type"] = "AUTO"
    data["i"] = words
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data


def url_open(url, data):
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    return html


def get_json_data(html):
    result = json.loads(html)
    result = result['translateResult']
    result = result[0][0]['tgt']
    return result


def main():
    words = input("please input words: ")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"

    data = get_data(words)
    html = url_open(url, data)
    result = get_json_data(html)
    print("The result: %s" % result)


if __name__ == "__main__":
        main()