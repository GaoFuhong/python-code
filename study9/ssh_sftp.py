# Author:Fuhong Gao
#基于用户名、密码上传下载
import paramiko
transport = paramiko.Transport("hostname",22)
transport.connect(username = "gapfuhong", password = "123456")
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('/tmp/location.py','/tmp/test.py') #将location.py上传至服务器/tmp/test.py
sftp.get('remove_path','local_path') #将remove_path下载至本地local_path
transport.close()