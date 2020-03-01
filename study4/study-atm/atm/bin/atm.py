# Author:Fuhong Gao
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #返回到atm这一层目录
print(base_dir)
sys.path.append(base_dir) #增加的环境变量
from core import main
if __name__ == '__main__':
    main.run()