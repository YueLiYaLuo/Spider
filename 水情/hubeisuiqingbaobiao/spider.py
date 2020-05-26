import requests
import datetime
from dateutil.relativedelta import relativedelta
def get_RiverReport(url):
    header = {
    'Host': '113.57.190.228:8001',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://113.57.190.228:8001/web/Report/RiverReport',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    }


    # 参数 2019-11-08 08:00
    # "http://113.57.190.228:8001/Web/Report/GetRiverData?date=2019-11-08+08%3A00"
    href = "http://113.57.190.228:8001/Web/Report/GetRiverData?date="+url
    print(href)
    request = requests.post(href,headers=header)
    if request.content:
        temp_dic = request.json()
        print(temp_dic['rows'])
            # for row in temp_dic['rows']:
            #     print(row)       #总的字典列表
    return temp_dic['rows']


if __name__=="__main__":
    # get_RiverReport()
    date = '2019-01-01 00:00:00'

    with open("data.txt","w",encoding="utf-8") as file :
        for i in range (0,1000):
            day = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S' )
            day = (day + relativedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
            str_date = str(day).replace(" ","+").replace(":","%3A")[:-5]
            result = get_RiverReport(str_date)
            file.write(str(result)+'\t'+ str(day) +"\n")
            date = day