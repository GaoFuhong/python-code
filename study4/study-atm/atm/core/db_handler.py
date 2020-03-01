# Author:Fuhong Gao
'''
处理所有的数据库交换
'''
def file_db_handle(conn_params): #数据库为文件形式
    '''
    parse the db file path
    :param conn_params: the db connection params set in settings
    :return:
    '''
    print('file db:',conn_params)
    db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    return db_path

def mysql_db_handle(conn_parms): #数据库为mysql形式
    pass
def db_handler(conn_parms):
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:a
    '''

    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)

    if conn_parms['engine'] == 'mysql':
        return mysql_db_handle(conn_parms)