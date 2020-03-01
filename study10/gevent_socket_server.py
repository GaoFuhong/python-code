# Author:Fuhong Gao
#通过gevent实现单线程下的多socket并发
import socket,gevent
from gevent import monkey
monkey.patch_all()
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen()
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request,cli)
def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print('Received:',data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        conn.close()
if __name__ == '__main__':
    server(8001)