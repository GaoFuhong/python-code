# Author:Fuhong Gao
from urllib import parse
from urllib import request
url = 'http://www.baidu.com/s?'
dict1 = {'wd':'百度地图'}
url_data = parse.urlencode(dict1) #将字典{k1:v1,k2:v2}转换为k1=v1&k2=v2
print(url_data)
data = request.urlopen((url+url_data)).read() #读取url的响应结果
data = data.decode('utf-8') #编码
# print(data)
url_org = parse.unquote(url_data) #解码
print(url_org)
