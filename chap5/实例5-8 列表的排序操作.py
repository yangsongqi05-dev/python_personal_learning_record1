lst=[2,434,56,3,2]
print('原列表：',lst)
lst.sort()#排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序：',lst)

#排序，降序
lst.sort(reverse=True)
print('降序：',lst)

print('-'*20)
lst2=['apple','Son','banana','orange']
print('原列表',lst2)
lst2.sort()#先排大写在排小写
print('升序：',lst2)

#降序
lst2.sort(reverse=True)
print('降序',lst2)

#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)