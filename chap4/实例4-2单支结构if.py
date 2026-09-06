number=eval(input('请输入你的幸运数字'))
if number==123: #等值判断
    print('恭喜你中奖了')
if number!=123:
    print('你未中奖')
print('------以上if判断的表达式，是通过比较运算符计算的，结果是布尔值')
n=98
if n%2:# 余数是0 0的布尔值是false
    print(n,'是奇数')#余数是0代码不执行
if not n%2: #not false
    print(n,'是偶数')

print('-------判断一个字符串是否是字符串-----')
x=input('请输入字符：')
if x:#空字符串为false
    print('x是一个空字符串')
if not x:#空字符串为false取反ture
    print('x是一个非空字符串')
print('----使用if语句时，如果语句只有一句代码，可以把语句直接写在：后面')
a=10
b=5
if a>b:max=a
print('a和b的最大值',max)