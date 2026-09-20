import random

def get_max(lst):
    x=lst[0]#x存出的是元素最大值
    for i in range(1,len(lst)):
        if lst[i]>x:
            x=lst[i]
    return x
lst = [random.randint(1,100) for item in range(1,11)]
print(lst)
max_num=get_max(lst)
print(max_num)
#用max
lst = [random.randint(1,100) for i in range(1,11)]
print(lst)
def get_max2(lis):
    return max(lis)
res=get_max2(lst)
print(res)
