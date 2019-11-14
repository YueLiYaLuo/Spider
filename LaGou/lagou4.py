# 伪装发送请求过程中传输的data的值可以直接加在post链接的后面
# 1.获取到岗位大致信息    get_PositionInfo(workname)
# 2.根据岗位id获取到工作的具体信息    get_DetailInfo(positionId)
# 第二步中获取信息的时候被反爬虫截止，添加伪ip访问模块破解

import json
import requests
from bs4 import BeautifulSoup
import urllib
import re

class GetLagouInfo():
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.header = {
            'Accept': 'application/json, text/javascript, */*;q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '50',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'JSESSIONID=ABAAABAAAGGABCBCA8D1B7FEBB9509019FDFFC9031E0800; _ga=GA1.2.1828083553.1545226955; _gid=GA1.2.1833427934.1545226955; user_trace_token=20181219214233-f04f8b9d-0393-11e9-94bc-5254005c3644; LGSID=20181219214233-f04f8d51-0393-11e9-94bc-5254005c3644; LGUID=20181219214233-f04f8f05-0393-11e9-94bc-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1545226957; index_location_city=%E6%B1%9F%E8%8B%8F; _gat=1; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1545228270; LGRID=20181219220427-ff9d23a9-0396-11e9-94bc-5254005c3644; SEARCH_ID=b17c4c76195f4a00a184f42cd8214690',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_java%E5%A4%A7%E6%95%B0%E6%8D%AE?oquery=%E5%A4%A7%E6%95%B0%E6%8D%AE&fromSearch=true&labelWords=relative&city=%E6%9D%AD%E5%B7%9E',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_PositionInfo(self, workname):
        datas = {
            'first': 'true',
            'kd': 'java大数据'
            # 职位名称
        }

        allCompany = []
        positionId = ''
        # 岗位id
        positionName = ''
        # 岗位名称
        salary = ''
        # 薪水
        education = ''
        # 学历
        positionAdvantage = ''
        # 岗位优势
        firstType = ''
        # 岗位类型
        skillLables = ''
        # 技能标签
        jobNature = ''
        # 是否全职
        workYear = ''
        # 工龄
        companyFullName = ''
        # 公司全称
        city = ''
        # 公司城市
        companyLabelList = ''
        # 公司标签
        companySize = ''
        # 公司规模
        financeStage = ''
        # 公司资金状况，是否融资等

        try:
            for i in range(0, 3):  # 爬取页数(共30页)
                print(i)
                response = requests.post(
                    "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&kd=" + workname + "&pn=" + str(
                        i),
                    data=json.dumps(datas), headers=self.header)
                if response.content:
                    # 如果response内有返回值
                    temp_dic = response.json()
                    allCompany = temp_dic['content']['positionResult']['result']
                    # 返回一个包含所有公司信息的list[{companyShortName: "车纷享", createTime: "2018-12-24 14:11:48", companySize: "150-500人", approve: 1,…},…]
                    for company in allCompany:
                        # print(company)
                        with open("introxxx.txt", 'a') as file:
                            file.write(str(company['positionId']) + '\t')
                            file.write(company['positionName'] + '\t')
                            file.write(company['salary'] + '\t')
                            file.write(company['education'] + '\t')
                            file.write(company['positionAdvantage'] + '\t')
                            file.write(company['firstType'] + '\t')
                            file.write('/'.join(company['skillLables']) + '\t')
                            file.write(company['jobNature'] + '\t')
                            file.write(company['workYear'] + '\t')
                            file.write(company['companyFullName'] + '\t')
                            file.write(company['city'] + '\t')
                            file.write('/'.join(company['companyLabelList']) + '\t')
                            file.write(company['companySize'] + '\t')
                            file.write(company['financeStage'] + '\t' + '\n')
            file.close()
            # 文件关闭
        except Exception:
            print(Exception)

    def get_DetailInfo(self, positionId):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        headers = {'User-Agent': user_agent}
        detailPositionHref = "https://www.lagou.com/jobs/" + positionId + ".html"

        detailInfo_file = open("detailInfo_data.txt", "a",encoding='utf-8')
        # 存放所有具体信息的文件

        try:
            print(detailPositionHref)
            request = urllib.request.Request(detailPositionHref, headers=headers)
            # 伪装请求
            response = urllib.request.urlopen(request)
            # 模仿浏览器访问，返回网页数据
            data = response.read()
            soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
            # 实例化beautifulsoup对象
            print(soup.get_text())

            job_advantage = soup.find_all('dd', class_='job-advantage')[0].get_text().replace("\n", "")
            job_detail = soup.find_all('div', class_='job-detail')[0].get_text().replace("\n", "")
            job_address = soup.find_all('div', class_='work_addr')[0].get_text().replace(" ", "").replace("\n","").replace("查看地图", "")
            urlinfo = soup.find_all('ul', class_='c_feature')[0].get_text()
            pattern = re.compile(r"[a-zA-z]+://[^\s]*")
            # 由于网站信息的原因这里通过正则表达式来获取url
            job_url = pattern.findall(urlinfo)[0]
            print(job_advantage)
            print(job_detail)
            print(job_address)
            print(job_url)

            detailInfo_file.writelines(job_advantage + "\t" + job_detail + "\t" + job_address + "\t" + job_url + "\n")
            # 写入文件

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # workname = "java大数据"
    getLagou = GetLagouInfo()
    # getLagou.get_PositionInfo(workname)
    getLagou.get_DetailInfo("3786732")