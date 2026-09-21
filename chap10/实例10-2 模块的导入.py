import my_info
print(my_info.name)
my_info.info()

#模块可以改名
import my_info as a
print(a.name)
a.info()

#(2)from ...import
from my_info import name#导入的是具体变量的名称
print(name)

from my_info import info #导入的是一个函数
info()

#通配符
from my_info import *
print(name)
info()

#同时导入多个模块
import math,time,random