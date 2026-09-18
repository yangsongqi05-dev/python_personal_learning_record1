def fun(*para):
    print(type(para))
    for item in para:
        print(item)


fun(1,2,3)
fun(10)
fun([11,22])#实际上传了一个参数
#在调用时，参数加一颗心，分别将列表进行解包
fun(*[10,20,30])

#个数可变的关键字操作
def fun2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, '----',value)

#调用
fun2(name='John', age=22,height=170)
d={'name':'lzx','age':22,'height':110}
fun2(**d)#**解包