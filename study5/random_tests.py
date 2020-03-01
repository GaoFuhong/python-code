# Author:Fuhong Gao
import random
print(random.random()) #随机生成0-1之间的浮点数
print(random.uniform(2,5)) #随机生成指定区间的浮点数
print(random.randint(1,5)) #随机生成1-5的整数，包括1和5
print(random.randrange(1,5)) #随机生成1-5的整数，包括1但不包括5
#random.choice()从序列中随机取出一个元素
print(random.choice('hello'))
print(random.choice([1,2,3,10,6,8,7]))
print(random.choice(('a','d','d','r','o','j')))
print(random.sample('sihfoifoiafoa',3)) #从序列中随机取三位构成一个列表
a = [1,2,3,4,5,6,7,8,9,10,11,12]
random.shuffle(a) #洗牌功能，打乱列表中元素的顺序
print(a)