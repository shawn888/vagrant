# 字典
dict = {'name': 'zhang san', 'age':18, 'height':180, 'is_marry': False}

# print(dict["name"])


dict["address"] = '北京市'
print(dict)

dict1 = {}
dict1["comment"] = 'this is very good car!'
dict1["brand"] = 'buick'
dict1["chines_name"] = '昂科威'
dict1["price"] = 230000
print(dict1)
# del dict1["comment"]
# print(dict1)

#产生一个键值对列表
# print(dict1.items())
for key,value in dict1.items():
    print("\nThis is "+
          key.title() + ":" +
          str(value) +
          ".")

# print(dict1.keys())
# print(dict1.values())

#将一组字段初始化为一个新字典,可以给出初始化的值
# print(dict1.fromkeys(dict1, '2'))

texts = {
    'japan':'python',
    'shines':'c',
    'esa':'php',
    'psa':'go',
    'hsa':'go',
}

#使用sorted来获得特定顺序的键值对列表
for key, value in sorted(texts.items()):
    print(key+":"+value)

#set 剔除重复项目
print(texts.values())
print(set(texts.values()))

#嵌套字典
text1 = {'name': 'zhang san', 'age':18, 'height':180, 'is_marry': False}
text2 = {'name': 'li si', 'age':28, 'height':170, 'is_marry': True}
text3 = {'name': 'wang wu', 'age':40, 'height':166, 'is_marry': True}

parsons = [text1, text2, text3]