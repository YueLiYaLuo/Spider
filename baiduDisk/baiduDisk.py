import urllib.request
from bs4 import  BeautifulSoup
import urllib.parse
class Gethref(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self,url):
        try:
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            data=response.read()
            href=[]
            title=[]
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            #print(soup)
            hrefs = soup.find_all('h3',class_='r')

            print(hrefs)
            for link in hrefs:
                title.append(link.get_text())
                # print(link)
                # print(link.get_text())
        except Exception as e:
            print(e)

if __name__=="__main__":

    href="http://www.daysou.com/s?q=java&start=0&isget=1&tp=baipan&cl=0&line=3"
    getBaiduDisk=Gethref()
    getBaiduDisk.start(href)
