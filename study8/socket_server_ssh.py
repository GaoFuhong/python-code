# Author:Fuhong Gao
#传送文件_服务器端
import socket,os
server = socket.socket()
server.bind(("localhost",9999))
server.listen()
while True:
    print("等待接收。。。")
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开！")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            print("cmd has no output...")
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #先将要发送的命令的大小发送给客户端
        client_ack = conn.recv(1024) #再接收一次，避免产生粘包
        conn.send(cmd_res.encode("utf-8"))
        #以上连续发送两次，可能发生粘包
        print("send done!")
server.close()