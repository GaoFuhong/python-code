# Author:Fuhong Gao
#管道 实现进程之间数据的传递
from multiprocessing import Process,Pipe
def f(conn):
    conn.send([22,None,'abc from child']) #child_conn发送数据
    conn.send([22,None,'abc from child2'])
    print('from parent:',conn.recv()) #child_conn接收数据
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe() #生成管道实例
    p = Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv()) #parent_conn接收数据
    print(parent_conn.recv())
    parent_conn.send("How are you?") #parent_conn发送数据
    p.join()