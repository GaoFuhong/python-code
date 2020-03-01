# Author:Fuhong Gao
import shelve #不像pickle模块那样只能dump一次，load一次
'''
import datetime
d = shelve.open("shelve_file") #打开一个文件
info = {"name":"gfh","age":22,"sex":"male"}
list1 = ["happy","hello","hi"]
d["info"] = info #持久化字典
d["list1"] = list1 #持久化列表
d["time"] = datetime.datetime.now()
d.close()
'''
d = shelve.open("shelve_file")
#读取数据
print(d.get("info"))
print(d.get("list1"))
print(d.get("time"))