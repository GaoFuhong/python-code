# Author:Fuhong Gao
mod1 = __import__("lib.aa") #导入模块lib（这是Python解释器自己内部用的）
obj1 = mod1.aa.C() #对aa中的对象C实例化
print(obj1.name)

#第二种形式
import importlib
mod2 = importlib.import_module("lib.aa") #导入lib.aa（官方建议用这个）
obj2 = mod2.C()
print(obj2.name)

#断言
assert type(obj2.name) is str #断言obj2.name是一个字符串，如果断言正确才执行之后的代码
print("Pass!")