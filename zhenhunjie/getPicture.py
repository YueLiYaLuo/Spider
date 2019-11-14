import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import os, stat

class GetZHJ(object):
    def __init__(self,url):

        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {
            'User-Agent': self.user_agent,
            'Host': 'm.gufengmh.com',
            'Connection': 'keep - alive',
            'Upgrade - Insecure - Requests': 1,
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'Referer': 'http: // m.gufengmh.com / manhua / zhenhunjie / 330728 - 10.html',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Cookie': '___rl__test__cookies = 1534401117048;cfduid = d42e04c9e40e7f1f57383a6e26a8cefad1534400060;UM_distinctid = 165415eefc78c0 - 068c36fee798ca - 37664109 - e1000 - 16541eefcc2dd;OUTFOX_SEARCH_USER_ID_NCOO = 760079480.0985398;CNZZDATA1272617950 = 711383008 - 1534395675 - null % 7C1534401075'
        }
        try:
            self.request = urllib.request.Request(url, headers=self.headers)
            self.response = urllib.request.urlopen(self.request)
            self.data = self.response.read()
            self.soup = BeautifulSoup(self.data, 'html.parser', from_encoding='utf-8')
            # print(soup)
        except Exception as e:
            print(e)

    def GetTitleAndPicUrl(self):        #获取每一张图片的url
        Title0 = self.soup.title.string  # 标题
        PicUrl0 = self.soup.find_all('mip-img')  # 获取图片链接
        Title=" ".join((str(Title0).replace("在线观看-古风漫画网","")))
        PicUrl=PicUrl0[0].get('src')

        print(Title)
        print(PicUrl)

        return Title,PicUrl

    def GetPageNum(self):   #获取每一章节图片的数量
        pageNum = self.soup.find(id="k_total").get_text()
        print(pageNum)

        return int(pageNum)

    def DownloadPictuer(self,Title,PicUrl,i,n):    #下载图片

        img_url = PicUrl
        file_path = 'C:/Users/94452/PycharmProjects/hello_prj4/spider/zhenhunjie/manhua/'+str(n)+Title
        #文件路径
        file_name =i
        #文件名称为这个图片的序号

        try:
            # 是否有这个路径
            if not os.path.exists(file_path):
                # 创建路径
                os.makedirs(file_path)
                # 获得图片后缀
            file_suffix = os.path.splitext(img_url)[1]
            # print(file_suffix)
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            # print(filename)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)

        except IOError as e:
            print("IOError")
        except Exception as e:
            print("Exception")



if __name__ == "__main__":
    n=476705

    m=n+5     #m为爬取的章节数
    while(n<m):
        url = "http://m.gufengmh.com/manhua/zhenhunjie/"+str(n)+".html"

        spider = GetZHJ(url)
        pageNum=spider.GetPageNum()
        # 自动获取到每一章节的页数然后进行遍历下载
        for i in range(0,pageNum+1):
            url="http://m.gufengmh.com/manhua/zhenhunjie/"+str(n)+"-"+str(i)+".html"
            spider = GetZHJ(url)
            Title,PicUrl=spider.GetTitleAndPicUrl()

            spider.DownloadPictuer(Title,PicUrl,i,n)
            print(i)
        n+=1