# 循环
language = ["c", "c++", "python", "go", "php"]
# for item in language:
    # print("This is "+ item.title())


numbers = list(range(1, 10))
# print(numbers)
# for item in range(1,10):
#     print(item)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))




#假如第一天给你0.1元,第二天是第一天的两倍,30天后你有多少钱
day_money = []
total = 0
for item in range(0,30):
    if(item == 0):
        curr_day_money = 0.1
    else:
        curr_day_money = day_money[-1]*2
    # print("第",item,"天:", curr_day_money)
    day_money.append(curr_day_money)



# print("共计:"+str(sum(day_money)))


# res = []
# for i in range(1,11):
#     value = i**2
#     res.append(value)
    # print(value)

#一行代码实现列表解析
# res = [value for value in range(1,1000000)]
# print(sum(res))
# print(res)

# res = []
# for value in range(3,31):
#     print(str(value)+"%3="+str(value%3))
    # if (value%3==0):
    #     print(value)


#切片
res = list(range(1,10))
# print(res[0:3])
# print(res[:5])
# print(res[5:])
# print(res[-2:])
res1 = [3,5,2,12,3,52,4,75]
res2 = sorted(res1,reverse=True)
# print(res2)
print(res2[:3])
res3 = res2[:3].copy()
print(res3)
#复制一个副本出来,是两个不同的列表,互相不受干扰
# res4 = res1[:]
#下面为赋值方式,两个列表指向同一块数据,修改任何一个都会发生改变
res4 = res1
print(res4)
res4.append(100)
print(res1)
print(res4)


