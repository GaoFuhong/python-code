#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import pickle
def SaveData(dict,db):
    try:
        f = open(db, 'wb')
        f.write(pickle.dumps(dict))
        print('数据保存成功！')
    except Exception as e:
        print('系统异常')