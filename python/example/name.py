# 字符串大小写转换
name = 'luo xiaoguang'
print(name.title())
name = name.title()
print(name.istitle())
print(name.upper())
print(name.lower())

# 拼接字符串
first_name = "luo"
last_name = "xiaoguang"
full_name = first_name + " " +last_name
print("Welcome Come " + full_name.title() + " To Python World!")

# 打印转义字符
print("\t Good!")
print("\n\t Good!")


# 删除指定字符,类似php的trim
user_name = 'test\t\n'
print(user_name)
user_name = user_name.strip()
print(user_name)
user_name = user_name.strip('t')
print(user_name)