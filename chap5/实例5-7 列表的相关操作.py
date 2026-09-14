lst=['hello','world','python']
print('原列表：',lst)
# 增加元素的操作
lst.append('sql')
print('增加元素后：',lst)
# 使用insert（index，x）在指定index位置上插入元素x
lst.insert(1,100)
print(lst)

#列表元素删除
lst.remove('world')
print('删除元素之后的列表',lst)
#使用pop（index）根据索引将元素取出再删除
print(lst.pop(1))
print(lst)

#清除列表所以元素clear()
# lst.clear()
# print(lst)

#列表的逆向输出
lst.reverse()
print(lst)
#列表的拷贝，将生成一个新的列表对象
new_lst=lst.copy()
print(new_lst)

#列表元素的修改
lst[1]='mysql'
print(lst)