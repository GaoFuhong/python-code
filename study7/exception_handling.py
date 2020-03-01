# Author:Fuhong Gao
#异常处理
def bark(self):
    print("%s is barking..." %self.name)
class Dogs(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eatting " %self.name, food)
d = Dogs("Xiaohuang")
# choice = input(">>:").strip()
list1 = ['gfh' , 'gx' , 123]
dict1 = {}
try:
    # print(list1[3])
    # dict1['name']
    # open('test1,txt')
    # getattr(d,choice)
    a = 1
    print(a)
except IndexError as e:
    print("列表操作错误", e)
#可以同时判断多个错误，但最好这些错误的处理办法都是一样的
except (IndexError,KeyError) as e:
    print("同样的错误处理", e)
except Exception as e: #在抛出异常的最后使用，之前的错误都没有找到
    print("未知错误")
else: #没有错误时执行
    print("一切正常！")
finally:
    print("不管有没有错，都执行。")
# except AttributeError as e:
#     print("没有这个方法",e)
#抓住所有的错误
'''
except Exception as e:
    print("出错了。。。",e)
'''



