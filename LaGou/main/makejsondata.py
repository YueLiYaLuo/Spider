'''
该函数实现功能：实现对json数据的转化
源数据格式：
"5309423	大数据Java工程师	8k-16k	本科	六险一金，补贴，带薪年假	开发|测试|运维类		全职	1-3年	成都数联铭品科技有限公司	成都	带薪年假/绩效奖金/扁平管理/定期体检	150-500人	C轮	"
json数据格式：第一行为index信息，第二行为document的具体内容
{"index": {"_id":"1"}}
{"positionId":"5309423","positionName":"大数据Java工程师","salary":"8k-16k","education":"本科","positionAdvantage":"六险一金，补贴，带薪年假","firstType":"开发|测试|运维类","skillLables":"","jobNature":"全职","workYear":"1-3年","companyFullName":"成都数联铭品科技有限公司","city":"成都","companyLabelList":"带薪年假/绩效奖金/扁平管理/定期体检","companySize":"150-500人","financeStage":"C轮","detailInfo":"https://www.lagou.com/jobs/5309423.html"}
'''


def transforJsonData():
    # 爬虫爬取到的源数据
    readFile = open("intro(java_bigdata).txt", "r", encoding='gbk')
    # 目标写入json文件
    writeFile = open("jsonData.json", "a", encoding='utf-8')
    indexn = 1
    for line in readFile:
        # line = "5309423	大数据Java工程师	8k-16k	本科	六险一金，补贴，带薪年假	开发|测试|运维类		全职	1-3年	成都数联铭品科技有限公司	成都	带薪年假/绩效奖金/扁平管理/定期体检	150-500人	C轮	"
        splitline = line.split("\t")
        splitline[14] = "https://www.lagou.com/jobs/" + splitline[0] + ".html"
        # 每一个document的属性
        title = ["positionId", "positionName", "salary", "education", "positionAdvantage", "firstType", "skillLables",
                 "jobNature", "workYear", "companyFullName", "city", "companyLabelList", "companySize", "financeStage",
                 "detailInfo"]

        string = ""
        for i in range(0, len(title)):
            if (i != len(title) - 1):
                info = "\"" + title[i] + "\"" + ":" + "\"" + splitline[i] + "\","
            else:
                info = "\"" + title[i] + "\"" + ":" + "\"" + splitline[i] + "\""
            string = string + info
        # index属性
        indexData = "{\"index\": {\"_id\":" + "\"" + str(indexn) + "\"" + "}}"
        print(string)
        indexn = indexn + 1
        print(indexData)
        # 写入文件
        writeFile.writelines(indexData + "\n")
        writeFile.writelines("{" + string +"}" + "\n")

    readFile.close()
    writeFile.close()


if __name__ == "__main__":
    transforJsonData()
