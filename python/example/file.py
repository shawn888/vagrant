# 文件操作
# with open('file/test.txt') as file_object:
#     """逐行读取"""
    # for line in file_object:
    #     print(line.strip())
    # """文件全部读取"""
    # contents = file_object.read()
    # print(contents.strip())

    # """读取赋值到列表"""
    # lines = file_object.readlines()



# pi = ''
# for line in lines:
#     pi+=line.strip()



# """查找生日是否出现再圆周率里"""
# birthday = input("you birthday: ")
# if birthday in pi:
#     print("happy birthday to you~")
# else:
#     print("not you birthday")


# print(pi[:20])
# print(len(pi))

with open("file/write.txt", 'a') as file_object:
    # file_object.write("\nWelcome to beijing!")
    wirte_lines = ["\nhello\n", "good\n", "thanks\n"]
    file_object.writelines(wirte_lines)
