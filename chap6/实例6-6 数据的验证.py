#isdigit()只能识别十进制的阿拉伯数字
print('123'.isdigit())#ture
print('一二三'.isdigit())#false
print('0b1010'.isdigit())#false
print('-'*50)
#所有字符都是数字
print('123'.isnumeric())#ture
print('一二三'.isnumeric())#ture
print('0b1010'.isnumeric())#false
print('-'*50)

#所有的字符都是字母（包含中文字符）
print('hello你好'.isalpha())#ture
print('hello你好123'.isalpha())#fales
print('hello你好一二三'.isalpha())#ture

print('-'*50)

#所有的字符都是字母或数字
print('hello你好'.isalnum())#ture
print('hello你好123'.isalnum())#ture
print('hello你好一二三'.isalnum())#ture

print('-'*50)

#所有的字符大小写
print('HelloWorld'.islower())#False
print('HelloWorld'.isupper())#false
print('helloworld你好'.islower())#false

print('-'*50)

#所有的字符都是首字母大写
print('HelloWorld'.istitle())#False W也大写了
print('Helloworld'.istitle())#ture

print('-'*50)
#判断是否是空白字符
print(' '.isspace())#ture
print('\t'.isspace())#ture
print('\n'.isspace())#ture
