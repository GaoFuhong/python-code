# Author:Fuhong Gao
import time #导入时间模块
def logger():  #创建一个日志文件，可以往里面不断添加内容
    time_format = '%Y-%m-%d %X' #年-月-日 时-分-秒的表示方式
    time_current = time.strftime(time_format) #记录当前的时间
    with open('log.txt','a+',encoding='utf-8') as f:
        f.write('%s 日志内容\n' %time_current)

def test1():
    print("in the test1...")
    logger()
def test2():
    print('in the test2...')
    logger()
def test3():
    print('in the test3...')
    logger()

#使用函数的好处：1.减少代码的复用；2.可扩展；3.保持一致性。