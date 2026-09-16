#（1）创建字典


d={10:'cat',20:'dog',30:'zoo',20:'pet'}
print(d)#key相同时，后面会覆盖前面的

#zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zip1=zip(lst1,lst2)
print(zip1)
d=dict(zip1)
print(d)
#{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

#使用参数创建字典
d=dict(cat=10,dog=20,zoo=30,pet=40)
print(d)

t=(20,30,40)
print({t:10})

# lst=[10,20,30]
# print({lst:10})
#报错

#字典属于序列
print('max',max(d))
print('min',min(d))
print('len',len(d))
#字典删除
del d

