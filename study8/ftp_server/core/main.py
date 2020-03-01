# Author:Fuhong Gao
import socketserver,json,os
class MyTCPHandler(socketserver.BaseRequestHandler): #创建一个请求处理器类
    def put(self,*args):
        '''接收客户端发来的文件'''
        cmd_dict = args[0]
        filename = cmd_dict["filename"]
        filesize = cmd_dict["size"]
        if os.path.isfile(filename): #如果同名文件已经存在，创建一个新的
            f = open(filename + ".new","wb")
        else: #文件不存在，直接接收
            f = open(filename,"wb")
        self.request.send(b"OK") #给客户端返回确认信息
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024) #接收文件
            f.write(data) #保存文件
            received_size += len(data)
        else: #文件接收完毕
            print("Flie [%s] has uploaded! " %filename)
    def handle(self):
        while True:
            print("等待接收。。")
            #异常
            try:
                self.data = self.request.recv(1024).strip() #接收客户端发来的文件名和文件大小
                print("{} wrote".format(self.client_address[0]))
                print(self.data)
                cmd_dict = json.loads(self.data.decode())
                action = cmd_dict["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dict)

            except ConnectionResetError as e:
                print("error:",e)
                break
if __name__ == "__main__":
    HOST, POST = "localhost",9999 #创建一个服务，绑定到本地，端口号是9999
    # 实例化ThreadingTCPServer,并将(HOST,POST)和MyTCPHandler当做参数传给ThreadingTCPServer
    server = socketserver.ThreadingTCPServer((HOST,POST),MyTCPHandler)  #注意：ThreadingTCPServer支持并发，客户端来一个请求，服务器处理一个请求。
    server.serve_forever() #处理多个请求，并一直执行着