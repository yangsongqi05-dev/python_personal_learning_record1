#遍历字符串
for i in 'hello':
    print(i)
#range()函数，python内置函数，产生一个[n,m)的整数序列
for i in range(1,11):
    print(i)
#计算1-10之间的累加和
s=0# 用于储存累加和
for i in range(1,10):
    s+=i
print('1-10之间的累加和为:',s)
print('-----100到999直接的水仙花数------')
'''
水仙花数 153=3*3*3+5*5*5+1*1*1
'''
for i in range(100,999):
    sd=i%10#获取各位上的数
    tens=i//10%10#获取十位上的数
    hundred=i//100
    #判断
    if sd**3+tens**3+hundred**3==i:
        print(i)