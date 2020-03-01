# Author:Fuhong Gao
#服务器端
import socket
server = socket.socket()
server.bind(('localhost',9999)) #绑定要监听的端口
server.listen(5) #监听（最多允许5个连接）
print("正在等待连接信息。。。")
while True:
    conn, addr = server.accept() #等待接收连接信息
    print("已经连接成功！")
    print(conn, addr)
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        if not data:
            print("客户端已经断开！")
            break
        conn.send(data.upper()) #返回内容，大写
server.close()
