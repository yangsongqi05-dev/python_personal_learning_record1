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


#根据图纸可以创建出N多个对象
stu=Student('lzx',18)
stu2=Student('张三',22)
stu3=Student('李四',19)
stu4=Student('王二',20)

print(type(stu))

Student.school='python教育'#给类的属性赋值

#将学生对象存储到列表当中
lst=[stu,stu2,stu3,stu4]#列表当中的元素是Student类型的对象
for item in lst:
    item.show()








