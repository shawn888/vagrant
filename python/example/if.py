# 条件语句

#比较字符串是区分大小写
car = 'Bmw'
print(car =='bmw')

res = ['zhangsan', 'lisi', 'wangwu']
print('lisi1' in res)
print('wangwu' not in res)

bool_val = 'hello'

if bool_val == 0:
    print('hello')
elif bool_val == 'hello':
    print("world")
else:
    print("!!!")


if 'zhangsan' in res:
    print("this is zhangsan")
elif 'lisi' in res:
    print("this is list")
elif 'wangwu' in res:
    print("this is wangwu")


