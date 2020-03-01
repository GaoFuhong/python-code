# Author:Fuhong Gao
class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("__MyType init__")
        super(MyType, self).__init__(what, bases, dict)
    def __call__(self, *args, **kwargs):
        print("__MyType call__")
        obj = self.__new__(self, *args, **kwargs)
        obj.data = {"name":111}
        self.__init__(obj, *args, **kwargs)

class Foo(object):
    __metaclass__ = MyType
    def __init__(self, name):
        self.name = name
        print("Foo __init__")
    def __new__(cls, *args, **kwargs): #__new__是用来创建实例的
        print("Foo __new__")
        return object.__new__(cls) #继承父亲的__new__方法
obj = Foo("gfh")
print(obj.name)