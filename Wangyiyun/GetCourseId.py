import requests
import json


def get_CourseInfo():
    header = {
    'Accept':'application/json',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'120',
    'Content-Type':'application/json',
    'Cookie':'_ntes_nnid=3c6f2eb7b55a1526fe4facacd4d8cc50,1518179291225; _ntes_nuid=3c6f2eb7b55a1526fe4facacd4d8cc50; _ngd_tid=fdrZk5OlvSof3SmufM9MbJ466cZQcGDW; __f_=1518954981586; EDUWEBDEVICE=618213db6c97400f8b475d554bef25ad; usertrack=ezq0pVqfvXQl3B8LButWAg==; _ga=GA1.2.1372650944.1520418177; nts_mail_user=chen944522285@163.com:-1:1; __utmz=129633230.1524406984.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); STUDY_MIND_TELBIND_CLOSE=1; __e_=1525143806740; NTES_STUDY_YUNXIN_ACCID=s-10862013; NTES_STUDY_YUNXIN_TOKEN=7bb239a27288bc6af6ba6c7ec27a8acd; NTESSTUDYSI=b6b127c835484d81b108d8dfce09cca5; __utma=129633230.776429048.1519811025.1525231966.1525252220.7; __utmc=129633230; _qddaz=QD.dejj7d.8lvbdl.jgoyktc7; _qddab=3-vjle9i.jgoyktcb; _qddamta_800158890=3-0; STUDY_UUID=9336fc9a-f628-430d-8e71-75f093744dee; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cDovL3N0dWR5LjE2My5jb20vZm9ydW0vaW5kZXguaHRtP2NpZD0zODEwMDYmcD01"; __utmb=129633230.78.7.1525259306577',                             #input your cookie
    'edu-script-token':'b6b127c835484d81b108d8dfce09cca5',                   #input your token
    'Host':'study.163.com',
    'Origin':'http://study.163.com',
    'Pragma':'no-cache',
    'Referer':'http://study.163.com/courses',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    payload={"pageIndex":1,"pageSize":50,"relativeOffset":0,"keyword":"python","searchTimeType":-1,"orderType":5,"priceType":-1,"activityId":0,"qualityType":0}

    data_list = []
    course_Info=[]  #双数下标为课程名，单数下标为课程号
    count=0
    for i in range(8):         #i为访问的页数
        ret = requests.post("http://study.163.com/p/search/studycourse.json", data=json.dumps(payload), headers=header)
        payload["pageIndex"] = int(payload["pageIndex"])+1
        temp_dic = ret.json()
        # print(temp_dic)       #总的字典列表
        # print(type(temp_dic))
        if temp_dic["message"]!="ok":   #判断json中的数据是否可读取
            print("error "+temp_dic["message"])
        data_list.append(temp_dic["result"]['list'])
        for item in temp_dic["result"]['list']:
            count +=1               #count记录一共多少条数据
            print("CourseName:"+item["productName"])
            course_Info.append(item["productName"])
            # print(item["description"]+"\n")
            print("CourseId:"+str(item["courseId"]))
            course_Info.append(str(item["courseId"]))     #int形式的courseId转换为str形式便于后续操作
            data_list.append(item)
    print(count)
#结果写入Course_Info中
    file_name = open('CourseInfo.csv', 'a', encoding="utf-8")
    for i in range(len(course_Info)):
        file_name.write(course_Info[i]+"\n")
    return course_Info

if __name__=="__main__":
    get_CourseInfo()