# Author:Fuhong Gao
#多进程，实现父进程与子进程之间数据的传递
from multiprocessing import Process,Queue
# import queue
def f(qq):
    qq.put([22,None,'abc'])
if __name__ == '__main__':
    q = Queue() #进程的queue
    p = Process(target=f,args=(q,)) #将父进程的q作为参数传给子进程
    p.start()
    print(q.get())