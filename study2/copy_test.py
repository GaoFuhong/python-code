# Author:Fuhong Gao
import copy
person = ["name", ["money",100]]

#三种类型的浅copy
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
print(p1)
print(p2)
print(p3)
'''

p1 = person[:]
p2 = person[:]
p1[0] = "FuhongGao"
p2[0] = "XiaoGu"

p1[1][1] = 50  #浅copy一般用来创建联合账号
print(p1)
print(p2)


#元组（tuple）,只有两种方法
names = ("XiaoGu","FuhongGao","XiaoGu","SiLi")
count1 = print(names.count("XiaoGu"))   #计数
index1 = print(names.index("XiaoGu"))   #求元素的索引
