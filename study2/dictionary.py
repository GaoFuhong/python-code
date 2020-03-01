# Author:Fuhong Gao
'''
info = {
    'stu1101': 'Fuhong Gao',
    'stu1102': 'Xiao Gu',
    'stu1103': 'San Zhang',
    'stu1104': 'Si Li'
}
print(info.get('stu1105'))#查找，没有在字典中就显示None

print('stu1102' in info) #判断某个键是否在字典中

print(info)
print(info['stu1102']) #查
info['stu1101'] = '高富洪' #改
print(info)
info['stu1105'] = 'Wu Wang' #增
print(info)
del info['stu1103'] #删
#等价于info.pop(info['stu1103'])
print(info)
'''

'''
#dictionary nesting
food_lists = {
    "vegetables": {
        'potato': ['blocky, starch', '3 yuan per kilogram'],
        'tomato': ['red,can be eaten row', '4 yuan per kilogram'],
        'carrot': ['slender,rich in carotenoids','5 yuan per kilogram'],
    },
    "fruits": {
        "mango": ['yellow,growing in the tropics','14 yuan per kilogram'],
        "grape": ['purple,string','10 yuan per kilogram'],
        "banana": ['yellow,bent','6 yuan per kilogram'],
    },
    "coarse_grain": {
        "corn":  ["have kinds of types,such as sweet corn,waxy corn",'6 yuan per kilogram'],
        "soy": ["rich in protein",'5 yuan per kilogram'],
    }
}
food_lists["fruits"]["mango"][1] = '100 yuan per kilogram'
print(food_lists)
print(food_lists.keys()) #打印键
print(food_lists.values())#打印值
#加入新的内容，如果加入的内容的键在原来的字典中，则按照原字典中的值打印
food_lists.setdefault("biscuit",{"quduoduo":['have chocolate','9 yuan per bag']})
print(food_lists)
'''

#字典的更新与合并
'''
info = {
    'stu1101': 'Fuhong Gao',
    'stu1102': 'Xiao Gu',
    'stu1103': 'San Zhang',
    'stu1104': 'Si Li'
}

info2 = {
    'stu1103': 'Ermazi Wang',
    1: 'abc',
    2: 5,
}
info.update(info2)
print(info)
print(info.items())#将一个字典转换成一个列表，每个元素就是原字典中的键值对

c = dict.fromkeys([6,7,8],[1,{'name':'xxx'},'abc']) #初始化一个新的字典
print(c)
c[7][1]['name'] = 'ZZZZZZ' #改一个，字典里的内容就都改了
print(c)
'''

#字典的循环
info = {
    'stu1101': 'Fuhong Gao',
    'stu1102': 'Xiao Gu',
    'stu1103': 'San Zhang',
    'stu1104': 'Si Li'
}
for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)

#两种循环的区别：第一种比第二种的效率高，因为第二种有一个把字典转换成列表的过程