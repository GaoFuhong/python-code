# Author:Fuhong Gao
class Role:
    n = 123  #类变量
    n_list = []
    name = "类name"
    def __init__(self,name,role,weapen,life_value = 100,money = 10000):
        #构造函数，在实例化时做一些初始化的工作
        self.name = name #实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapen = weapen
        self.__life_value = life_value #加两个下划线变成私有属性，外部不能访问
        self.money = money
    def __del__(self):
        #析构函数，在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作，如关闭数据路连接、打开的临时文件
        print("%s died..." %self.name)
    def show_status(self): #写一个方法对私有属性进行修改和查看
        self.__life_value  -= 50
        print("%s's life_value:%s" %(self.name,self.__life_value))
    def shot(self): #类的方法，功能（动态属性）
        print("shooting...")
    def got_shot(self):
        print("ah...I got shot!")
    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))
print(Role.n, Role.name)
r1 =Role("Gu Xiao","police","AK47") #实例化（初始化了一个类，造了一个对象）
r1.n = "abc" #相当于在对象r2里创建了一个新的变量n
r1.n_list.append("from r1")
print(r1.n, r1.name, r1.n_list) #对象先找实例变量，再找类变量
r1.buy_gun("AK47")
del r1 #删除实例r1，随即执行析构函数
r2 =Role("Fuhong Gao","terrorist","B22")
r2.name = "San Zhang" #可以修改实例变量
r2.body_armor = True
print(r2.weapen)
# del r2.weapen  删除变量
r2.n_list.append("from r2")
r2.got_shot()
r2.show_status()
print(r2.name,r2.body_armor, r2.n, r2.n_list)
print(Role.n_list)