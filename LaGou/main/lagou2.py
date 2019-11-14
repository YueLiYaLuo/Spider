# 伪装发送请求过程中传输的data的值可以直接加在post链接的后面
# 1.获取到岗位大致信息    get_PositionInfo(workname)


import json
import requests


def get_PositionInfo(workname):
    header = {
        'Accept': 'application/json, text/javascript, */*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '50',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie':'_ga=GA1.2.1828083553.1545226955; user_trace_token=20181219214233-f04f8b9d-0393-11e9-94bc-5254005c3644; LGUID=20181219214233-f04f8f05-0393-11e9-94bc-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169488304a0ac-079ccc2efeb972-b79183d-921600-169488304a16aa%22%2C%22%24device_id%22%3A%22169488304a0ac-079ccc2efeb972-b79183d-921600-169488304a16aa%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1495837627.1552184197; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551765155,1551765162,1551942194,1552184198; LGSID=20190310101637-88861f35-42da-11e9-9718-525400f775ce; JSESSIONID=ABAAABAAADEAAFIAA5F05BA0E6C37EEE48A6CDFAEC365A2; OUTFOX_SEARCH_USER_ID_NCOO=1297070174.901033; _gat=1; LGRID=20190310110127-cc40fc35-42e0-11e9-90a7-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552186888',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_java%E5%A4%A7%E6%95%B0%E6%8D%AE?oquery=%E5%A4%A7%E6%95%B0%E6%8D%AE&fromSearch=true&labelWords=relative&city=%E6%9D%AD%E5%B7%9E',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # payload={"pageIndex":1,"pageSize":50,"relativeOffset":0,"keyword":"python","searchTimeType":-1,"orderType":5,"priceType":-1,"activityId":0,"qualityType":0}

    datas = {
        'first': 'true',
        'kd': 'java大数据'  # 职位名称
    }

    allCompany = []
    positionId = ''  #岗位id
    positionName = ''  #岗位名称
    salary = ''  # 薪水
    education = ''  # 学历
    positionAdvantage = ''  # 岗位优势
    firstType = ''  # 岗位类型
    skillLables = ''  #技能标签
    jobNature = ''  # 是否全职
    workYear = ''  # 工龄
    companyFullName = ''  # 公司全称
    city = ''  #公司城市
    companyLabelList = ''  # 公司标签
    companySize = ''  # 公司规模
    financeStage = ''  # 公司资金状况，是否融资等

    try:
        for i in range(0,200):       #爬取页数(共200页)
            print(i)
            response = requests.post(
                "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&kd="+workname+"&pn=" + str(i),
                data=json.dumps(datas), headers=header)
            # print(response.content)
            if response.content:         #如果response内有返回值
                temp_dic = response.json()
                allCompany = temp_dic['content']['positionResult']['result']
                # 返回一个包含所有公司信息的list[{companyShortName: "车纷享", createTime: "2018-12-24 14:11:48", companySize: "150-500人", approve: 1,…},…]
                for company in allCompany:
                    # print(company)
                    with open("intro.txt",'a') as file :
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
    except Exception:
        print(Exception)


if __name__ == "__main__":
    workname = "java大数据"
    get_PositionInfo(workname)
