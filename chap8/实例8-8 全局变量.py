a=100#全局变量

def calc(x,y):
    return a+x+y
print(a)
print(calc(10,20))
print('-'*30)
def calc2(x,y):
    a=200
    return a+x+y
print(calc2(10,20))#局部变量优先级更高
print(a)
print('-'*30)
def calc3(x,y):
    global a  #让s变成全局变量
    a=300
    return a+x+y
print(calc3(10,20))
print(a)