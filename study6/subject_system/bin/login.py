# Author:Fuhong Gao
import __init__
from role import Role

def loginF(role):
    flag=True
    print('当前角色编码是：%s' %role)
    while flag:
        exits=0
        user = input('用户：')
        password = input('密码：')
        f=open('../db/user.txt','r')
        data=f.readlines()
        print('用户数据：',data)
        for i in data:
            i=i.replace('\n','').split(' ')
            #print('校验密码',i[0],i[1],i[2])
            #print('校验密码', user.txt, password, role)
            if i[0]==user and i[1]==password and i[2]==role:
                exits=1
        if exits==1:
            print('用户校验成功！')
            r=Role(role,user)
            r.selectType()
        else:
            print('用户名或密码错误！')
