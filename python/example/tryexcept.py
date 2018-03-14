# 异常处理
#捕获所有异常错误
try:
    res = 5/2
except:
    print("出错")
else:
    print("结果为:" + str(res))

#捕获打开文件不存在时的异常错误
try:
    with open("huha.txt") as file_obj:
        contens = file_obj.readlines()

except FileNotFoundError:
    print("文件不存在")

else:
    print(contens)


#计算文档词语数
try:
    with open("file/novel.txt") as f_obj:
        con = f_obj.read()
except FileNotFoundError:
        #pass语句 不做任何处理
        # print("文件不存在,读取错误")
        pass
else:
    words = con.split()
    totoal_num = len(words)
    print("共有词语个数:"+ str(totoal_num))