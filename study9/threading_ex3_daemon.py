# Author:Fuhong Gao
import threading
import time
def run(n):
    print("task",n)
    time.sleep(2)
    print("task done.",n,threading.current_thread())
start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()
    t_objs.append(t)
print("-----all the threads have finished-----",threading.current_thread(),threading.active_count())
print("cost time:",time.time() - start_time)