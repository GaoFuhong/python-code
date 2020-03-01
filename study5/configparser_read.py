# Author:Fuhong Gao
import configparser
config = configparser.ConfigParser()
config.read('example.ini') #读取文件
print(config.defaults()) #打印DEFAULT中的内容
print(config['bitbucket.org']['User']) #打印节点中的内容

sec = config.remove_section('bitbucket.org') #删除节点'bitbucket.org'
config.write(open('new_example.ini','w'))