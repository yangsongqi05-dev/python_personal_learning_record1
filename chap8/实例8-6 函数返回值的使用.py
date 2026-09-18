#函数的返回值
def calc(a,b):
    print(a+b)

calc(1,2)
print(calc(1,2))#None

def calc2(a,b):
    s=a+b
    return s #将s返回函数调用处处理
get_s=calc2(1,2)
print(get_s)
get_s2=calc2(calc2(1,2),3)
print(get_s2)

#返回值可以是多个
def get_num(num):
    s=0#累加和
    j=0#奇数合
    o=0#偶数和
    for i in range(1,num+1):
        if i%2==0:
            o+=i
        else:
            j+=i
        s+=i
    return s,j,o#3个值
result=get_num(10)
print(result)
#解包赋值
a,b,c=result
print(a)
print(b)
print(c)
