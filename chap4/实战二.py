#（1）初始化变量
answer='y'
#（2）条件判断
while answer=="y":
    print('--------欢迎使用10086查询功能---------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询剩余通话时长')
    print('0.退出系统')
    choice=input('请输入你要执行的操作：')
    if choice=='1':
        print('当前余额为231.1元')
    elif choice=='2':
        print('当前剩余流量为999G')
    elif choice=='3':
        print('当前剩余通话时长为200分钟')
    elif choice=='0':
        print('谢谢使用')
        break
    else:
        print('请重新输入')
    answer=input('还继续操作吗？y/n')
else:
    print('程序退出谢谢使用')