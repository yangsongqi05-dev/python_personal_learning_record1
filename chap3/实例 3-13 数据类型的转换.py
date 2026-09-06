x=10
y=3
z=x/y #在执行除法运算的时候，将运算结果赋值给z
print(z,type(z))#隐式转换，通过运算隐式的转了结果的类型

#float类型转为int，只保留整数
print("float类型转化为int：",int(3.14))
#int转float
print(float(3))
#str转int
print(int('100')+int('100'))
#str转为int或float会报错的情况
#print(int('18a'))#ValueError: invalid literal for int() with base 10: '18a'
#print(int('3.14'))#ValueError: invalid literal for int() with base 10: '3.14'

#chr()ord()一对
print(ord('杨'))#杨在unicode对应的整数值
print(chr(26472))#26472在unicode对应的字符

#进制之间的转化
print('十进制转十六：',hex(26472))
print('十进制转八：',oct(26472))
print('十进制转二：',bin(26472))