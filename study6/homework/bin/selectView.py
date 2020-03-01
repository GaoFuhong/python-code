#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import __init__
import pickle
from school import School
def selectSchool(db='../db/school.txt'):
    f = open(db, 'rb')
    data=pickle.loads(f.read())
    return data['schoolName']
def selectGrade(db='../db/grade.txt'):
    #传入学校名称查询班级
    f = open(db, 'rb')
    data=pickle.loads(f.read())
    return data['schoolName']
def selectCourse(db='../db/course.txt'):
    # 传入学校名称查询课程
    f = open(db, 'rb')
    data=pickle.loads(f.read())
    return data['schoolName']
def selectStuent(db='../db/student.txt'):
    # 传入学校名称、班级名称查询学生
    f = open(db, 'rb')
    data=pickle.loads(f.read())
    return data['schoolName']['gradeName']