# Author:Fuhong Gao
import pickle
def sayhi(name): #pickle反序列化时函数名不变，内容可以改变
    print("Hellooooo,",name)
f = open('text2.text','rb')
data = pickle.load(f) #data = pickle.loads(f.read()),这两句话的意思一样
print(data['func']('gx'))

