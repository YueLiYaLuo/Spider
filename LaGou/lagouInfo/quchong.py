'''
对所有的岗位进行去重，添加到Ik分词器中
'''

openfile = open("allPositionName.txt","r",encoding='utf-8')
writefile = open("positionName.txt","a",encoding='utf-8')
positionlist=[]
for line in openfile:
    positionlist.append(line.replace("\n",""))
positionlist=list(set(positionlist))

for each in positionlist:
    print(each)
    writefile.writelines(each+"\n")

print(len(positionlist))