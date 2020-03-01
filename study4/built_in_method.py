# Author:Fuhong Gao
#abs(x):返回数字的绝对值
#all(iterable):如果所有的元素迭代都是真的，则返回True（或者可迭代为空）
print(all([0,1,-5])) #False
#any(iterable):如果任意一个元素迭代为真，则返回True;如果iterable的元素为空，则返回False
print(any([0,1,-5])) #True
#ascii(object):把内存的数据对象改成字符串的形式
a = ascii([1,-3,'I love Xiao Gu! '])
print(type(a),[a]) #<class 'str'> ["[1, -3, 'I love Xiao Gu! ']"]
#bin(x):把一个整数转化成二进制
print(bin(5)) #0b101
#bool([x]):判断列表、字典等的真假
print(bool({})) #False
b = bytes('abcde',encoding='utf-8')
print(b.capitalize(),b) #字节是不可以修改的（字符串也不能修改）
c = bytearray('abcde',encoding='utf-8') #将字符串改成列表，根据ascii码修改
print(c[0]) #打印‘a’的ascii码
c[1] = 50
print(c)
#callable(object):判断object参数是否可调用,列表、字典等不可调用，函数、类等可调用
print(callable([])) #False
def sayhi():
    pass
print(callable(sayhi)) #True
#chr(i):根据ascii码转换成对应的字符
print(chr(97))
#ord(c):给定一个ascii码的字符，返回对应的数字
print(ord('c'))
#compile(),将源代码（字符串）编译成可执行代码
code = "for i in range(10):print(i)"
loop = compile(code, '','exec')
print(loop)
exec(loop) #执行
#不知道为什么，下面注释的代码不能执行
# code2 = "1+3"
# calc = compile(code2,'','eval')
# calc
# eval(calc)#执行
#dir（[object]）:返回对象的可用方法
list1 = []
print(dir(list1))
#divmod(a,b):返回两个数相除的商和余数
print(divmod(5,2))
#匿名函数
(lambda n:print(n))(20)
#filter(function, iterable):功能如根据条件过滤掉默写元素
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)
res2 = map(lambda x:x*2,range(10))
for i in res2:
    print(i) #类似于列表生成式print([i*2 for i in range(10)])
import functools #必须导入
res3 = functools.reduce(lambda x,y:x+y,range(10)) #实现0-9的累加
print(res3)
#frozenset([iterable]):冻结列表，不可变
froz_list = frozenset([1,2,33,2,524,0,0.5])#将列表变成一个集合，并且没有增、删、改等功能
print(globals())#返回当前程序中所有的变量及对应的值，以字典形式表示
print(hash(123)) #将数字、字符串映射成数字一一对应
print(hash('gfh'))
print(hex(10))#将一个整数转换成十六进制
#id(object):返回对象的内存地址
print(id("gfh"))
#isinstance()：判断某一个变量是否是某种类型
def test():
    local_var = 333
    print(locals())#以字典形式打印局部变量
test()
print(max([0,5,-1])) #返回一个列表中的最大值
print(min([0,5,-1])) #返回一个列表中的最小值
print(oct(16))#将一个整数转换成八进制
print(pow(2,8))#求某个数的多少次方
#repr(object):将某个对象用字符串表示
print(round(1.2554,2))#对某个小数进行四舍五入
#slice(stop):切片
#sorted():从iterable中返回一个可排序列表
dict1 = {1:22,0:1,-5:88,2:5,58:-8,99:41}
print(dict1) #打印字典
print(sorted(dict1.items())) #按照字典的key排序并打印
print(sorted(dict1.items(),key = lambda x:x[1])) #按照字典的value排序并打印
print(sum([0,5,-1,3])) #对一个列表求和
list_a = [1,2,3,4,5,6]
list_b = ['a','b','c','d']
ab = zip(list_a,list_b) #将两个列表一一对应起来，并且按照数量较少的那个列表对应
for i in ab :
    print(i)
__import__('decorator1') #导入某个文件名，并执行

