try:
    num = eval(input("请输入一个整数:"))
    num1 = eval(input("请输入一个整数:"))
    result = num / num1
    print(result)
except ZeroDivisionError:
    print('除数为0')
