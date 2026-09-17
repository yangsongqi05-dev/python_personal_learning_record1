s='helloword'
print('{0:*<20}'.format(s))#字符串的显示宽度为20，左对齐，空白部分用*填充
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

#居中对其center
print(s.center(20,'*'))

#千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(78994562))
print('{0:,}'.format(78994562.5258))

#浮点数的小数部分的精度
print('{0:0.2f}'.format(3.1415926))
#字符串类型，表示是最大的显示长度
print('{0:.5}'.format('helloworld'))

#整数类型
a=425
print('二进制：{0:b},十进制：{0:d},八进制：{0:o},十六进制：{0:x}'.format(a))

#浮点数类型
print('{0:0.2f},{0:.2E},{0:.2e},{0:.2%}'.format(a))