


class Student():
    #首位双下划线
    def __init__(self,name,age,score):
        self._name=name #self._name受保护的，只能本类和子类访问
        self.__age=age #self.__age表示私有，只能本类去访问
        self.score=score #普通实例属性，类的内部，外部，子类都可以访问

    def _fun1(self):
        print('子类及本身可以访问')

    def __fun2(self):#私有的
        print('只有定义的可以访问')

    def fun3(self):
        self._fun1()#类本身访问受保护的方法
        self.__fun2()#类本身访问私有的方法
        print(self._name)#受保护的实例属性
        print(self.__age)#私有的实例属性

#创建一个学生类的对象
stu=Student('lzx',18,20)
#类的外部
print(stu._name)
# print(stu.__age)#AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
stu._fun1()
# stu.__fun2()#AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?

#私有的其实也能访问
print(stu._Student__age)
stu._Student__fun2()

print(dir(stu))