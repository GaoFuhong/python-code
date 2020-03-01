# Author:Fuhong Gao
#定义函数
def func1():
    """文档描述"""
    print('函数的代码块')
    return 0  #返回值
#定义过程
def func2():
    """testing2"""
    print('过程的代码块')
x = func1() #调用函数
y = func2() #调用过程
#注意：过程其实就是没有返回值的函数
print('from func1 return is %s'%x)
print('from func2 return is %s'%y)