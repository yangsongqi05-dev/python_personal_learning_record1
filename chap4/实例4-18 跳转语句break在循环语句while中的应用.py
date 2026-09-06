s=0#存储累加和
i=1#（1）初始化变量
while i<11:#(2)条件判段
    s+=i
    if s>20:
       print('累加和大与20的当前的数是',i)
       break
    i=i+1#(4)改编遍历
print('--------------------------')
i=0#（1）初始化变量
while i<3:#（条件判断）
    user_name=input('请输入用户名：')
    password=input('请输入密码：')
    if user_name=='lzx' and password=='000000':
        print('登录成功！')
        break
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
    i+=1
else:
    print("三次均输入错误")


