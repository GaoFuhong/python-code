# Author:Fuhong Gao
#协程实例（使用yield实现）
import time
def consumer(name):
    print('-->start eatting bun...')
    while True:
        new_bun = yield
        print('%s is eatting bun-%s'%(name,new_bun))
def producer(name):
    r = c1.__next__()
    r = c2.__next__()
    n = 0
    while n < 5:
        n += 1
        c1.send(n)
        c2.send(n)
        time.sleep(1)
        print('\033[32;1m%s is making bun-%s\033[0m' %(name,n))
if __name__ == '__main__':
    c1 = consumer('San Zhang')
    c2 = consumer('Si Li')
    p = producer('Boss')