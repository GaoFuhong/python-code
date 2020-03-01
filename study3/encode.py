# Author:Fuhong Gao
import sys
print(sys.getdefaultencoding())
s = "你好！世界！" #python3.x的默认编码是Unicode，注意区分Python2.x
print(s,type(s))
s_gbk = s.encode("gbk")  #转换成gbk
print(s_gbk,type(s_gbk))
s_utf8 = s.encode("utf")  #转换成utf-8
print(s_utf8)

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf8")  #gbk转换成utf-8,和Python一样，中间需要转换成Unicode
print("utf-8",gbk_to_utf8)


