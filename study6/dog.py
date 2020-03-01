# Author:Fuhong Gao
class Dog():
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("%s wang wang wang..."%self.name)
d1 = Dog("San Zhang")
d2 = Dog("Si Li")
d3 = Dog("Wu Wang")

d1.bulk()
d2.bulk()
d3.bulk()