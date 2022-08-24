# -*- coding: UTF-8 -*-
import re
from time import sleep
import requests
import json

# 读取日志文件


def readFile(path):
    f = open(path, encoding="utf-8")
    text = f.read()
    f.close()
    return text

# 提取IP


def extractIP(text):
    l = re.findall(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", text)
    # 去重
    return list(set(l))

# 获取定位


def getPosition(ipList):
    for item in ipList:
        url = "http://opendata.baidu.com/api.php?query=" + \
            item+"&co=&resource_id=6006&oe=utf8"
        response = requests.get(url)
        print(item, ": ", json.loads(response.text)['data'][0]['location'])
        # 加个延时
        sleep(1)


def main():
    text = readFile("./file.txt")
    ipList = extractIP(text)
    getPosition(ipList)


if __name__ == '__main__':
    main()
