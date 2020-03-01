# Author:Fuhong Gao
import queue
q = queue.PriorityQueue() #存储数据时可以设置优先级的队列
#存储数据并设置优先级
q.put('Si Li',-1)
q.put('Xiao Gu',10)
q.put('Fuhong Gao',15)
q.put('San Zhang',0)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
'''
q = queue.LifoQueue() #Last in first out
q.put(1) #往队列里存数据
q.put(2)
q.put(3)
print(q.get()) #取数据
print(q.get())
print(q.get())
'''