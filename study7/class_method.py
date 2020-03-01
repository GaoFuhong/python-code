# Author:Fuhong Gao
#类方法
class Dog(object):
    name = "DouDou" #类变量
    def __init__(self,name):
        self.name = name
    @classmethod #类方法，只能访问类变量，不能访问实例变量
    def eat(self):
        print("%s is eatting %s..." %(self.name,'bone'))
d1 = Dog('Xiaohuang')
d1.eat()