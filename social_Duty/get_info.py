import urllib.request
import urllib.parse
import re


class Get_info(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}

    def start(self,url):

        writefile=open("2016.txt","a")

        try:
            request=urllib.request.Request(url,headers=self.headers)
            response=urllib.request.urlopen(request)
            data=response.read().decode('gbk')      #返回网页数据
            data1=re.findall(r"industry:(.+?),Hstock", data)
            for i in range(0,len(data1)):
                info=re.findall(r"'(.+?)'", data1[i])
                for i in range(0,len(info)):
                    writefile.write(info[i]+"\t")
                    print(info[i])
                writefile.write("\n")
            # info.append(data2)

        except Exception as e:
            print(e)

info=Get_info()
for i in range(1,178):
    url="http://stockdata.stock.hexun.com/zrbg/data/zrbList.aspx?date=2016-12-31&count=20&pname=20&titType=null&page="+str(i)+"&callback=hxbase_json11528804760761"
    info.start(url)

