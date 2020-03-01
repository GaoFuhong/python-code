# Author:Fuhong Gao
#传送文件_客户端
import socket,hashlib
client = socket.socket()
client.connect(("localhost",9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response:",server_response)
        client.send(b"ready to receive file...")
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new","wb")
        m = hashlib.md5() #每接收一行内容，进行一次md5加密
        #避免粘包的发生：
        while received_size < file_total_size:
            if file_total_size - received_size > 1024: #要接收不止一次
                size =1024
            else: #接收最后一次，剩多少接收多少
                size = file_total_size - received_size
            data = client.recv(size)
            received_size += len(data)
            m.update(data) #对接收的文件md5加密
            f.write(data)
            # print(file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()
            print("file send done.",file_total_size,received_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print("server file md5:",server_file_md5)
        print("new file md5:",new_file_md5)
client.close()