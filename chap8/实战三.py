def change_case(s):
    new_str=''
    for char in s:
        if char.isupper():
            new_str+=char.lower()
        elif char.islower():
            new_str+=char.upper()
        else:
            new_str+=char
    return new_str
text=input('请输入一个字符串：')
result=change_case(text)
print(result)
