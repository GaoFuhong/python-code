# Author:Fuhong Gao
#信号量：同时允许一定数量的线程更改数据
import threading, time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()
if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
while threading.active_count() != 1:
    pass
else:
    print("all thread done!!!")