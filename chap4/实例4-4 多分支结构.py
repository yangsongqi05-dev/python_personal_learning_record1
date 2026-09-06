score=eval(input('请输入你的成绩：'))
if score<0 or score>100:
    print('成绩有误')
elif score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
elif score<50:
    print('F')