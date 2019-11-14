from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from jieba import analyse

#分词生成purgeTitle.txt
def purgeWord():
    textrank = analyse.textrank
    writefile = open("purgeTitle.txt","a+",encoding="UTF-8")
    with open("title.txt","r",encoding="UTF-8") as file:
        for line in file:
            keywords = textrank(line)
            writefile.writelines(",".join(keywords)+"\n")
            print(keywords)
    writefile.close()

#词云,使用time.jpg当作轮廓图
def drawWordcloud():
    text = open('purgeTitle.txt','r',encoding="UTF-8").read()
    font = r'C:\Windows\Fonts\STSONG.TTF'       #设置字体，如果不设置字体的话默认无法识别中文
    mask_picture = np.array(Image.open("1.png"))
    wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2,mask=mask_picture).generate(text.lower())

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file('ShowWordcloud.png')

if __name__=="__main__":
    #purgeWord()
    drawWordcloud()