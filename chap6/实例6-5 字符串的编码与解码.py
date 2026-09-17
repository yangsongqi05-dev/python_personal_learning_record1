s='伟大的中国梦'
#编码 str-->bytes
scode=s.encode(errors='replace')#默认是utf-8，中文占3个字符
print(scode)

scode=s.encode('gbk', errors='replace')
print(scode)

#编码中出错的问题
s2='耶✌'
scode1=s2.encode('gbk',errors='replace')
print(scode1)

#解码的过程
print(bytes.decode(scode,'gbk'))