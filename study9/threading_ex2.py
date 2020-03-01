# Author:Fuhong Gao
#通过继承类的方式启动线程
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time
    def run(self):
        print("task",self.n)
        time.sleep(self.sleep_time)
        print("task %s done" %self.n)
t1 = MyThread("t1",2)
t2 = MyThread("t2",4)
t1.start()
# t1.join() #等待第一个线程执行完毕才执行第二个，将线程变成串行的
t2.start()
t1.join()
print("main thread...")