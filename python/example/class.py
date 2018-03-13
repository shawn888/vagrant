# 类  面向对象
class Person():
    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age
        self.run_num = 0

    def run(self):
        """模拟走路"""
        print(self.name + " 正在走路~")

    def speak(self):
        """模拟说话"""
        print(self.name + " 正在说话~")

    def get_run_num(self):
        """模拟获取用户行进的里程数"""
        print(self.name + " 行进了" + str(self.run_num) + "公里~")

    def update_run_num(self, num):
        """更新行进里程数"""
        if num < self.run_num:
            print("行进里程不能越走越少~")
        else:
            self.run_num += num


# lisi = Person("lisi", 18)
# lisi.run()
# lisi.speak()
#
# # lisi.run_num=100
# lisi.update_run_num(1)
# lisi.get_run_num()
# lisi.update_run_num(5)
# lisi.get_run_num()
#


#超人
class Cperson(Person):
    """超人"""
    def __init__(self, name, age):
        """初始化父类属性"""
        super().__init__(name, age)
        self.battery = Battery()


    def fly(self):
        """超人会飞"""
        self.battery.size = 50
        print(self.name + " 正在飞行~")

    def speak(self):
        """超人说话"""
        print(self.name + " 正在说火星语")



class Battery():

    def __init__(self, size = 100):
        """初始化电池容量"""
        self.size = size

    def get_size(self):
        if self.size <= 50:
            print("电量还剩"+ str(self.size) + '%, 请充能~')
        else:
            print("电量充足~")

fly_person = Cperson("emmm", 999)
fly_person.speak()
fly_person.fly()
# fly_person.battery.size = 50
fly_person.battery.get_size()