
def get_digit(x):
    s=0#存储累加和
    lst=[]#存储提取出来的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    s=sum(lst)
    return lst,s

#函数调用
s=input('请输入一个字符串：')

lst,x=get_digit(s)
print('提取的数字列表：',lst)
print('累加和为：',x)