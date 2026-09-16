d={'hello':10,'python':20,'world':30}
#访问字典中的元素
#1.使用d[key]
print(d['hello'])
#2.使用d.get
print(d.get('python'))

#二者直接是有区别的，如果key不存在，d[key]会报错，d.get可以指定默认的值
# print(d['java'])#KeyError: 'java'
print(d.get('java'))
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item)

#在使用for循环遍历时，分别获取key,value
for key,value in d.items():
    print(key,value)