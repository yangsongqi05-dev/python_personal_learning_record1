#format()
print(format(3.14,'20'))#数值默认右对齐
print(format('hello','20'))#字符串默认左对齐
print(format('hello','*<20'))
print(format('hello','*>20'))
print(format('hello','*^20'))#居中
print(format(3.16,'10.2'))#右对齐10个字符长度并保留2位数字会四舍五入

print(eval('10>30'))