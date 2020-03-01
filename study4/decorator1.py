# Author:Fuhong Gao
import time
def timer(func):
    def wrapper(*wargs,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("in the func run time is %s" %(stop_time - start_time))
    return wrapper
@timer
def test1():
    time.sleep(2)
    print("content printed after 2 seconds...")

test1()