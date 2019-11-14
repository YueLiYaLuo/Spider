#伪装发送请求过程中传输的data的值可以直接加在post链接的后面
#1.获取到岗位大致信息    get_PositionInfo()
#2.

import json
import requests
import spider.LaGou.lagouInfo.getCookies as gc
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
    'Referer':'https://www.lagou.com/jobs/list_java%E5%A4%A7%E6%95%B0%E6%8D%AE?oquery=%E5%A4%A7%E6%95%B0%E6%8D%AE&fromSearch=true&labelWords=relative&city=%E6%9D%AD%E5%B7%9E',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
    }
    #payload={"pageIndex":1,"pageSize":50,"relativeOffset":0,"keyword":"python","searchTimeType":-1,"orderType":5,"priceType":-1,"activityId":0,"qualityType":0}

    cookie = gc.init_cookies()

    datas={
    'first': 'true',
    'kd':'java'  #职位名称
    }

    for i in range(1,2):
        ret = requests.post("https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&pn="+str(i), data=json.dumps(datas), headers=header, cookies=cookie)
        temp_dic = ret.json()
        all = temp_dic['content']['hrInfoMap']
        #dict_values([{'portrait': 'i/image2/M00/2A/E7/CgotOVoqNKCAAStRAAB3fq6Sago375.png', 'phone': None, 'userId': 5375135, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '熊芬', 'canTalk': True, 'positionName': '行政人事专员'}, {'portrait': 'i/image2/M01/8C/3C/CgoB5luYzt-AU2dUAAFbvo0p7jY087.jpg', 'phone': None, 'userId': 11365052, 'receiveEmail': None, 'userLevel': 'G1', 'realName': 'Rita', 'canTalk': True, 'positionName': '人事行政经理'}, {'portrait': 'i/image2/M01/D6/2C/CgotOVxSoEWAEIyeAABUp7JoDTI447.png', 'phone': None, 'userId': 8619730, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '茶白', 'canTalk': True, 'positionName': '人事主管'}, {'portrait': 'i/image2/M01/5C/03/CgotOVsrjcCAH59vAAA5rxXgbII100.png', 'phone': None, 'userId': 11068980, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '李经理', 'canTalk': True, 'positionName': '总经理助理'}, {'portrait': 'i/image2/M01/AB/BC/CgoB5lvuYAWAf_B7AABRX5PWOXI990.jpg', 'phone': None, 'userId': 8460277, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '汪增馨', 'canTalk': True, 'positionName': 'HR'}, {'portrait': 'i/image3/M00/3E/02/CgpOIFqwvH-AAzjSAADItERdTUg286.jpg', 'phone': None, 'userId': 5502106, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '胡文静', 'canTalk': True, 'positionName': '人事经理'}, {'portrait': 'i/image/M00/03/DF/Cgp3O1bEIUiAA1cHAABS53UVWx0810.jpg', 'phone': None, 'userId': 322709, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '李逸倩', 'canTalk': True, 'positionName': 'HR'}, {'portrait': None, 'phone': None, 'userId': 11962712, 'receiveEmail': None, 'userLevel': 'G1', 'realName': 'Yang', 'canTalk': True, 'positionName': 'HRG'}, {'portrait': 'i/image2/M01/9E/63/CgotOVvNfdeAT7HxAAA56ukbxTM940.png', 'phone': None, 'userId': 6611812, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '七月', 'canTalk': True, 'positionName': '招聘'}, {'portrait': 'i/image2/M01/7B/83/CgotOVtyXi-ASDoFAAANPwy_734354.jpg', 'phone': None, 'userId': 10632323, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '蒋女士', 'canTalk': True, 'positionName': '人事专员'}, {'portrait': 'i/image2/M01/82/6A/CgoB5luDnPSAKFgqAAQSG38RirM841.jpg', 'phone': None, 'userId': 11528038, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '糖糖', 'canTalk': True, 'positionName': '人事行政助理'}, {'portrait': None, 'phone': None, 'userId': 2492545, 'receiveEmail': None, 'userLevel': 'G1', 'realName': 'cjw', 'canTalk': True, 'positionName': 'CEO'}, {'portrait': 'i/image2/M01/D8/EB/CgotOVxjZ-iATRA7AAKMQn8ijkg117.jpg', 'phone': None, 'userId': 12479979, 'receiveEmail': None, 'userLevel': 'G1', 'realName': '梁智慧', 'canTalk': True, 'positionName': '人事'}, {'portrait': None, 'phone': None, 'userId': 3931507, 'receiveEmail': None, 'userLevel': 'G1', 'realName': 'job', 'canTalk': True, 'positionName': ''}, {'portrait': 'i/image3/M00/0C/6F/CgpOIFpm2Z-AGKsUAAB829V1Enk307.jpg', 'phone': None, 'userId': 1736455, 'receiveEmail': None, 'userLevel': 'G1', 'realName': 'headerhr', 'canTalk': True, 'positionName': ''}])
        print(all.values())
        for each in all:
            print(all[each]['portrait'])

if __name__=="__main__":
    get_PositionInfo()