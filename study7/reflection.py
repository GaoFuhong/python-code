# Author:Fuhong Gao
def bark(self):
    print("%s is barking..." %self.name)
class Dogs(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eatting " %self.name, food)
d = Dogs("Xiaohuang")
choice = input(">>:").strip()
if hasattr(d,choice): #判断d中有没有一个choice字符串对应的属性或方法
    # func = getattr(d,choice) #根据choice字符串去获取d对象里对应属性或方法的内存地址
    # func("bone")
    attr = hasattr(d,choice)
    setattr(d,choice,"Baibai") #对已有的name属性进行修改
    # delattr(d,choice) #删除某属性
else:
    # setattr(d,choice,bark) #添加一个方法
    # d.bark(d)
    setattr(d,choice,10) #添加一个属性
    print(getattr(d,choice))
print(d.name) #打印修改后的属性