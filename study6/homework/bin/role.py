#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
from createUser import CreateSchool,CreateGrade,CreateCourse,CreateTeacher,CreateStudent
__author__ = "Colby"
class Role(object):
    def __init__(self,role,user):
        '''
        :param role: 角色类别编码
        :param user: 用户名称
        '''
        print('Role视图')
        self.role=role
        self.user = user
    def roleAdmin(self):
        print('''======欢迎您管理员：%s======
        您有如下权限：
            1、创建学校
            Q|q、退出
        ==================='''%self.user)
        data = input('请选择：')
        if data == '1':
            CreateSchool()
        else:
            exit(1)
        self.roleAdmin()
    def roleSchool(self):
        print('''======欢迎您学校：%s======
                您有如下权限：
                    1、创建班级
                    2、创建讲师
                    3、创建课程
                    4、创建学生用户
                    Q|q、退出
                ===================''' % self.user)
        data=input('请选择：')
        if data=='1':
            CreateGrade()
        elif data=='2':
            CreateCourse()
        elif data=='3':
            CreateTeacher()
        elif data=='4':
            CreateStudent()
        else:
            exit(1)
        self.roleSchool()
    def roleTeacher(self):
        print('''======欢迎您老师：%s======
                您有如下权限：
                    1、选择班级
                    2、查看学员列表
                    3、修改学员成绩
                    Q|q、退出
                ===================''' % self.user)
    def roleStudent(self):
        print('''======欢迎您学生：%s======
                您有如下权限：
                    1、注册
                    2、缴费
                    3、选择班级
                    Q|q、退出
                ===================''' % self.user)
    def selectType(self):
        if self.role == '1':
            print('role当前为%s' %self.role)
            self.roleAdmin()
        elif self.role == '2':
            self.roleSchool()
        elif self.role == '3':
            self.roleTeacher()
        elif self.role == '4':
            self.roleStudent()
        else:
            pass
