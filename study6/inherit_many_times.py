# Author:Fuhong Gao
#多继承区别
#python 3.x 中经典类和新式类均按广度优先继承
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
class C(A):
    def __init__(self):
        print("C")
class D(B,C):
    def __init__(self):
        print("D")
x = D() #继承顺序是B--C--A