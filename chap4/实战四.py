import random
rand=random.randint(1,100)
count=1#记录猜数的次数
while count<=10:
    number=eval(input('在我心中有个数请你猜一猜：'))
    if number==rand:
        print('猜对了')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    count=count+1
#判断次数
if count<=3:
    print('真聪明')
elif count<=6:
    print('还行，一共猜了',count,'次')
elif count<=9:
    print('笨死了，一共猜了',count,'次')
