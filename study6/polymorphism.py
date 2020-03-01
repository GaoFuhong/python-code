# Author:Fuhong Gao
#多态
class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass
    @staticmethod
    def animal_talk(obj):
        obj.talk()
class Dog(Animal):
    def talk(self):
        print("%s: Wonf! Wonf!!!" %self.name)

class Cat(Animal):
    def talk(self):
        print("%s: Meow!!!" %self.name)
# def animal_talk(obj):
#     obj.talk()

d1 = Dog("XiaoHuang")
c1 = Cat("DouDou")
Animal.animal_talk(d1)
Animal.animal_talk(c1)
# d1.talk()
# c1.talk()