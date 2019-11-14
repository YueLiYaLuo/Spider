import os


def file_name(file_dir):
    bookname = []
    n=0
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        n+=1
        if(n==1):
            bookname = dirs
    print(bookname)

    for temp in bookname:
        print(temp.split("_")[0])

file_name("E:\documents")

