# Author:Fuhong Gao
#生成器并发
import time
def customer(name1):
    print("\033[31;1m%s\033[0m准备吃棒棒糖了！" %name1)
    while True:
        lollipop = yield
        print("\033[32;1m%s味\033[0m的棒棒糖来了，被\033[31;1m%s\033[0m吃了..." %(lollipop,name1))
def producer(name2):
    c1 = customer("古晓")
    c2 = customer("Xiao Gu")
    c1.__next__()
    c2.__next__()
    print("老高开始做棒棒糖了。。。。")
    w = ["草莓","葡萄"]
    for i in w:
        time.sleep(1)
        print("做了2个棒棒糖。。。")
        c1.send(i)
        c2.send(i)
producer("老高")
