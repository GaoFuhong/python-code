# Author:Fuhong Gao
#嵌套函数
# def foo():
#     print("in the foo...")
#     def bar():
#         print("in the bar...")
#     bar()
# foo()

#一个简单的装饰器（注意：在定义函数时，函数名应避免使用test1、rest2...否则容易出错）
import time
def timer(func): #将test1和test2传给func
    #定义一个函数（“变量”）
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func running time is %s" %(stop_time - start_time))
    return deco #返回函数名
@timer  #等价于：test1 = timer(test1)，哪个函数要使用装饰器，就在它的头部加上@timer
def fun1(): #不含参数
    time.sleep(1)
    print("in the test1...")
@timer  #test2 = timer(test2)     test2(name,age) = deco(name,age)
def fun2(name,age): #含参数
    time.sleep(1)
    print("name:",name,"age:",age)
fun1()
fun2("gfh",22)