s='3.14+3'
print(s,type(s))
x=eval(s) #使用eval函数去掉s这个字符串的引号，执行加法算法
print(x,type(x))

#eval函数经常与input（）函数一起使用，用获取用户输入的数值
age=eval(input('Enter your age:'))#将字符串类型转成了int类型，相当于int（age）
print(age,type(age))

