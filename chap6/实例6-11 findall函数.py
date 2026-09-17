import re
pattren='\d\.\d+'#\d数字，\.小数，\d+一个或多个数字
s='I study python3.11 every day python2.7 I love you'
lst=re.findall(pattren,s)
print(lst)