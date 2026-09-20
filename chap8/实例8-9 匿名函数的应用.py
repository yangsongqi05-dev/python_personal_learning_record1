

def calc(a,b):
    return a+b
print(calc(1,2))
print('-'*30)
#匿名函数
s=lambda a,b:a+b#s表示一个匿名函数
print(type(s))#<class 'function'>函数的意思
#调用匿名函数
print(s(10,20))
print('-'*30)
#列表的正常取值操作
lst=[10,20,30,40]
for i in range(0,len(lst)):
    print(lst[i])
print()
print('-'*30)
for i in range(0,len(lst)):
    result=lambda x:x[i]
    print(result(lst))

student_scores=[
    {'name':'罗志祥','score':90},
    {'name':'张三','score':60},
    {'name':'李四','score':50}
]
#对列表进行排序，按字典中的成绩去排
student_scores.sort(key=lambda x:x['score'],reverse=True)
print(student_scores)