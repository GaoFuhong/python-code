#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import __init__
import sys
import role
from login import loginF
if __name__=='__main__':
    while True:
        print('''
        =====================================
        请选择角色：
            1、管理员
            2、学校
            3、讲师
            4、学生
            Q|q、退出
        =====================================
        ''')
        data=input('输入序号即可：')
        if data=='1':
            loginF(data)
        elif data=='2':
            loginF(data)
        elif data=='3':
            loginF(data)
        elif data=='4':
            loginF(data)
        elif data=='Q' or data=='q':
            exit(1)
        else:
            print('无效字符，请重新输入')
