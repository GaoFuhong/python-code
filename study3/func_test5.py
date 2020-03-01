# Author:Fuhong Gao
def test(x,y): #x，y是形参
    print(x)
    print(y)

test(1,2) #1,2是实参（位置参数调用） 或者：test(y = 1, x = 2)也行（关键字调用）
#注意：test(1,y = 2)也行，位置参数只能写在关键字参数前面

#默认参数
def test2(x,y = 'a'):
    print(x)
    print(y)
test2('2333') #不用给y赋值，它是默认参数，当然也可以重新赋值，如：test2('2333',y = 2)

#参数组
def test3(*args): #参数组用*号加一个变量名，将多个实参转换成一个元组
    print(args)
test3('gfh',1,3,1,4,'gx') #实参的个数不固定
test3(*['gfh',1,3,1,4,'gx']) #用*号加一个列表的效果等价 args = turple(['gfh',1,3,1,4,'gx'])

#位置参数和参数组结合使用
def test4(x,*args):
    print(x)
    print(args)
test4(1,2,3,4,5,6)

#将关键字参数转换成字典的方式存放
def test5(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
test5(name = 'gfh', age = 22, sex = 'male', height = '171cm')
#test5(**{'name':'gfh', 'age':22, 'sex':'male', 'height':'171cm'}) #**加一个字典等价

#字典和位置参数结合
def test6(name,**kwargs):
    print(name)
    print(kwargs)
test6('gfh', age = 22, sex = 'male')
#字典和默认参数结合
def test7(name, age = 22, **kwargs): #注意**kwargs只能放在最后
    print(name)
    print(age)
    print(kwargs)
test7('gfh',sex = 'male',height = 171)

#所有类型的参数一起用
def test8(name, age = 22, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test8") #函数里面还可以嵌套一个函数
def logger(source):
    print("from %s" %source)

test8('gfh',sex = 'male',height = 171) #此时参数组*args没有接受参数