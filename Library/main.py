'''
爬取自己大学四年看的书
直接将网页保存到本地然后提取数据
'''
from PIL import Image
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
# 第一步获取数据
def get_LibraryInfo():

    dataFile = open("page.txt","r",encoding='utf-8')
    try:
        # 模仿浏览器访问，返回网页数据
        data = dataFile
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        # 实例化beautifulsoup对象
        print(soup.get_text())

    except Exception as e:
        print(e)

# 第二步数据整理
def dataFormat():
    lineNum = 1
    with open("libraryData.txt", "r", encoding='utf-8') as readFile:
        with open("data.txt", "a", encoding='utf-8') as writeFile:
            for line in readFile:
                print(line)
                if lineNum % 9 != 0:
                    writeFile.write(line.replace("\n", "") + "\t")
                else:
                    writeFile.writelines("\n")
                lineNum += 1

# 第三步分类，将专业书籍和非专业书籍分开，然后将
def classify():
    other_Book = open("other_Book.txt", "a", encoding="UTF-8")
    study_Book = open("study_Book.txt", "a", encoding="UTF-8")
    other_datesum = 0
    study_datesum = 0
    with open("data.txt", "r", encoding="UTF-8") as dataFile:
        for line in dataFile:
            date1 = line.split("\t")[4]
            date2 = line.split("\t")[5]
            # 当前书籍花费的时间
            days = Caltime(date1,date2)
            if line.split("\t")[6][0:2] == "自科":
                study_Book.writelines(line.split("\t")[2]+"\t"+line.split("\t")[3]+"\t"+str(days)+"\n")
                study_datesum += days
            else:
                other_Book.writelines(line.split("\t")[2]+"\t"+line.split("\t")[3]+"\t"+str(days)+"\n")
                other_datesum += days
    print("专业学习书籍所有时间为:")
    print(study_datesum)
    print("非专业学习书籍所有时间为:")
    print(other_datesum)

# 计算每一本书花费的时间
def Caltime(date1, date2):
    import time
    import datetime
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    # 返回两个变量相差的值，就是相差天数
    # print((date2 - date1).days)  # 将天数转成int型
    return (date2 - date1).days

# 第四步将标题提取出来并分词，只取专业书籍的关键字
def purge():
    from jieba import analyse
    textrank = analyse.textrank
    writeFile = open("purge_study_Book.txt","a",encoding="UTF-8")
    with open("study_Book.txt","r",encoding="UTF-8") as readFile :
        for line in readFile:
            keywords = textrank(line.split("\t")[0])
            if(keywords):
                writeFile.writelines(",".join(keywords)+"\n")
                print(keywords)
    writeFile.close()

#第五步：词云,使用time.jpg当作轮廓图
def drawWordcloud():
    text = open('purge_study_Book.txt','r',encoding="UTF-8").read()
    font = r'C:\Windows\Fonts\STSONG.TTF'       #设置字体，如果不设置字体的话默认无法识别中文
    mask_picture = np.array(Image.open("timg.jpg"))
    wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2,mask=mask_picture).generate(text.lower())

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file('ShowWordcloud.png')


if __name__=="__main__":
    # 提取数据
    # get_LibraryInfo()
    # 数据整理
    # dataFormat()
    # 分类
    # classify()
    # 分词
    # purge()
    # 画词云
    drawWordcloud()