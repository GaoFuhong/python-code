# Author:Fuhong Gao
#斐波拉契数列：除第一和第二个数外，任意一个数都可以由前面两个数相加得到。1,1,2,3,5,8,13,21...
#生成器
def fib(max): #max表示生成斐波拉契数列的个数
    n, a, b = 0, 0, 1
    while n < max:
        # print(b) #从1开始打印斐波拉契数列
        yield b #将print换成yield,就变成一个generator，yield的作用：保存当前状态，并返回
        a, b = b, a + b #将b赋给a，将a+b赋给b
        #注意赋值：相当于 t = (b, a+b) t是一个tuple
                        # a = t[0]
                        # b = y[1]
        n += 1
    return '-----done------'  #作用是产生异常时打印的消息
'''
print(fib(20)) #打印了一个地址
f = fib(20)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("---------start loop-----------")
for i in f: #使用循环不会返回'-----done------'
    print(i)
'''
#不是用循环，并且抛出异常处理
f = fib(6)
#只打印6个斐波拉契数列，但是程序超出了这个值，就会抛出异常
while True:
    try:
        x = next(f)
        print("g:",x)
    except StopIteration as e:
        print("generator return value:",e.value)
        break
# print(f.__next__())
# print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())
# # print(f.__next__())