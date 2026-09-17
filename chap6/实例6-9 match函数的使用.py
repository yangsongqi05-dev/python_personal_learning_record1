import re#导入
from idlelib.parenmatch import ParenMatch
from typing import Match

pattren='\d\.\d+'#\d数字，\.小数，\d+一个或多个数字
s='I study python every day'#待匹配字符串
match=re.match(pattren,s,re.I)
print(match)#None
s2='3.11python I study python every day'
match2=re.match(pattren,s2)
print(match2)
#<re.Match object; span=(0, 4), match='3.11'>

print('匹配值的起始位置：',match2.start())
print('匹配值的结束位置：',match2.end())
print('匹配值的位置元素：',match2.span())
print('待匹配的字符串：',match2.string)
print('匹配的数据：',match2.group())