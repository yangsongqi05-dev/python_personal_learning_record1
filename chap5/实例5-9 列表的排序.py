lst=[2,434,56,3]
print('原列表：',lst)
#排序
asc_lst=sorted(lst)
print('升序：',asc_lst)
print('原列表：',lst)

#降序
desc_lst=sorted(lst,reverse=True)
print('降序：',desc_lst)
print('原列表：',lst)

lst2=['apple','Son','banana','orange']
print('原列表',lst2)

#忽略大小进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表',lst2)
print('排序后的列表',new_lst2)