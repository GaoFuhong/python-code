# Author:Fuhong Gao
#多线程 并发（通过函数的方式启动线程）
import threading
import time
def run(n):
    print("task",n)
    time.sleep(2)
'''
t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))
t1.start()
t2.start()
'''
# run("t1")
# run("t2")

#采用循环的方式启动多个线程（计算线程并发的时间）
t_objs = [] #定义一个空列表，用于存线程实例
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join,先将每个线程实例传到列表中
for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
    t.join()
print("-----all the threads have finished-----")
print("cost time:",time.time() - start_time) #计算的时间只是主线程的运行时间，不包括停顿的2秒