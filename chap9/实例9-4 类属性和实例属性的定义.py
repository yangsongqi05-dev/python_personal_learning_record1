class Student:
    #类属性，定义在类中，方法外的变量
    school='北京xxx教育'

    #初始化方法
    def __init__(self,xm,school):#xm,age是方法的参数，是局部变量，xm,age作用域是整个__init__方法

        self.name=xm#左侧是实例属性，xm是局变量，将局部变量xm赋值给实例属性self.name
        self.school=school#实例属性和局部变量的名称可以相同
        