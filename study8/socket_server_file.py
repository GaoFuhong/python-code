# Author:Fuhong Gao
#传送文件_服务器端
import socket,os,hashlib
server = socket.socket()
server.bind(("localhost",9999))
server.listen()
while True:
    print("等待接收。。。")
    conn, addr = server.accept()
    print("new conn:",addr)
    while True:
        print("准备接收指令。。。")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开！")
            break
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,"rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode()) #发送文件的大小
            conn.recv(1024)
            for line in f:
                m.update(line) #读一行，md5加密一行
                conn.send(line) #一行一行的发送文件
            print("file md5:",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode()) #send md5 #连续send两次，可能产生粘包
        print("Send done!")
server.close()