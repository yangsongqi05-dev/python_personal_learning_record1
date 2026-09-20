class Car():
    def __init__(self,type,num ):
        self.type = type
        self.num = num
    def start(self):
        print('我是车我能启动')
    def stop(self):
        print('我是车我能停止')

#出租车
class Taxi(Car):
    def __init__(self,type,num,company):
        super().__init__(type,num)
        self.company = company
    def start(self):
        print('乘客你好')
        print(f'我是{self.company}出租车公司，我的车牌号是：{self.num}')
    def stop(self):
        print('目的到了，请扫码付款，欢迎下次乘坐')

class Family(Car):
    def __init__(self,type,num,name):
        super().__init__(type,num)
        self.name = name
    def start(self):
        print(f'我是{self.name}，我的轿车我做主')
    def stop(self):
        print('目的地到了我们去玩吧')

#测试方法
taxi=Taxi('大众','京A8888','哈喽')
taxi.start()
taxi.stop()

print('-'*50)

family=Family('特斯拉','京B8888','武大郎')
family.start()
family.stop()

