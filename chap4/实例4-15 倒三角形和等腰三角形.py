#倒三角洲
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()#内层循环完毕后换行
print('-'*10)
#等腰三角形
for i in range(1,6):#5行
    #倒三角形
    for j in range(1,6-i):
        print(' ',end='')
    #1，3，5，7.。。等腰三角形
    for k in range(1,i*2):
        print('*',end='')
    print()