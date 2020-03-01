# Author:Fuhong Gao
#继承
# class People: 经典类
class People(object): #新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
    def eat(self):
        print("%s is eatting..."%self.name)
    def talk(self):
        print("%s is talking..."%self.name)
    def sleep(self):
        print("%s is sleeping..."%self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s makes friends with %s" %(self.name,obj.name))
        self.friends.append(obj)

class Man(People,Relation): #多继承，顺序从左到右
    def __init__(self,name,age,money):
        People.__init__(self,name,age)
        # super(Man,self).__init__(name,age) 另一种继承父类的方法
        self.money = money
        print("%s has %s yuan!" %(self.name,self.money))
    def handle(self): #在子类新增方法
        print("%s is handling goods..." %self.name)
    def talk(self): #重构父类的方法
        People.talk(self)
        print("resting...")

class Woman(People,Relation):
    def sing(self):
        print("%s is singing..." %self.name)

m1 = Man("Fuhong Gao",22,100)
m1.eat()
m1.handle()
m1.talk()

w1 = Woman("Xiao Gu",18)
w1.sleep()
w1.sing()

m1.make_friends(w1)
w1.name = "Xiao Gugu"
print(m1.friends[0].name)