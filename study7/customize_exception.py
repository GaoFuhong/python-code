# Author:Fuhong Gao
#自定义异常
class GfhError(Exception):
    def __init__(self, msg):
        self.message = msg
    # def __str__(self):
    #     return 'sdfsf'
try:
    raise GfhError('数据库连不上')
except GfhError as e:
    print(e)