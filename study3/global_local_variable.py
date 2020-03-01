# Author:Fuhong Gao
'''
city = "Chengdu" #全局变量
def change_name(name):
    global city #在函数里面强行改全局变量
    city = "Shanghai"
    print("before change:",name,city)
    name = "Fuhong Gao" #局部变量，只在函数里生效（这个函数就是这个变量的作用域）
    print("after change:",name)
name = 'gfh'
change_name(name)
print(name)
print(city)
'''

#不要使用这种方式，不应该在函数里面改全局变量
# def change_name():
#     global name #只在函数里面的全局变量
#     name = 'gfh'
# change_name()
# print(name)

names = ['gfh','gx','zs','ls','ww']
def change_names():
    names[2] = 'wemz'
    print(names)
change_names()
print(names)
#在函数里面可以修改列表、字典、集合、类这样的全局变量