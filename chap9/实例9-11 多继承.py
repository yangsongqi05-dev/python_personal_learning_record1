


class FatherA:
    def __init__(self,name):
        self.name=name

    def showA(self):
        print('父类A中的方法')


class FatherB:
    def __init__(self, age):
        self.age= age

    def showB(self):
        print('父类B中的方法')

#多继承
class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        self.gender=gender
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)

son=Son('lzx','18','男 ')
son.showA()
son.showB()



















