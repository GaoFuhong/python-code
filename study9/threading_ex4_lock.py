# Author:Fuhong Gao
import threading
import time
def run(n):
    lock.acquire() #获取一把锁，加锁之后变成串行
    global num
    num += 1
    time.sleep(0.5)
    lock.release() #释放锁
lock = threading.Lock() #锁的实例
num = 1
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()
print("-----all the threads have finished-----",threading.current_thread(),threading.active_count())
print("end_num:",num)