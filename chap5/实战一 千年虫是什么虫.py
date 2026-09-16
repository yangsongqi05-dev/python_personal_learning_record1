lst=[88,89,90,98,00,99]#表示员工的出生年份
print(lst)
#遍历列表的方式
# for index in range(len(lst)):
#     if str(lst[index])!=0:
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
# print('修改后的年份：',lst)

for index,value in enumerate(lst):
    num = value
    if num < 10:
        lst[index]='200'+str(num)
    else:
        lst[index]='19'+str(num)
print('修改后的年份：',lst)