# Author:Fuhong Gao
name = input("Name:")
age = int(input("Age:"))
print(type(age),type(str(age)))
sex = input("Sex:")
height = input("Height:")
info = '''
----------info of {_name}  ----------
Age:{_age}
Sex:{_sex}
Height:{_height}
'''.format(_name = name,
           _age = age,
           _sex = sex,
           _height = height,)
print(info)