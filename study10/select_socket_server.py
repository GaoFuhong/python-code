# Author:Fuhong Gao
#多并发
import select
import socket
import queue
server = socket.socket()
server.bind(('localhost',8001))
server.listen(5)
server.setblocking(False) #不阻塞
msg_queue = {}
inputs = [server,]
outputs = []
while True:
    print('waiting for next event...')
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)
    for r in readable:
        if r is server:
            conn, addr = server.accept()
            print('new connect from ', addr)
            inputs.append(conn)
            msg_queue[conn] = queue.Queue() #初始化一个队列，用以存返回给这个客户端的数据
        else:
            data = r.recv(1024)
            if data:
                print('received data from [%s]:'%r.getpeername()[0],data)
                msg_queue[r].put(data)
                outputs.append(r)
                # r.send(data)
                # print('send done...')
            else:
                print('The client was disconnected.')
                #清理已断开的连接
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                del msg_queue[r]
    for w in writeable: #要返回给客户端的连接列表
        try:
            next_msg = msg_queue[w].get_nowait()
        except queue.Empty:
            print('Client [%s] '%w.getpeername()[0],'queue is empty...')
            outputs.remove(w)
        else:
            print('Send message to [%s] '%w.getpeername()[0],next_msg)
            w.send(next_msg.upper())
    for e in exceptional: #出现连接断开的情况
        print('handling exception for ',e.getpeername())
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
        del msg_queue[e]
