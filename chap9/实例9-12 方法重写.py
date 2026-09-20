class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'大家好我的姓名是{self.name},我今年{self.age}岁')


#Student继承Person
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score


    def show(self):
        #调用父类的方法
        super().show()
        print(f'我的分数是{self.score}')
#Dockor继承Person
class Docdor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

    def show(self):
        #调用父类的方法
        super().show()
        print(f'我的工作部门是{self.department}')

stu=Student('lzx',18,80)
stu.show()

doctor=Docdor('ysq',20,'外科')
doctor.show()