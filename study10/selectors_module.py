# Author:Fuhong Gao
import selectors,socket
sel = selectors.DefaultSelector()
def accept(sock,mask):
    conn,addr = sock.accept()
    print('accept:',conn,'from:',addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)
def read(conn,mask):
    data = conn.recv(1024)
    if data:
        print('echoing',repr(data),'to',conn)
        conn.send(data)
    else:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()
sock = socket.socket()
sock.bind(('localhost',8001))
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)
while True:
    events = sel.select() #默认是阻塞的，有活动连接就返回活动的连接列表
    for key,mask in events:
        callback = key.data #=accept
        callback(key.fileobj,mask)
