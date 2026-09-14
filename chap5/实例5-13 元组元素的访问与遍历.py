t=('hello','world','python')
#根据索引访问
print(t[0])
t2=t[0:3:2]#支持切片操作
print(t2)

#元组遍历
for item in t:
    print(item)

#for+range+len
for i in range(len(t)):
    print(i,t[i])

#使用enumerate
for index,item in enumerate(t):
    print(index,item)

for index,item in enumerate(t,start=11):
    print(index,item)