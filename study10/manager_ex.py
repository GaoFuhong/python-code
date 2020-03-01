# Author:Fuhong Gao
#实现进程之间数据的共享
from multiprocessing import Process,Manager
import os
def f(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.3] = None
    l.append(os.getpid())
    print(l)
if __name__ == '__main__':
    with Manager() as manager: #相当于manager = Manager()
        d = manager.dict() #生成一个字典，可以在多个进程间共享和传递
        l = manager.list(range(5)) #生成一个列表
        p_list = []
        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)