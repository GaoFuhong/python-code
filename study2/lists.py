# Author:Fuhong Gao
import copy
names = ["FuhongGao","XiaoGu","SanZhang",["xxx","yyy"],"SiLi","WuWang","WuWang"]
print(names)
names2 = names.copy()   #浅copy
print(names2)
names[0] = "高富洪"
print(names)
print(names2)
names[3][0] = "aaa"
print(names)
print(names2)
#names2 = copy.deepcopy(names)  #深copy
#print(names)
#print(names2)

#列表循环
for i in names:
    print(i)

#有步长的切片
print(names[0:-1:2])  #0，-1可以省略，即names[::2]
'''
print(names[0],names[3])
print(names[1:3]) #切片
print(names[-1]) #从后面开始数：倒数第一个是-1
print(names[-2:])

names.append("ZhaoLiu") #在列表末尾加
names.insert(1,"ErWa") #在第1个元素前面插入
names[1] = "SanWa" #修改元素
print(names)
names.remove("SiLi")#删除SiLi
#等价于 del names[4]   也等价于 names.pop(4)     names.pop()表示默认删除最后一个元素
print(names)
print(names.index("SanZhang"))  #查看某个元素的索引
print(names.count("WuWang"))  #查看某个元素出现的次数
names.reverse()   #反转列表中的元素
print(names)
names.sort()    #按照ASCII码排序
print(names)
names2 = [1,2,3,4]
names.extend(names2) #扩展，把两个列表连接起来
print(names,names2)
print(names)
print(names2)'''

