# Author:Fuhong Gao
#序列化多次
import json
info = {
    'name':'gfh',
    'age':22
}
f = open('text3.text','w')
f.write(json.dumps(info))
info['age'] = 23
f.write(json.dumps(info))
f.close()