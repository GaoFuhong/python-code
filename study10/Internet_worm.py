# Author:Fuhong Gao
#爬网页（遇到io阻塞时会自动切换任务）
from gevent import monkey #打个补丁monkey
monkey.patch_all() #把当前程序的所有io操作单独做上标记
import gevent#gevent检测不到urllib的io操作
from urllib import request
import time
def f(url):
    print('GET:%s' %url)
    resp = request.urlopen(url)
    data = resp.read()
    # f = open('url.html','wb')
    # f.write(data)
    # f.close()
    print('%s bytes received from %s' %(len(data),url))
urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://www.github.com/']
# f('http://www.sicau.edu.cn')
time_start = time.time()
for url in urls: #串行
    f(url)
print('同步cost:', time.time() - time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'https://www.yahoo.com/'),
    gevent.spawn(f,'https://www.github.com/')
])
print('异步cost:',time.time() - async_time_start)