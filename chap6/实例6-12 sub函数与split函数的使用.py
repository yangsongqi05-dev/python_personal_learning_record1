import re
from os import lstat

pattern='黑客|破解|反爬'
s='我想学python，想反爬一些vip视频，python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://cn.bing.com/search?q=ysq&form=SWAUA2'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)