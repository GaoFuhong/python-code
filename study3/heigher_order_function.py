# Author:Fuhong Gao
def add(a,b,f):
    return f(a) + f(b)
res = add(2,-6,abs)#abs就是一个内置函数，再传给add(a,b,f)函数
print(res)
