# Author:Fuhong Gao
#greenlet 已经封装好了的协程
from greenlet import greenlet
def t1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def t2():
    print(56)
    gr1.switch()
    print(78)
gr1 = greenlet(t1) #启动一个协程
gr2 = greenlet(t2)
gr1.switch()
