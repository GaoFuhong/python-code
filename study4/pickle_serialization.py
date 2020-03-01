# Author:Fuhong Gao
import pickle
def sayhi(name):
    print("Hello,",name)
info = {
    'name':'gfh',
    'age':22,
    'func':sayhi
}
f = open('text2.text','wb')
pickle.dump(info,f) #f.write(pickle.dumps(info))，这两句话的意思一样
f.close


