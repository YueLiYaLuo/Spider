# 每访问10条重新获取cookies

from bs4 import BeautifulSoup
import time
import random
import requests
import urllib
import spider.LaGou.lagouInfo.getCookies as gc

def get_DetailInfo(positionId, companyId,cookie):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'

    headers = {'User-Agent': user_agent,
               }
    detailPositionHref = "https://m.lagou.com/jobs/" + positionId + ".html"

    # 存放所有具体信息的文件
    detailInfo_file = open("mobleLagoInfo_Detail.txt", "a+", encoding='utf-8')

    try:
        print(detailPositionHref)
        #添加延时访问防止被封
        time.sleep(random.randint(1, 3))

        # 伪装请求
        request = urllib.request.Request(detailPositionHref, headers=headers)
        # 模仿浏览器访问，返回网页数据
        response = urllib.request.urlopen(request)

        # 实例化beautifulsoup对象
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
        # print(soup.get_text())

        # 根据网页结构job_info中一起获取到的是job_nature，job_workYear和job_education的值
        job_info = soup.find_all('span', class_='text')
        # 将其按照一定的组织结构关系分离出来
        # 工作性质：全职/兼职
        job_nature = job_info[3].get_text()
        # 工作经验
        job_workYear = job_info[4].get_text()
        # 学历要求
        job_education = job_info[5].get_text().replace("\n", "").replace(" ", "")
        # 职业诱惑
        job_temptation = soup.find_all('div', class_='temptation')[0].get_text().replace('\n', '').replace(" ", "")
        # 职位描述
        job_detail = soup.find_all('div', class_='content')[0].get_text().replace("\n","")
        # 公司网址
        job_url = "https://m.lagou.com/gongsi/" + companyId + ".html"

        print('job_nature:', job_nature)
        print('job_workYear:', job_workYear)
        print('job_education:', job_education)
        print('job_temptation:', job_temptation)
        print('job_url', job_url)
        print('job_detail:', job_detail)

        # 写入文件
        detailInfo_file.write(positionId + '\t' + companyId + '\t')
        detailInfo_file.write(job_nature + '\t')
        detailInfo_file.write(job_workYear + '\t')
        detailInfo_file.write(job_education + '\t')
        detailInfo_file.write(job_temptation + '\t')
        detailInfo_file.write(job_url + '\t')
        detailInfo_file.write(job_detail + '\t' + '\n')

    except Exception as e:
        print(e)

def go():
    read_file = open("info.txt", "r")
    # n用来测试计数
    n=0
    for line in read_file:
        positionId = line.split("\t")[0]
        companyId = line.split("\t")[1]
        print(positionId + "\t" + companyId)
        cookie = gc.init_cookies()
        get_DetailInfo(positionId, companyId,cookie)
        print(n)
        n=n+1

if __name__ == "__main__":
    cookies = gc.init_cookies()
    get_DetailInfo('4382581', '1531',cookies)
    # go()