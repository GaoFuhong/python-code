# Author:Fuhong Gao
#事件 红绿灯程序
import threading,time
event = threading.Event() #事件实例
def lighter():
    count = 0
    event.set() #进入循环之前设一个标志位
    while True:
        if count >= 6 and count < 10: #6秒之后变成红灯,并持续4秒
            event.clear() #把标志位清除,等待重新被设定
            print("\033[41;1m----Red light is on----\033[0m")
        elif count >= 10:
            event.set() #变成绿灯
            count = 0
        else:
            print("\033[42;1m----Green light is on----\033[0m")
        time.sleep(1)
        count += 1
def car(name):
    while True:
        if event.is_set(): #设置了标志位，代表绿灯
            print("[%s] is running..." %name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..." %name)
            event.wait()
            print("\033[34;1mGreen light is on, start going...\033[0m")
light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=("FengTian",))
car1.start()
car2 = threading.Thread(target=car,args=("BaoMa",))
car2.start()
