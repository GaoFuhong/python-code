# Author:Fuhong Gao
def test1():
    print("屏幕输出内容1。。。")#没有返回值，但解释器会隐式的返回一个None

def test2():
    print('屏幕输出内容。。。')
    return 0 #返回0

def test3():
    print("屏幕输出内容。。。")
    return 1,"hello",['Xiao Gu','Fuhong Gao'],{'name':'Xiao Gu'}
x = test1() #执行函数的内容，并把返回值传给x
y = test2()
z = test3() #python将返回的多个内容组合成一个元组
print(x)
print(y)
print(z)
