# Author:Fuhong Gao
import os
print(os.getcwd()) #获取当前工作目录
os.chdir(r"D:\PycharmProjects") #改变当前脚本工作目录，注意加个r    或这种形式：os.chdir("D:\\PycharmProjects")
print(os.getcwd())
os.chdir(r"D:\PycharmProjects\study5") #改回来
# os.curdir 返回当前目录
# os.pardir 返回当前目录的父目录
os.makedirs(r"D:\PycharmProjects\study5\new_file_1\new_file_2") #生成多层递归目录
os.removedirs(r"D:\PycharmProjects\study5\new_file_1\new_file_2") #若目录为空，则删除，并递归到上一层目录；若也为空。则删除，以此类推。一般用于清楚空目录
# mkdir('dirname') 生成单级目录
# rmdir('dirname') 删除单级空目录
print(os.listdir(r"D:\PycharmProjects")) #列出指定目录下的所有文件和子目录
# os.remove() 删除一个文件
#os.rename('oldname','newname') 重命名文件/目录  注意路径
print(os.stat(r"D:\PycharmProjects\study5\README")) #获取文件/目录信息
print(os.sep) #输出操作系统特定的路径分隔符
print(os.linesep) #输出当前平台的行终止符
print(os.pathsep) #输出用于分隔文件路径的字符串
print(os.environ) #获取系统的环境变量
print(os.name) #输出字符串指示当前使用平台  win--> nt
os.system("dir") #运行shell变量
#注意：使用os.system("bash command")时，若File->Settings->Editor->File Encodings->Global Encoding:utf-8，这时会乱码,需要改成GBK
print(os.popen("ipconfig/all").read()) #这种方法和os.system()类似，且不管是utf-8还是GBK都不会乱码
print(os.path.abspath(__file__))  #获取path规范化的绝对路径
print(os.path.split(r"C:\q\p\c\c.txt")) #将path分割成目录和文件名二元组
print(os.path.dirname(r"C:\q\p\c\c.txt")) #返回path的目录，即os.path.split()的第一个元素
print(os.path.basename(r"C:\q\p\c\c.txt")) #返回文件名，即os.path.split()的第二个元素
#以上三个都不考虑path是否存在
print(os.path.exists(r"C:\q\p\c")) #判断path是否存在
print(os.path.isabs(r"C:\a")) #判断path是否是一个绝对路径（绝对路径一定要有根目录）
print(os.path.isfile(r"C:\log.txt")) #判断path是否是一个文件
print(os.path.isdir(r"C:\Windows")) #判断path是否是一个目录
print(os.path.join(r"C:\c",r"a.txt")) #将多个路径组合
print(os.path.getmtime(r"C:\log.txt")) #获取文件或者目录的最后存取时间（返回一个时间戳）
print(os.path.getatime(r"C:\log.txt")) #获取文件或者目录的最后修改时间（返回一个时间戳）






