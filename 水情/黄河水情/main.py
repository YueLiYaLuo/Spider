import urllib
from bs4 import BeautifulSoup
import re
import requests
import json


class 水情(object):
    def __init__(self):
        self.headers = {
        }
        self.url = "http://61.163.88.227:8006/hwsq.aspx"

    # 第一次访问获取到__VIEWSTATE,__VIEWSTATEGENERATOR,__EVENTVALIDATION值
    def 第一次获取传入参数(self):
        # 获取实体名字
        try:
            request = urllib.request.Request(self.url, headers=self.headers)
            # 伪装请求
            response = urllib.request.urlopen(request)
            # 模仿浏览器访问，返回网页数据
            data = response.read().decode('utf-8')
            VIEWSTATE = re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', data,
                                   re.I)
            VIEWSTATEGENERATOR = re.findall(
                r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', data,
                re.I)
            # <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />
            EVENTVALIDATION = re.findall(
                r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', data, re.I)
            print("VIEWSTATE:",VIEWSTATE[0])
            print("VIEWSTATEGENERATOR:",VIEWSTATEGENERATOR[0])
            print("EVENTVALIDATION:",EVENTVALIDATION[0])
            return VIEWSTATE[0], VIEWSTATEGENERATOR[0], EVENTVALIDATION[0]
        except Exception as e:
            print(e)

    def 获取数据(self):
        VIEWSTATE, VIEWSTATEGENERATOR, EVENTVALIDATION = self.第一次获取传入参数()
        import requests
        import json
        from urllib import parse
        # 定义请求地址
        url = "http://61.163.88.227:8006/hwsq.aspx"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "14110",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1723320388.3151002; ___rl__test__cookies=1590475533193",
            "Host": "61.163.88.227:8006",
            "Origin": "http://61.163.88.227:8006",
            "Referer": "http://61.163.88.227:8006/hwsq.aspx",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
            "X-MicrosoftAjax": "Delta=true",
            "X-Requested-With": "XMLHttpRequest"}
        # 通过字典方式定义请求body
        FormData = {
            "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
            "__EVENTVALIDATION":EVENTVALIDATION,
            "__VIEWSTATE":VIEWSTATE,
            "ctl00$ContentLeft$menuDate1$TextBox11": "2020-05-07",
            "ctl00$ScriptManager1": "ctl00$ScriptManager1|ctl00$ContentLeft$Button1",
            # "__ASYNCPOST":"false",
            "ctl00$ContentLeft$Button1":"查询"
        }
        data = parse.urlencode(FormData)
        # 请求方式
        ret = requests.post("http://61.163.88.227:8006/hwsq.aspx", data=json.dumps(data), headers=headers)
        # print(ret.text)

        date = re.findall(r'<div class=\'secTitle\'>(.*?)</div>', ret.text,
                                   re.I)
        print(date)
        # soup = BeautifulSoup(ret.text, 'html.parser')
        # dataList  = soup.findAll("td",align = 'left')
        # for data in dataList:
        #     print(data)
        #     print(data.get_text())



if __name__ == '__main__':
    水情 = 水情()
    水情.获取数据()
