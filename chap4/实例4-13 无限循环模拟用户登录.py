#（1）初始化变量
i=0
while i<3:#(2)条件判断
    #（3）语句块
    user_name=input('请输入你的用户名：')
    pwd=input('请输入你的密码：')
    #登录操作，if。。。。else
    if user_name=='lzx' and pwd=='000000':
        print('登录成功，请稍后')
        #需要改变变量，退出循环
        #（4）改变变量
        i=8
    else:
      if i<2:
        print('用户名或密码不正确，你还有',2-i,'次机会')
    i+=1#改变变量
#单分支判断
if i==3:
    print('对不起，三次均错误请24小时后重试')

