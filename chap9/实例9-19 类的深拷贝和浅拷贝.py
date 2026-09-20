class CPU():
    pass
class Disk():
    pass
class computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=CPU()#创建一个cpu对象
disk=Disk()#创建一个disk对象
#变量（对象）赋值
com=computer(cpu,disk)

com1=com
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com1,'子对象的内存地址：',com1.cpu,com1.disk)
print('-'*300)
#类的浅拷贝
import copy
com2=copy.copy(com)
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com2,'子对象的内存地址：',com2.cpu,com2.disk)
print('-'*300)
#类的深拷贝
com3=copy.deepcopy(com)#子对象也会重新拷贝
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com3,'子对象的内存地址：',com3.cpu,com3.disk)