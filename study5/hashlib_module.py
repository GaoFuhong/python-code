# Author:Fuhong Gao
import hashlib
import hmac  #它对创建的key和内容再进行处理和再加密
#md5
m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest()) #以十六进制加密
m.update("it's me是我".encode(encoding="utf-8")) #如果有中文，必须加.encode(encoding="utf-8")
print(m.hexdigest()) #这时候的加密包括Hello 和 it's me
#验证：
m2 = hashlib.md5()
m2.update(b"Helloit's me")
print(m2.hexdigest())

#sha1
s = hashlib.sha1()
s.update(b"Helloit's me")
print(s.hexdigest())

#hmac
h = hmac.new(b"123","我love古晓！".encode(encoding="utf-8"))
print(h.digest()) #以十进制加密
print(h.hexdigest()) #以十六进制加密


