# Author:Fuhong Gao
import time
#函数即“变量”
# def bar():
#     print('in the bar...')
# def foo():
#     print('in the foo...')
#     bar()
# foo()

#高阶函数
#（1）在不修改被装饰函数源代码的情况下为其添加功能
# def bar():
#     time.sleep(1)
#     print("in the bar...")
# def test1(func):
#     print(func) #打印的是函数bar()的内存地址
#     start_time = time.time()
#     func() #调用函数bar()
#     stop_time = time.time()
#     print('the bar running time is %s' %(stop_time - start_time))
# test1(bar)

#（2）不修改函数的调用方式
def bar():
    print('in the bar...')
bar()
def test2(func):
    print(func) #打印被调用函数的内存地址
    print("新增加的功能。。。")
    return func #返回被调用函数的内存地址
bar = test2(bar) #把test2(bar)的内存地址赋给bar
bar() #重新调用bar()

# func = bar
# func()


#匿名函数
# calc = lambda x:x**3
# # print(calc(3))