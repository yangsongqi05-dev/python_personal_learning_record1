#（1）sorted排序


lst=[10,50,65,84,62]
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表：',lst)
print('升序：',asc_lst)
print('降序：',desc_lst)

#（2）reversed 反向
new_lst=(reversed(lst))
print(type(new_lst))#<class 'list_reverseiterator'>迭代器对象需要转换才能看见
print(list(new_lst))

#（3）zip
x=['a','b','c','d']
y=[10,20,33,40,50]
zipobj=zip(x,y)
print(type(zipobj))
# print(list(zipobj))

#(4)enumerate
enu=enumerate(y,start=1)
print(type(enu))
print(tuple(enu))

#(5)all 查看所有布尔类型 一个为false所有为false
lst2=[10,20,'']
print(all(lst2))#False

#(6)any 一个为ture所有为ture
print(any(lst2))

#next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))

def fun(num):
    return num%2==1

obj=filter(fun,range(10))#将0-9数字执行一次fun操作
print(list(obj))

def upper(x):
    return x.upper()

new_lst=['hello','world','python']
obj2=map(upper,new_lst)
print(list(obj2))


