# Author:Fuhong Gao
# with语句可以在文件操作结束后自动关闭
import sys
with open("yesterday","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

#同时打开多个文件：
with open('yesterday','r',encoding='utf-8') as f,\
        open('yesterday','r',encoding='utf-8') as f2: #Python的开发规范，每行一般不超过80个字符
    for line in f:
        print(line.strip())