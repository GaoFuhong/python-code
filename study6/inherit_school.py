# Author:Fuhong Gao
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.staffs = []
        self.students = []
    def hire(self,staff_obj):
        print("Hired a new staff named %s" %staff_obj.name)
        self.staffs.append(staff_obj)
    def enroll(self,stu_obj):
        print("Handle enroll procedure for %s" %stu_obj.name)
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ------info of Teacher %s------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' %(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course[%s]" %(self.name,self.course))

class Students(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Students,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print('''
        ------info of Student %s------
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' %(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tution(self,amount):
        print("%s has paid tution for ¥%s" %(self.name,amount))

school = School("Sicau","Yaan")
t1 = Teacher("Mantao Wang",39,"Male",6000,"Java")
t2 = Teacher("Xuliang Duan",36,"Male",7000,"MIS")
s1 = Students("Fuhong Gao",22,"Male","9038","MIS")
s2 = Students("Xiao Gu",18,"Female","9015","Python")

school.hire(t2)
school.enroll(s1)
school.enroll(s2)
t1.tell()
s1.tell()
t2.teach()
for stu in school.students:
    stu.pay_tution(6666)



