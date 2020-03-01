# Author:Fuhong Gao
import module_gfh #导入定义的模块
#import module1,module2,module3 导入多个模块
# from module_gfh import * #相当于把module_gfh中的代码复制过来
# from module_gfh import m1,m2,m3
from module_gfh import logger as module_gfh_logger #将module_gfh中的logger()函数导入过来并改名为main_logger
print(module_gfh.name)
module_gfh.sayhi()

def logger():
    print("in the main_logger")
logger() #调用的是mian中的logger函数

module_gfh_logger() #调用的是module_gfh中的logger
import sys,os
print('当前文件的绝对路径：',os.path.abspath(__file__))
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #这时的目录是...\study5
print(x)
sys.path.append(x) #sys.path（路径搜索）是一个列表，在列表的最后追加路径
# sys.path.insert(0,x) ：插入路径（插在最前面）

import module_2 #module_2在study5的目录下

