class Student:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    #使用@property 修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

        # 将我们的gender这个属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != '男' and value != '女':
            print('性别有误已将默认值设置为男')
            self.__gender = '男'
        else:
                self.__gender = value


stu=Student('lzx','女')
print(stu.name,'的性别是',stu.gender)

stu.gender='其他'
print(stu.name,'的性别是',stu.gender)



