# Author:Fuhong Gao
'''
主程序处理模块，处理所有的用户交互任务
'''

#导入core目录下的其他模块：
from core import auth
from core import logger
from core import accounts
from core import transaction
import time

trans_logger = logger.logger('transaction') #和logger的交互
access_logger = logger.logger('access') #记录日志，全局的日志模块，每次直接添加内容，不用像文件一样打开、关闭

#临时的账户数据，是最初的信息：
user_data = {
    'account_id':None, #账户ID最初为空
    'is_authenticated':False, #是否登录（最初未登录）
    'account_data':None #存账户数据
}

def account_info(acc_data):
    print(user_data)

def repay(acc_data):
    '''
    显示余额并还款
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            # print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)
        if repay_amount == 'b':
            back_flag = True

def withdraw(acc_data):
    '''
    打印当前的余额、取款
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
        if withdraw_amount == 'b':
            back_flag = True

def transfer(acc_data):
    pass
def pay_check(acc_data):
    pass
def logout(acc_data):
    pass
def interactive(acc_data):
    '''
    交互
    :param acc_data:
    :return:
    '''
    menu = u'''
    ----------- GFH Bank -----------
         \033[32;1m1.  账户信息
        2.  还款(功能已实现)
        3.  取款(功能已实现)
        4.  转账
        5.  账单
        6.  退出
        \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    } #数字对应相应的函数名
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    当程序启动时，这个函数会被立刻调用，它处理与用户的交互任务。
    :return:
    '''
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)