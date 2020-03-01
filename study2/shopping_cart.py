# Author:Fuhong Gao
'''
#有问题！！！
salary = input("Please input your salary:")
print("Thank you! Your salary is {your_salary}".format(your_salary = salary))
info_goods = [[1,"iPhone",5888],[2,"camera",6999],[3,"TV",4500],[4,"air_conditioner",3899],[5,"bicycle",1999],[6,"watch",269]]
have_bought = []
for i in range(6):
    num = input("Please input a number of the goods you want :")
    for j in range(1,7):  #找对应商品的编号
        print(j)
        if j == num:
            print("The number of goods is {your_num},the goods is {your_goods},and the price of goods is {your_price}".format(your_num = info_goods[j-1][0],your_goods = info_goods[j-1][1],your_price = info_goods[j-1][2]))
            if salary >= info_goods[j-1][2]:
                salary = salary - info_goods[j-1][2]
                have_bought = have_bought.append([info_goods[j-1]])
            else:
                print("Your balance is not enough!")
            break
    else:
        print("Your number is error!")
    ask = input("Do you want to keep shopping? Please input 'Y' or 'N'.")
    ans = ask
    if ans == "N":
        break
print("The information you bought are : {_info}".format(_info = have_bought))
print("Your balance is {_balance}".format(_balance = salary))
'''

#正确购物车代码
produc_list = [
    ("iPhone",5888),
    ("camera",6999),
    ("TV",4500),
    ("air_conditioner",3899),
    ("bicycle",1999),
    ("watch",269),
]#商品列表信息
shopping_list = []#建一个空的购物车列表
salary = input("Please input your salary:")#输入工资
if salary.isdigit():
    salary = int(salary)#如果工资是一个数字，转换成整型
while True:
    for index, item in enumerate(produc_list):
        print(index, item)#打印商品列表的索引和元素
    user_choice = input("What do you want to buy? Please input the index.")#用户输入商品的索引
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(produc_list) and user_choice >= 0:
            product_item = produc_list[user_choice]#输入的数字在商品列表的长度范围之类
            if product_item[1] <= salary:#商品价格不大于工资的情况
                shopping_list.append(product_item)#将所选商品加入购物车
                salary -= product_item[1]#计算工资余额
                print("Added %s into your shopping cart,and your current balance is \033[32;1m%s\033[0m"%(product_item,salary))
            else:
                print("Your current is only \033[31;1m%s\033[0m!"%(salary))#商品价格已经超出工资余额
        else:
            print("The product'index \033[31;1m%s\033[0m is not exist!"%(user_choice))#输入的数字不符合要求
    elif user_choice == "Q":#选择退出
        print("---------shopping lists---------")
        for p in shopping_list:
            print(p)#打印购物车的商品
        print("Your current banlace:\033[41;1m%s\033[0m."%(salary))#打印余额
        exit()#退出
    else:
        print("Invalid option!")#非法输入
