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

#静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    @classmethod
    def cm(cls):#cls---->class的简写
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

#创建类的对象
stu=Student('ysq',18)
#实例属性，使用对象名进行打点调用
print(stu.name,stu.age)

#类属性，直接类目打点调用
print(Student.school)

#实例方法，使用对象名进行打点调用
stu.show()

#静态方法，类名打点调用
Student.cm()