from ctypes import pythonapi

luck_number=8
my_name = '罗志祥'

print('luck_number的数据类型是：',type(luck_number))
print(my_name,'的幸运数字是：',luck_number)

#python动态修改变量的数据类型，通过赋不同的值可以直接更改
luck_number='北京欢迎你'
print('luck_number的数据类型是',type(luck_number))

#在python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(number))#id()查看对象内存地址
print(id(number))
