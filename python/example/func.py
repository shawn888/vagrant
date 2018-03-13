# 函数
def add(a, b = 10):
    result = int(a)+int(b)
    return result



# a = input("请输入数字: ")
# b = input("请再输入数字 ")
# res = add(a, b)
# print("add result:" + str(res))


# def process_list(userlist):
#     for name in userlist:
#         print(name)


users = ["zhangsan", "lisi", "wangwu"]
result_users = []

def check(users, result_users):
    while len(users)>0:
        value = users.pop()
        result_users.append(value)

check(users[:], result_users)
print(users)
print(result_users)


#传元组
def adds(name, *numbers):
    print(name+" result:")
    result = 0
    for num in numbers:
        result+=num
    return result

print(adds("add",1,2,3,4,5))


# 传字典
def getuserinfo(name, **userinfo):
    print("name:"+name+ " info: "+str(userinfo))


getuserinfo("zhangsan", age=18, height='170cm', is_marry=False)
