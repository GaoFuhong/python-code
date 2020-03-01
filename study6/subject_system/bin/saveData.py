# Author:Fuhong Gao
import pickle
def SaveData(dict,db):
    try:
        f = open(db, 'wb')
        f.write(pickle.dumps(dict))
        print('数据保存成功')
    except Exception as e:
        print('系统异常')