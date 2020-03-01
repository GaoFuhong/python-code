# Author:Fuhong Gao
#生产者消费者模型
import queue,threading,time
q = queue.Queue(maxsize=10) #设一个队列实例，队列长度最大为10
def Producer(name):
    count = 1
    while True:
        q.put("bone-%s" %count)
        print("produced bone ",count)
        count += 1
        time.sleep(0.1)
def Consumer(name):
    # while q.qsize() > 0:
    while True:
        print("[%s] got [%s] and ate it." %(name, q.get()))
        time.sleep(1)
p = threading.Thread(target=Producer,args=("San Zhang",))
c1 = threading.Thread(target=Consumer,args=("XiaoHuang",))
c2 = threading.Thread(target=Consumer,args=("XiaoBai",))

p.start()
c1.start()
c2.start()