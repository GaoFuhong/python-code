# Author:Fuhong Gao
import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #atm目录
DATABASE = {
    'engine': 'file_storage', #数据库类型，将来可支持mysql,postgresql等
    'name':'accounts',#账户名
    'path': "%s/db" % BASE_DIR #文件路径
}
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}