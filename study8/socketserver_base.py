# Author:Fuhong Gao
#网络服务器_基础版
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler): #创建一个请求处理器类
    def handle(self):
        while True:
            print("等待接收。。")
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote".format(self.client_address))
                print(self.data)
            except ConnectionResetError as e:
                print("error:",e)
                break
            self.request.send(self.data.upper())
if __name__ == "__main__":
    HOST, POST = "localhost",9999 #创建一个服务，绑定到本地，端口号是9999
    # 实例化ThreadingTCPServer,并将(HOST,POST)和MyTCPHandler当做参数传给ThreadingTCPServer
    server = socketserver.ThreadingTCPServer((HOST,POST),MyTCPHandler)  #注意：ThreadingTCPServer支持并发，客户端来一个请求，服务器处理一个请求。
    server.serve_forever() #处理多个请求，并一直执行着
