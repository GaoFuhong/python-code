# Author:Fuhong Gao
string1 = "emmm...\tFuhong Gao loves {name} {how_long}! "
print(string1.capitalize())#字符串首字母大小写
print(string1.count("m")) #计算某个字符串出现的次数
print(string1.center(60,'*'))#指定字符串的长度，不够在两端添规定的符号，并居中显示内容。若小于本来字符串长度，则原样打印
print(string1.endswith('14'))#判断该字符串是否以某个字符串结束，返回布尔值：Ture  False
print(string1.expandtabs(20))#将制表符转换成对应数目的空格
print(string1.find("Gao"))#找到某个字符串在原字符串中的位置，返回索引
#字符串的切片:
print(string1[string1.find("Gao"):20])
print(string1.format(name = 'XiaoGu', how_long = 1314))#格式化
print(string1.format_map({'name':'XiaoGu','how_long':1314})) #字典的格式化
print('A1232'.isalnum())#是否只包含阿拉伯数字和英文，返回布尔值：Ture  False
print('gAOfuhong'.isalpha())#s是否是纯英文字符
print('123'.isdecimal())#是否是一个十进制的数
print('231'.isdigit())#是否是一个正整数
print('_hhh'.isidentifier())#判断是否是一个合法的变量名
print('131313'.isnumeric())#判断是否是一串纯数字
print("I Love Guxiao".istitle())#判断是否是标题（每个单词首字母大写）
print("AAA".isupper())#是否全大写
print('*'.join(["I",'love','you','!']))
print(string1.ljust(50,'*'))
print(string1.rjust(50,'-'))
print(string1.lower()) #把大写变成小写
print('\n\n\naaa'.lstrip())#去掉左边的回车和空格（rstrip去右边，strip去两边）

p = str.maketrans('abcdefg','1234567')#一一对应，再转换
print("I abjabd".translate(p))
print('Fuhong Gao loves XiaoGu'.replace('o','O',1)) #替换对应的元素,加上“,1”表示只替换第一个
print("gaofuhong and gaofuhmmmmm".rfind('gao')) #找到某个元素并且是最右边的索引
print('gao fu hong loves gu xiao 1314! '.split()) #将字符串按照空格（默认）转换成列表，或者按照指定符号划分
print('Gao Loves Xiao'.swapcase())#大小写互换

