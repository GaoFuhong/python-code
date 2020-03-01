# Author:Fuhong Gao
#用于索引操作，如字典。
class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key): #获取数据
        print("__getitem__:", key)
        return self.data.get(key)
    def __setitem__(self, key, value): #设置数据
        print("__setitem__:", key,value)
        self.data[key] = value
    def __delitem__(self, key): #删除数据
        print("__delitem__:", key)
obj =Foo()
obj['name'] = 'Fuhong Gao'
print(obj['name'])
print(obj.data)