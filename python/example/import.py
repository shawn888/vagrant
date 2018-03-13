# 模块封装
from collections import OrderedDict
from random import randint
# import func_import

# from func_import import getuserinfo as gt

# gt("lisi", age=18, height='170cm', is_marry=True)
# func_import.getuserinfo("lisi", age=18, height='170cm', is_marry=True)

#嵌套字典
l = OrderedDict()
l["comment"] = 'this is very good car!'
l["brand"] = 'buick'
l["chines_name"] = '昂科威'
l["price"] = 230000

for key,item in l.items():
    print(key, item)


#m = randint(1, 10)
#print(m)


class Die():

    def __init__(self, sides = 6):
        """初始化"""
        self.sides = sides
        self.list = []
        self.num = 0

    def roll_die(self):
        """投骰子"""
        while len(self.list) < self.sides:
            value = randint(1,self.sides)
            if value not in self.list:
                self.list.append(value)
            self.num +=1


s = Die(10)
s.roll_die()
print(s.list)
print(s.num)