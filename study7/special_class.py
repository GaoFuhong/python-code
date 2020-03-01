# Author:Fuhong Gao

#创建类的普通方法：
'''
class Foo(object):
    def __init__(self, name):
        self.name = name
f = Foo("Fuhong Gao")
print(type(f)) #f对象由Foo类创建
print(type(Foo)) #Foo类由type类创建
'''

#创建类的特殊方法：
def __init__(self, name,age):
    self.name = name
    self.age = age
def func(self):
    print("Hello,%s." %self.name)
Foo = type('Foo',(object,),{'talk':func,
                     '__init__':__init__})
print(type(Foo))
f = Foo('Fuhong Gao',22)
f.talk()