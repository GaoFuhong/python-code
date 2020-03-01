# Author:Fuhong Gao
#递归死循环
# def calc(n):
#     print(n)
#     return calc(n+1)
# calc(0)

#递归函数：不断除以2并取整
def calc(n):
    print(n)
    if int(n/2) >0:
        return (calc(int(n/2)))
    print("结束时n的值:",n)
calc(20)