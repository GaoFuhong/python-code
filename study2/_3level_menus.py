# Author:Fuhong Gao
#建立一个字典，
data = {
    '雅安校区':{
        '信息工程学院':{
            '计算机科学':['C语言','Java'],
            '物联网':['数据结构','物联网技术'],
            '信息管理与信息系统':['网站设计','管理信息系统'],
        },
        '理学院':{
            '信息科学与技术':['高等数学','数字分析'],
            '应用数学':['数学建模','概率论'],
            '应用物理学':['大学物理A','结构力学'],
        },
        '生命科学学院': {
            '化学生物': ['有机化学', '植物学'],
            '应用化学': ['无机化学', '化学实验'],
        },
    },
    '成都校区':{
        '农学院':{
            '植物遗传育种':['植物育种学','遗传学'],
            '农学':['植物生理学','种子学']
        },
        '动物科技学院':{
            '动物科学':['动物科学','动物医学'],
            '水产养殖':[' 鱼类增养殖学','水生生物学'],
        },
    },
    '都江堰校区':{
        '土木工程学院':{
            '建筑工程':['土木工程制图与CAD','工程测量'],
            '给排水科学与工程':['水力学','水分析化学'],
        },
        '商学院':{
            '市场营销':['市场营销学','经济学'],
            '资产评估':['资产评估学','会计学'],
        },
    }
}
exit_falg = False
while not exit_falg:
    for i in data:
        print(i)
    choice1 = input("选择四川农业大学的校区>>")
    if choice1 in data:
        while not exit_falg:
            for j in data[choice1]:
                print('\t',j)
            choice2 = input("选择该校区的学院>>")
            if choice2 in data[choice1]:
                while not exit_falg:
                    for k in data[choice1][choice2]:
                        print('\t\t',k)
                    choice3 = input("选择该学院的专业>>")
                    if choice3 in data[choice1][choice2]:
                        while not exit_falg:
                            print('该专业的主修课程：')
                            for l in data[choice1][choice2][choice3]:
                                print('\t\t\t',l)
                            choice4 = input("已经在最后一层，按B返回上一层，按Q退出！")
                            if choice4 == 'B':
                                pass
                            elif choice4 == 'Q':
                                exit_falg = True
                    elif choice3 == 'B':
                        break
                    elif choice3 == 'Q':
                        exit_falg = True
            elif choice2 == 'B':
                break
            elif choice2 == 'Q':
                exit_falg = True
