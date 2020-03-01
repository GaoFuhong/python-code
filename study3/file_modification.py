# Author:Fuhong Gao
#修改文件
f = open('yesterday','r',encoding='utf-8') #读原文件
f_new = open('yesterday.new','w',encoding='utf-8') #创建一个新的文件，可以写
for line in f:
    if '肆意的快乐等我享受' in line:
        line = line.replace('肆意的快乐等我享受','肆意的快乐等GFH享受')
    f_new.write(line) #修改内容，边读边写
f.close()
f_new.close()