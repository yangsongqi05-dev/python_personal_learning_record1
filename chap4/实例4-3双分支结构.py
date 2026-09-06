number=eval(input('请输入你的6位中奖号码：'))
if number==123445:
    print('恭喜你中奖了')
else:
    print('未中奖')

print('---以上代码可以使用条件表达式进行简化---')
result='恭喜你中奖了' if number==123445 else'未中奖'
print(result)
