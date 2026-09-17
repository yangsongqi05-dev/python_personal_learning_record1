s='HelloWord'
#字符串的替换
new_s=s.replace('o','你好')
print(new_s)

#字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

#去掉字符串左右的空格
s='   Hello   Word    '
print(s.strip())#两侧都去掉
print(s.lstrip())#去掉左侧的
print(s.rstrip())#去掉右侧的

#去掉指定的字符
s3='dl-helloword'
print(s3.strip('dl'))#与顺序无关包含ld都去
print(s3.lstrip('dl'))#去掉左侧的
print(s3.rstrip('dl'))#去掉右侧的
