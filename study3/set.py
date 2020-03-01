# Author:Fuhong Gao
list_1 = [1,3,5,6,0,14,0,2,1,5]
list_1 = set(list_1) #将列表转换成集合
print(list_1,type(list_1)) #打印集合并查看元素类型
list_2 = set([1,22,8,14,7,1])#新建一个集合
print(list_1.intersection(list_2))#求list_1和list_2的交集
print(list_1.union(list_2))#求list_1和list_2的并集
print(list_1.difference(list_2))#求list_1和list_2的差集，在list_1但不在list_2里
print(list_2.difference(list_1))#求list_2和list_1的差集，在list_2但不在list_1里
list_3 = set([1,14])
print(list_3.issubset(list_1)) #判断list_3是否是list_1的子集
print(list_2.issuperset(list_3)) #判断list_2是否是list_3的父集
print(list_1.symmetric_difference(list_2)) #对称差集，list_1和list_2的并集减交集
list_4 = set([0,5,8])
print(list_3.isdisjoint(list_4)) #如果list_3和list_4的交集为空，则返回True

#运算符求交、并、差、对称差集
print(list_1 &list_2)
print(list_1 | list_2)
print(list_1 - list_2)
print(list_1 ^ list_2)

#基本操作：
list_1.add('abc')#添加1项
list_1.update([888,999,3.5])
print(list_1)
list_1.remove(3.5) #删除某一项
print(list_1)
print(len(list_1)) #计算集合的长度

print('abc' in list_1) #判断某个元素是否在集合中
print(2 not in list_1)
print(list_1.pop())#任意删除一个元素
list_1.discard('gfh')#指定删除一个元素，如果不存在，pass
print(list_1)
list_1.discard(888)
print(list_1)
