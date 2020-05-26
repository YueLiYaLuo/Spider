import urllib
from bs4  import  BeautifulSoup
class Spider(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self,url):
        try:
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            data=response.read()
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            # 一级标题
            print("*"*10+"一级标题"+"*"*10)
            firstlv=soup.find_all('div',class_='firstlv_warpper')
            writeFile = open("data/data.txt","a",encoding="utf-8")
            for first in firstlv:

                # alist = first.find_all('a',class_='fourthlv lowerlv')

                # for a in first:
                #     print(a)
                    # print(a.get_text().replace("\n",""))
                # writeFile.write(first.get_text())
                print(first.get_text())
                print("*"*20)
            writeFile.close()
            # 二级标题
            # print("*"*10+"二级标题"+"*"*10)
            # secondlv = soup.find_all('div', class_='secondlv lowerlv')
            # for second in secondlv:
            #     print(second.get_text().replace("\n", ""))
            # # 三级标题
            # print("*"*10+"三级标题"+"*"*10)
            # thirdlv = soup.find_all('div', class_='thirdlv lowerlv')
            # for third in thirdlv:
            #     print(third.get_text().replace("\n", ""))
            # # 四级标题
            # print("*"*10+"四级标题"+"*"*10)
            # fourthlv = soup.find_all('a', class_='fourthlv lowerlv')
            # for fourth in fourthlv:
            #     print(fourth.get_text().replace("\n", ""))
            #     print(fourth['href'])


        except Exception as e:
            print(e)



url = "https://www.ipaperclip.net/"
spidet = Spider()
spidet.start(url=url)


