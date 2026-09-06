for i in 'hello':
    if i == 'e':
        break
    print(i)
print('----------------------------------')
for i in range(3):
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_name == 'lzx' and password == '000000':
        print('登录成功！')
        break
    else:
        if i < 2:
            print('用户名或密码不正确，你还有', 2 - i, '次机会')
else:
    print('三次均错误')