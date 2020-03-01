# Author:Fuhong Gao
#json不能对序列化多次的内容进行反序列化
import json
f = open('text3.text','r')
data = json.loads(f.read())
print(data)