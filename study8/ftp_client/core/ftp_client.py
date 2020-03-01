# Author:Fuhong Gao
import socket,os,json
class FtpClient(object):
    def __init__(self): #构造函数
        self.client = socket.socket() #实例化
    def help(self): #帮助信息
        msg = '''
        ls
        pwd
        cd ../..
        put filename
        get filename
        ''' #第一个参数都是指令
        print(msg)
    def connect(self,ip,port): #连接
        self.client.connect((ip, port))
    def interactive(self): #交互
        #self.authenticate() 登录验证的方法
        while True:
            cmd = input("输入指令>>:").strip()
            if len(cmd) == 0:
                continue
            cmd_str = cmd.split()[0] #cmd_str就是指令
            #反射：
            if hasattr(self,"cmd_%s" %cmd_str):
                func = getattr(self,"cmd_%s" %cmd_str)
                func(cmd)
            else:
                self.help()
    def cmd_put(self,*args): #上传文件
        cmd_split = args[0].split() #将输入的内容按空格分开，组成一个列表
        if len(cmd_split) > 1: #有效指令
            filename = cmd_split[1] #获取文件名
            if os.path.isfile(filename): #判断是否是一个文件
                filesize = os.stat(filename).st_size #获取文件大小
                #json字典
                msg_dict = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize,
                    "overridden":True
                }
                self.client.send(json.dumps(msg_dict).encode("utf-8")) #将文件名和文件大小一次性发给服务器
                print("send:",json.dumps(msg_dict).encode("utf-8"))
                server_response = self.client.recv(1024) #防止粘包，等待服务器的确认信息
                f = open(filename,"rb") #打开文件
                for line in f: #传送文件
                    self.client.send(line)
                else: #文件传送完毕
                    print("File [%s] upload succeed!" %filename)
                    f.close()
            else:
                print(filename,"is not exist.")
    def cmd_get(self):
        pass
#实例化
ftp = FtpClient()
ftp.connect("localhost",9999)
ftp.interactive()