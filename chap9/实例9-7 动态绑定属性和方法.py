class Student:
    # 类属性，定义在类中，方法外的变量
    school = '北京xxx教育'

    # 初始化方法
    def __init__(self, xm, age):  # xm,age是方法的参数，是局部变量，xm,age作用域是整个__init__方法

        self.name = xm  # 左侧是实例属性，xm是局变量，将局部变量xm赋值给实例属性self.name
        self.age = age  # 实例属性和局部变量的名称可以相同

#定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name},今年：{self.age}岁了')

#创建两个student类的对象
stu=Student('lzx',18)
stu2=Student('张三',22)
print(stu.name, stu.age)
print(stu2.name, stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name, stu2.age,stu2.gender)

#动态绑定方法
def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu2的方法')
stu2.fun=introduce#函数的一个赋值
#调用
stu2.fun()