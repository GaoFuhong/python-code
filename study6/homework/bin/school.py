#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import __init__
from saveData import SaveData
class School(object):
    def __init__(self,schoolName):
        self.schoolName=schoolName
    def schoolSave(self,db='../db/school.txt'):
        dict={}
        dict['schoolName'] = self.schoolName
        SaveData(dict,db)