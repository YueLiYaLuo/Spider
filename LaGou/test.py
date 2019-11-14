#伪装发送请求过程中传输的data的值可以直接加在post链接的后面
#1.获取到岗位大致信息    get_PositionInfo()
#2.

import json
import requests
import spider.LaGou.lagouInfo.getCookies as gc
import time
import random
def get_PositionInfo():
    header = {
    'Accept':'application/json, text/javascript, */*;q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':'50',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
    }
    cookie = gc.init_cookies()

    datas={
    'first': 'true',
    'kd':'java'  #职位名称
    }

    allCompany = []
    # 岗位id
    positionId = ''
    # 岗位名称
    positionName = ''
    # 薪水
    salary = ''
    # 学历
    education = ''
    # 岗位优势
    positionAdvantage = ''
    # 岗位类型
    firstType = ''
    # 技能标签
    skillLables = ''
    # 是否全职
    jobNature = ''
    # 工龄
    workYear = ''
    # 公司全称
    companyFullName = ''
    # 公司logo
    companyLogo = ''
    # 公司城市
    city = ''
    # 公司标签
    companyLabelList = ''
    # 公司规模
    companySize = ''
    # 公司资金状况，是否融资等
    financeStage = ''

    for i in range(1, 2):
        print(i)
        # 添加随机延时
        # time.sleep(random.randint(3, 6))
        ret = requests.post("https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&pn=" + str(i),
                            data=json.dumps(datas), headers=header, cookies=cookie)
        temp_dic = ret.json()
        companyLogo = temp_dic['content']['hrInfoMap']
        allCompany = temp_dic['content']['positionResult']['result']
        for company in allCompany:
            url= companyLogo[str(company['positionId'])]['portrait']
            print(url)



if __name__=="__main__":
    get_PositionInfo()