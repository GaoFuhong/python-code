# Author:Fuhong Gao
import json
f = open('text.text','r')
data = json.loads(f.read())
print(data['age'])