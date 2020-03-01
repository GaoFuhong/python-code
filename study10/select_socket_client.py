# Author:Fuhong Gao
import socket
messages = [
    b'This is a message.',
    b'It will be sent.',
    b'In parts.'
]
server_addr = ('localhost',8001)
socks = [
    socket.socket(socket.AF_INET,socket.SOCK_STREAM) for i in range(1000)]
print('connecting to %s port %s' %server_addr)
for s in socks:
    s.connect(server_addr)
for m in messages:
    for s in socks:
        print('%s:send message %s'%(s.getsockname(),m))
        s.send(m)
    for s in socks:
        data = s.recv(1024)
        print('%s: received %s'%(s.getsockname(),data))
        if not data:
            print('closing socket',s.getsockname())