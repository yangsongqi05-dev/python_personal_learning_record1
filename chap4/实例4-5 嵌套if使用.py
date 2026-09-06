answer=input('请问，你喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入酒精含量'))
    if proof<20:
        print('滚')
    elif proof<80:
        print('你着了')
    else:
        print('蹲起！')
else:
    print('滚')