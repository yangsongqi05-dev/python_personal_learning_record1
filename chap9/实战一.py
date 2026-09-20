class Circle:
    def __init__(self,r):
        self.r = r
    def get_area(self):
#return 3.14*self.r*self.r
        return 3.14*pow(self.r,2)
    def get_perimeter(self):
        return 2*3.14*self.r

#创建对象
r=eval(input('请输入半径：'))
c=Circle(r)
#调用对象
area=c.get_area()
perimeter=c.get_perimeter()
print('圆的面积为：',area)
print('圆的周长为：',perimeter)
