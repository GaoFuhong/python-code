# Author:Fuhong Gao
#传送命令_客户端
import socket
client = socket.socket()
client.connect(("localhost",9999))
while True:
    cmd = input("请输入指令>>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) #接收命令结果的长度
    print("命令结果大小：",cmd_res_size)
    client.send("准备好接收了。。。".encode("utf-8"))
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) #每次收到的可能有小于1024的信息，所以必须用len判断
        received_data += data
    else:
        print("cmd_res receive done...",received_size)
        print(received_data.decode())
client.close()