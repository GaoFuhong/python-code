# Author:Fuhong Gao
#静态方法
class Dog(object):
    def __init__(self,name):
        self.name = name
    @staticmethod #实际上跟类没什么关系了，相当于变成了一个独立的函数
    def eat(self):
        print("%s is eatting %s..." %(self.name,'bone'))
d1 = Dog('Xiaohuang')
d1.eat()