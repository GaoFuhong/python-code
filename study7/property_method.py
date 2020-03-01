# Author:Fuhong Gao
#属性方法
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None #设置一个静态变量
    @property #把一个方法变成一个静态属性
    def eat(self):
        print("%s is eatting %s..." %(self.name,self.__food))
    @eat.setter #修改
    def eat(self,food):
        print('set to food:' ,food)
        self.__food = food
    def __call__(self, *args, **kwargs): #可在对象后面加括号，直接出发执行
        print("running call...",args,kwargs)
    @eat.deleter
    def eat(self):
        del self.__food
        print("finish deleting!")
    def __str__(self): #在打印对象时，默认输出该方法的返回值
        return "<obj:%s>" %self.name
d1 = Dog('Xiaohuang')
d1.eat
d1.eat = 'bone' #可以对food赋值
d1.eat
d1(1,2,3,name='gfh') #对象后面加括号
print(Dog.__dict__) #打印类的所有属性，不包括实例属性
print(d1.__dict__) #打印所有实例属性，不包括类属性
print(d1)
del d1.eat
d1.eat
