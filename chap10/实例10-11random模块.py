#导入
import random
#设置随机数的种子
random.seed(10)
print(random.random())
print(random.random())
print('-'*30)
random.seed(10)
print(random.randint(1,100))

for i in range(10):
    print(random.randrange(1,10,3))

print(random.uniform(10,100))#随机小数


lst=[i for i in range(1,11)]
print(random.choice(lst))#随机取出

random.shuffle(lst)#随机排序
print(lst)