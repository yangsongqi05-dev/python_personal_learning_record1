#大小写转换
from os import lstat

s1='HelloWorld'
s2=s1.lower()
print(s1,s2)

s3=s1.upper()
print(s3,s1)

#字符串的分割
e_mail=('lzx@123.com')
lst=e_mail.split('@')
print('邮箱名：',lst[0],'邮箱服务器域名：',lst[1])

#
print(s1.count('o'))#o出现的次数

#检索操作
print(s1.find('o'))#左边o首次出现的位置
print(s1.rfind('o'))#右边
print(s1.find('p'))#-1 木有找到
#.index和find作用一样

#判断前缀和后缀
print('demo.py'.endswith('py'))#true
print(s1.startswith('H'))#前缀
