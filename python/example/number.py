import this

#数字类型
#假如第一天给你0.1元,第二天是第一天的两倍,30天后你有多少钱
i = 0
result = []
start = 0.1
total = 0
while(i<30):
    if(i==0):
        result.append(start)
    else:
        result.append(result[-1]*2)
    print("第" , i+1 , "天:" , result[i])
    total = total + result[i]
    i=i+1

print("共计:", total)


#使用加号连接字符串时,遇到连接的变量是整形时会报错,以下为解决办法
#办法1
# age = 23
# msg = "祝你" + str(age) + "岁生日快乐!"
# print(msg)
#
#
# print(3/2)