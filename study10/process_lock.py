# Author:Fuhong Gao
#进程同步
from multiprocessing import Process,Lock
def f(l,i):
    # l.acquire()
    print('Hello,world-',i)
    # l.release()
if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        p = Process(target=f,args=(lock,num))
        p.start()
