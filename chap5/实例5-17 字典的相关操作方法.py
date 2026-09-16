d={1001:'李梅',1002:'张三',1003:'李四'}
print(d)

#向字典中添加元素
d[1004]='王二'#直接用赋值运算符向字典中添加元素
print(d)

#获取字典中所有key
key=d.keys()
print(key)#dict_keys([1001, 1002, 1003, 1004])
print(list(key))
print(tuple(key))

#获取字典中的所有value
value=d.values()
print(value)
print(list(value))
print(tuple(value))

#如果将字典中的数据转成key-value的样式，以元组的方式展现
lst=list(d.items())
print(lst)

lst=dict(d.items())
print(lst)

#使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))

print(d.popitem())#随机删除
print(d)

#清空字典中的所有元素
d.clear()
print(d)
#python中一切皆对象，每一个对象都有一个布尔值
print(bool(d))
