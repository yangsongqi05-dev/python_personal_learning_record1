import admin.my_admin as a#包名.模块名
a.info()
print('-'*30)
from admin import my_admin as b
b.info()
print('-'*30)
from admin.my_admin import info #导入具体的函数
info()
print('-'*30)
from admin.my_admin import *
print(name)
