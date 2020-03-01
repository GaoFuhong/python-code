# Author:Fuhong Gao
#客户端
import socket
client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))
while True:
    msg = input("输入内容：>>").strip()
    client.send(msg.encode("utf-8")) #可以传中文
    data = client.recv(1024) #可以接收1024个字节
    print("Receive:",data.decode())
client.close()