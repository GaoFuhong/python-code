#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from school import School
from grade import Grade
from selectView import selectSchool
def CreateSchool():
    print('---创建学校信息---')
    schoolName=input('schoolName:')
    s1=School(schoolName)
    s1.schoolSave()
def CreateGrade():
    print('---创建班级信息---')
    gradeName=input('gradeName:')
    print('''
            可选择学校：
            %s
            ''' % selectSchool())
    schoolName = input('schoolName:')
    s1 = Grade(gradeName,schoolName)
    s1.gradeSave()
def CreateCourse():
    print('---创建课程信息---')
    courseName = input('courseName:')
    cycle = input('cycle:')
    price = input('price:')
    gradename = input('gradename:')
def CreateTeacher():
    print('---创建教师信息---')
    teacherName = input('teacherName:')
    gradeName = input('gradeName:')
    schoolName = input('schoolName:')
def CreateStudent():
    print('---创建学生信息---')
    studentName = input('studentName:')
    schoolName = input('schoolName:')
    gradeName = input('gradeName:')
