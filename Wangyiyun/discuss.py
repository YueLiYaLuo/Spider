import urllib.request
from bs4 import  BeautifulSoup
import urllib.parse


class GetDissc(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self,url):
        try:
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            data=response.read()
            title=[]
            href=[]
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            #print(soup)
            hrefs = soup.find_all('a',class_='s-fc5 post')
            print(hrefs)
            # print(titles)
            for link in hrefs:
                title.append(link.get_text().replace("\n",""))
                #print(link.get_text())      #获取标题

            for link in hrefs:
                href.append(link.get("href")) #获取到相对路径
            url0="http://study.163.com"
            url_file = open('content2.txt', 'a',encoding="utf-8")
            for i in range (len(title)):
                # url_file.write("标题："+title[i]+"\t"+"链接:"+url0+href[i]+"\n")
                url_file.write(title[i])
                url2=url0+href[i]
                content=self.getContent(url2)
                for cont in content:
                    url_file.write(cont+"\n")
            url_file.close()
        except Exception as e:
            print(e)

    def getContent(self,url):       #获取帖子中的内容
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            data = response.read()
            content = []
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            # print(soup)
            contents = soup.find_all('div', class_='j-content f-richEditorText')
            for cont in contents:
                content.append(cont.get_text().replace("\n", ""))   #去掉多余的回车符
                print(cont.get_text().replace("\n", ""))
            return content
        except Exception as e:
            print(e)



getDissc=GetDissc()
for i in range(1):     #i为爬取页数
    url="http://study.163.com/forum/index.htm?cid=1003590004&p="+str(i)
    getDissc.start(url)

# url2="http://study.163.com/forum/detail/1004586205.htm"
# getDissc.getContent(url2)                             #单独测试获取内容模块