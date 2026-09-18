
try:
    socre=eval(input('请输入你的分数：'))
    if 0<=socre<=100:
        print('分数为：',socre)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
