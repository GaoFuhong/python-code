# Author:Fuhong Gao
#以下是未经导入优化的代码，因为每次都会去搜索module_t1，耗费时间
'''
import module_t1

def logger():
    module_t1.use_many_times()
    print("in the logger...")

def runner():
    module_t1.use_many_times()
    print("in the runner...")

logger()
runner()
'''
#假设后面还有很多函数，都会用到module_t1中的use_many_times()函数
#..........................
#以下是经导入优化的代码
from module_t1 import use_many_times

def logger():
    use_many_times()
    print("in the logger...")

def runner():
    use_many_times()
    print("in the runner...")

logger()
runner()


