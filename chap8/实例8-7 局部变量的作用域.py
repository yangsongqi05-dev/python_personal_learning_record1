from unittest import removeResult


def calc(a,b):
    s=a+b
    return s
# print(a,b,s)#a,b,s是局部变量
result=calc(10,20)
print(result)