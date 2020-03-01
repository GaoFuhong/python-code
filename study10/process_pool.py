# Author:Fuhong Gao
#进程池 （在windows中启动进程是真的慢。。。）
from multiprocessing import Process,Pool
import time,os
def Foo(i):
    time.sleep(1)
    print('in process-',os.getpid())
    return i+100
def Bar(arg):
    print("--> exec done:",arg,'child process id:',os.getpid())
if __name__ == '__main__': #__name__ == 'main' 如果手动执行这个脚本，就执行下面的内容，如果当做一个模块导入，就不执行
    pool = Pool(5) #等价于pool = Pool(processes = 5) 允许进程池里同时放入5个进程
    print('main process id:',os.getpid())
    for j in range(10):
        pool.apply_async(func=Foo,args=(j,),callback=Bar) #callback: 回调 主进程执行的回调
        # pool.apply(func=Foo,args=(j,)) #串行
        # pool.apply_async(func=Foo,args=(j,)) #并行
    print('-----------------------')
    pool.close()
    pool.join() #进程池中进程执行完毕再关闭，如果注释，程序将直接关闭