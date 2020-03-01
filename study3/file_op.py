# Author:Fuhong Gao
#data = open("yesterday",encoding='utf-8').read()
#Windows操作系统的编码方式是gbk，而python3是utf-8，打不开。所以要加一个encoding='utf-8'
#print(data)
#读全部文件：
'''
f = open("yesterday",'r',encoding="utf-8") #文件句柄,'r'代表读模式，默认是'r'
data = f.read() #读第一次
data2 = f.read() #读第二次（注意;第二次读是在第一次读完的文件之后继续读，所以data2没有内容）
print(data)
print('----------------data2------------%s------'%data2) #data2没有内容
f.close() #文件关闭

f = open("yesterday",'r',encoding="utf-8")
for i in range(10):
    if i <5:
        f.readline()
    else:
        print(f.readline()) #打印5-10行
'''

#low loop:
'''
f = open("yesterday",'r',encoding="utf-8")
for index,line in enumerate(f.readlines()): #f.readlines()是把文件内容的每一行作为列表中的一个元素，因为要将文件先存储到内存中，所以一般只适合读小文件
    #第10行不打印
    if index == 9:
        print("-----我是分割线--------------")
        continue
    print(line.strip())  #strip表示去掉空格换行
'''
#高效率的循环
'''
count = 0
f = open("yesterday",'r',encoding="utf-8")
for line in f:
    if count == 9:
        print("---------我是分割线--------------")
        count += 1
        continue
    print(line.strip())
    count += 1
'''

#已经执行：
'''
f2 = open('love','w',encoding="utf-8") #写模式,建立一个新的文件
f2.write("I love Xiao Gu! \n")
f2.write('Come on! ') #往里面写内容

f2 = open('love','a',encoding="utf-8") #'a'是追加模式，在文件最后写内容，但是不覆盖
f2.write("\nDo you love me?") #注意：追加模式不能读,run一次，添加一次
f2.close()
'''

#文件的一些方法：
'''
f = open('yesterday','r',encoding='utf-8')
print(f.tell())   #打印文件中光标的位置，刚开始光标的位置为0
f.readline()  #读一行
print(f.tell())   #读一行之后光标的位置
for i in range(2):
    print(f.readline()) #再读2行
print(f.tell())
f.seek(0)  #让光标回到文件起始位置
print(f.encoding) #打印文件的编码
print(f.fileno()) #文件的编号
print(f.seekable()) #判断文件是否可以移动光标
print(f.readable()) #判断文件是否可读
print(f.writable()) #判断文件是否可写
f.flush() #实时刷新，比如在写文件的时候，内容是没有立刻存到硬盘上的，而是先到缓存区，如果利用flush（），则直接存到硬盘上
f.closed #判断文件是否关闭
'''
'''
f = open('yesterday2','a',encoding='utf-8')
f.truncate(20) #从头开始截，截20个字符
'''
'''
f = open('yesterday','r+',encoding='utf-8') #'r+'表示既可以读又可以追加
print(f.readline())
print(f.readline())
print(f.readline())#读3行
f.write('\n我爱古晓！ ')
f.flush()
data = f.read()
print(data)
'''
'''
f = open('yesterday','w+',encoding='utf-8') #写读，先往文件中写东西，会覆盖原来文件中的内容
f.write('I love Xiao Gu 1314! \n')
f.write('I love Xiao Gu 1314! \n')
f.write('I love Xiao Gu 1314! \n')
f.seek(10)
f.tell()
print(f.readline()) #可以读内容
f.write('补充的内容会在文件最后追加。。。') #虽然光标在第10的位置，但写的内容会在最后追加
f.close()
'''
# f = open('yesterday','a+',encoding = 'utf-8') #追加读写


#二进制文件的读
f = open('yesterday','rb') #注意不要编码：encoding  使用情况：（1）网络传输；（2）读视频类文件
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#二进制文件的写
f = open('yesterday','wb')
f.write('Hello world! '.encode())
f.close()