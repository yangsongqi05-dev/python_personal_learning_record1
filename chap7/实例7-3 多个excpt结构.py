try:
    num = eval(input("请输入一个整数:"))
    num1 = eval(input("请输入一个整数:"))
    result = num / num1
    print(result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能将字符串转为数字')
except BaseException:
    print('未知异常')

