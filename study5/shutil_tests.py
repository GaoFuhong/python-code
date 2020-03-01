# Author:Fuhong Gao
import shutil
'''
f1 = open("README",encoding="utf-8") #打开一个已经存在的文件
f2 = open("new_file","w",encoding="utf-8") #创建一个新文件，用于存储复制的文件内容
shutil.copyfileobj(f1,f2) #复制
'''

# shutil.copyfile("new_file","new_file2")
# shutil.copytree("a","new_a")  #递归的复制文件
# shutil.rmtree("new_a") #递归的删除文件
# shutil.make_archive("make_archive_test","zip","D:\PycharmProjects\study1") #打包文件

import zipfile
z = zipfile.ZipFile("任意打包多个文件","w")
z.write("README")
print("---------")
z.write("p_test.py")
z.close()

