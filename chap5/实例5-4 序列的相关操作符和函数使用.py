s='helloworld'
print('e在helloword中存在吗？',('e'in s))
print('v在helloword中存在吗？',('v'in s))

#not in使用
print('e在helloword中不存在吗？',('e'not in s))
print('v在helloword中不存在吗？',('v'not in s))

#内置函数使用
print('len()',len(s))
print('max()',max(s))
print('min()',min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index():',s.index('o'))#o在s中第一次出现的索引位置
print('s.count():',s.count('o'))#统计o在字符串中出现的次数
