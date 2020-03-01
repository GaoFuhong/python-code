# Author:Fuhong Gao
#随机生成一个包含字母和数字的4位验证码
import random
verification_code = '' #定义一个全局变量
for i in range(4): #循环4次，i的值依次是0,1,2,3,
    if random.randrange(0,4) == i: #如果i的值等于随机生成的1-4（不包括4）中的值
        temp = chr(random.randint(97,122)) #随机生成一个小写字母赋给临时变量temp
        #如果要同时生成大小写字母，目前本人只想到 temp = random.choice(['a','b','c',…，'z','A','B',…，'Z'])
    else:
        temp = random.randint(0,9) #不等则生成一个0-9的随机数字
    verification_code += str(temp)
print(verification_code)
