#正向递增
from idlelib.pyshell import PyShell

s='helloword'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print("\n------------")

#反向索引
for i in range(-9,0):
    print(i,s[i],end='\t\t')

