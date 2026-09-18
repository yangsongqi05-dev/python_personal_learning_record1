#数据
lst=[
    ['01','电视机','海尔','1000'],
    ['02','电风扇','TCL','400'],
    ['03','洗衣机','老板','800']
]
print('编号\t\t名称\t\t\t品牌\t\t价格')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()#换行
#格式化操作
for item in lst:
    item[0]=f'0000{item[0]}'
    item[3]=f'￥{float(item[3]):.2f}'

print('编号\t\t名称\t\t\t品牌\t\t价格')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()#换行