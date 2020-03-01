# Author:Fuhong Gao
import os
from core import db_handler
from core import logger
from conf import settings
import json
import time

def acc_auth(account,password):
    '''
    账户验证函数
    :param account:验证账户的账号
    :param passwprd:验证密码
    :return:如果登录成功，返回账户；否则，返回None
    '''
    db_path = db_handler.db_handler(settings.DATABASE) #传数据库的信息
    account_file = "%s/%s.json" % (db_path, account) #将账户文件的内容赋值给account_file
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f: #打开文件
            account_data = json.load(f)
            if account_data['password'] == password: #密码正确
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d")) #判断用户是否已过期
                if time.time() > exp_time_stamp: #过期
                    print(
                        "\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else:  # 通过验证
                    return account_data
            else: #没过期
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def acc_login(user_data,log_obj):
    '''
    账户登录函数
    :param user_data:
    :param log_obj:
    :return:
    '''
    retry_count = 0 #初始化输入的次数为0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password) #程序的解耦，将一些功能独立出来：将账户、密码写成一个函数
        if auth:  # not None means passed the authentication（有返回值）
            #登录成功之后，修改全局字典
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            # print("welcome")
            return auth
        retry_count += 1
    else:
        log_obj.error("Account [%s] too many login attempts." % account)
        exit()