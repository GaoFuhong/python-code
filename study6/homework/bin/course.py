#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import __init__
from saveData import SaveData
class Course(object):
    def __init__(self,courseName,cycle,price,gradeName,schoolName):
        self.courseName=courseName
        self.cycle=cycle
        self.price = price
        self.gradeName = gradeName
        self.schoolName = schoolName
    def courseSave(self,db='../db/course.txt'):
        dict={}
        dict['courseName'] = self.courseName
        dict['cycle'] = self.cycle
        dict['price'] = self.price
        #gradeName,schoolName通过查询获取
        dict['gradeName'] = self.gradeName
        dict['schoolName'] = self.schoolName
        SaveData(dict,db)
