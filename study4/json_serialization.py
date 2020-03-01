# Author:Fuhong Gao
import json #只能序列化一些简单的内容，列表、字典等，不能序列化函数
info = {
    'name':'gfh',
    'age':22
}
f = open('text.text','w')
f.write(json.dumps(info))
f.close()