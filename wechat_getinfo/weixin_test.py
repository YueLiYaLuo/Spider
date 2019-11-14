#直接爬去西刺代理上的某一页代理进行随机选取一个进行使用
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests
import random

class Spider(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}

    def get_ip_list(self):                     #从西刺代理网站上获取一个IP列表
        url = 'http://www.xicidaili.com/nn/'
        web_data = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    def get_random_ip(self,ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
        print(proxies)
        return proxies

    def start(self,url,proxy,n):    #参数n是为了，当有ip地址不能使用时产生下一个ip而继续爬取当前页面
        try:
            httpproxy_handler = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(httpproxy_handler)     #使用代理ip
            request=urllib.request.Request(url,headers=self.headers)
            response = opener.open(request)
            data=response.read()
            # print(data)
            datahref=[]
            title_all=[]                    #存放标题
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            links=soup.find_all('div',class_='img-box')
            for link in links:
                datahref.append(link.a['href'])
                # print(link.a['href'])
            file=open('link.text','a')          #链接写到link文档中

            for i in range(0,len(datahref)):
                link_ultimate=datahref[i]
                print(datahref[i])
                name=self.getname(link_ultimate)
                title_all.append(name)
                file.write(name+link_ultimate)
            n=n+1
        except Exception as e:
            print(e)
        return n

    def getname(self, url):  # 获取每一个公众号的名称
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            data = response.read()
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            tag = soup.strong
            name = tag.contents[0].replace(" ","").replace("\n",'')         #用replace方法
            # print(tag.contents[0])
            print(name)
            # print(tag.contents)
        except Exception as e:
            print(e)
        return name

if __name__=='__main__':
    # title=input("输入要搜索的内容")
    spider = Spider()
    ip_list=spider.get_ip_list()
    i=1
    while(i<11):
        try:
            proxy = spider.get_random_ip(ip_list)  # 获取随机ip
            url='http://weixin.sogou.com/weixin?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&type=1&page='+str(i)+'&ie=utf8&p=76331800&dp=1'
            i=spider.start(url,proxy,i)
        except Exception as e:
            print(e)

