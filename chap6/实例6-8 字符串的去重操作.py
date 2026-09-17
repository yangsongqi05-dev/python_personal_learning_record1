s='helloawawlloocddd'
#(1)字符串的拼接及not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item#拼接操作
print(new_s)
#（2）使用索引+not in
new_2=''
for i in range(len(s)):
    if s[i] not in new_2:
        new_2+=s[i]
print(new_2)

#(3)通过集合去重+列表排序
nwe_s3=set(s)
lst=list(nwe_s3)
lst.sort(key=s.index)
print(''.join(lst))