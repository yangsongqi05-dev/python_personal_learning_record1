class Person:
    def eat(self):
        print('人，要吃饭')

class Cat:
    def eat(self):
        print('猫，要吃鱼')

class Dog:
    def eat(self):
        print('狗，要吃骨头')

#这三个类中有一个同名的方法，eat
#编写函数
def fun(obj):#obj形式参数，
    obj.eat()#通过变量obj调用eat方法

#创建对象
per=Person()
cat=Cat()
dog=Dog()
#调用fun函数
fun(per)
fun(cat)
fun(dog)