#使用+进行拼接
s1='hello'
s2='world'
print(s1+s2)

#使用字符串join()方法
print(''.join([s1,s2]))
print('*'.join([s1,s2]))
print('你好'.join(['hello','world','python']))

#直接拼接
print('hello''world')

#格式化字符串
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))