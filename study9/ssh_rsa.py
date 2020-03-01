# Author:Fuhong Gao
#基于公钥密钥连接
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
ssh = paramiko.SSHClient() #创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在konw_hosts文件中的主机
ssh.connect(hostname = 'c1.salt.com', port = 22, username ='gaofuhong', key = private_key) #连接服务器
stdin, stdout,stderr = ssh.exec_command('df') #执行命令
result = stdout.read() #获取在命令正确时的结果
ssh.close() #关闭连接

