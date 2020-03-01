# Author:Fuhong Gao
#使用Gevent实现自动io切换
import gevent
def Foo():
    print('Run in Foo...') #第1步
    gevent.sleep(2)
    print('Explicit context switch to Foo again!') #第6步
def bar():
    print('Explicit context to bar!') #第2步
    gevent.sleep(1)
    print('Implicit context switch back to bar!') #第5步
def func3():
    print('run func3...') #第3步
    gevent.sleep(0)
    print('run func3 again...') #第4步
gevent.joinall([
    gevent.spawn(Foo),
    gevent.spawn(bar),
    gevent.spawn(func3)
])