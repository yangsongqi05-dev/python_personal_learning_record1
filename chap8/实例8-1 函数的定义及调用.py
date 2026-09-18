def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}的累加和为：{s}')
#函数调用
get_sum(10)
get_sum(100)