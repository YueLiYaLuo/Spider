#获取知识图谱的概念集具体描述内容
import json
import requests
from bs4 import BeautifulSoup
import urllib
import re
class GetEntity(object):
    def __init__(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': user_agent}

    def get_EntityName(self,url):
        #获取实体名字
        entitys = []
        try:
            request = urllib.request.Request(url, headers=self.headers)
            # 伪装请求
            response = urllib.request.urlopen(request)
            # 模仿浏览器访问，返回网页数据
            data = response.read()
            # print(data)
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            # 实例化beautifulsoup对象
            # print(soup)
            entitys = soup.find_all("div",class_="navbox")
            for entity in entitys:
                print(entity.get_text())
        except Exception as e:
            print(e)

    def get_EntityHref(self,url):
        #获取实体具体页面链接
        hrefs = []
        try:
            request = urllib.request.Request(url, headers=self.headers)
            # 伪装请求
            response = urllib.request.urlopen(request)
            # 模仿浏览器访问，返回网页数据
            data = response.read()
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            # print(soup)
            entitys = soup.find_all("a")
            for entity in entitys:
                # print(entity)
                print(entity.get("href"))
        except Exception as e:
            print(e)

    def get_Info(self):
        #获取概念的具体信息
        url = "https://en.wikipedia.org"
        with open("Href.txt", "r", encoding='utf-8') as read_file:
            for line in read_file:
                href = url + line
                # print(href)
                try:
                    request = urllib.request.Request(href, headers=self.headers)
                    # 伪装请求
                    response = urllib.request.urlopen(request)
                    # 模仿浏览器访问，返回网页数据
                    data = response.read()
                    soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
                    details = soup.find_all("p")
                    detail = details[0].get_text()
                    # 写入文件
                    print(line.split("/")[2])
                    # 打印概念名称
                    print(detail)
                    # 打印概念具体内容
                except Exception as e:
                    print(e)



getEntity = GetEntity()
# getEntity.get_EntityName("https://en.wikipedia.org/wiki/Data_structure")
# getEntity.get_EntityHref("https://en.wikipedia.org/wiki/Data_structure")
getEntity.get_Info()