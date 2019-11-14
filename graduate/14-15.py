import re

pattern = re.compile('["设计""实现"]')
count = 0
with open("title.txt","r",encoding="utf-8") as openfile:
    for line in openfile:
        if pattern.findall(line):
            count =count + 1
            print(pattern.findall(line))

print(count)
