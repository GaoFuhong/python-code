# Author:Fuhong Gao
#基于用户名、密码连接
import paramiko #未安装paramiko模块
ssh = paramiko.SSHClient() #创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #允许连接不在know_hosts文件中的主机
ssh.connect(hostname = 'c1.salt.com', port = 22, username = 'gaofuhong', password = '123456') #连接服务器
stdin, stdout, stderr = ssh.exec_command('df') #执行命令
result = stdout.read() #获取命令结果
ssh.close() #关闭连接

