#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import __init__
from saveData import SaveData
class Grade(object):
    def __init__(self,gradeName,schoolName):
        self.gradeName=gradeName
        self.schoolName=schoolName
    def gradeSave(self,db='../db/grade.txt'):
        dict={}
        dict['gradeName'] = self.gradeName
        dict['schoolName'] = self.schoolName
        SaveData(dict,db)