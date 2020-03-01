# Author:Fuhong Gao
import time
t = time.localtime() #本地当前的时间
print("当前是%d年."%t.tm_year) #取出年份
print("当前本地时间元组的格式化输出：",time.strftime("%Y-%m-%d %H:%M:%S",t))
print("将格式化字符串转换成时间元组：",time.strptime("2018-08-08 16:32:40","%Y-%m-%d %H:%M:%S"))#一一对应，顺序可以交换
import datetime
print(datetime.datetime.now()) #获取当前的时间
print(datetime.datetime.now()+datetime.timedelta(3)) #3天后的时间
print(datetime.datetime.now()+datetime.timedelta(-10)) #10天前的时间
print(datetime.datetime.now()+datetime.timedelta(hours=4)) #4小时之后的时间
print(datetime.datetime.now()+datetime.timedelta(minutes=-30)) #30分钟以前的时间

c_time = datetime.datetime.now()
print(c_time.replace(minute=4,second=44)) #时间替换
