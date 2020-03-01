# Author:Fuhong Gao
#多进程
import threading,multiprocessing,time
def thread_run():
    print("当前线程id:",threading.get_ident()) #打印当前线程的id号
def run(name):
    time.sleep(1)
    print('Helle,',name)
    t = threading.Thread(target=thread_run,) #在一个进程里面运行一个线程
    t.start()
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('Gay-%s'%i,))
        p.start()
    # p.join()