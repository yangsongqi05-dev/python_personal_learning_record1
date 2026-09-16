#创建一个空列表，用于存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)
#输出所有商品信息
for item in lst:
    print(item)

#创建一个空列表，用于存储购物车中的商品
cart=[]
while True:
    flag=False#代表没有商品的情况
    num=input('请输入要购买的商品编号：')
    #遍历商品列表，查询一下要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:#切片操作，从商品中切出序列号
            flag=True#代表商品已找到
            cart.append(item)
            print('商品已添加到购物车中')
            break
    if not flag and num!='q':
        print('商品不存在')

    if num=='q':
        break
print('-'*50)
print('你的购物车的商品为：')
cart.reverse()
for item in cart:
    print(item)