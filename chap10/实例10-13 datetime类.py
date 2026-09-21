from datetime import datetime#从datetime模块中，导入datetime类
dt=datetime.now()
print('当前的系统时间：',dt)
#datetime是一个类，手动创建这个类的对象
dt2=datetime(2028,8,8,10,8)
print('dt的数据类型',type(dt2),'dt2所表示的日期时间：',dt2)
print('年',dt2.year,'月',dt2.month,'日',dt2.day)
print('时',dt2.hour,'分',dt2.minute,'秒',dt2.second)

#比较两个datetime类型的对象大小
labor_day=datetime(2028,4,1,0,0,0)
national_day=datetime(2028,10,1,0,0,0)
print('2028年4月1日比10月1日早吗：',labor_day<national_day)

#datetime也可以和字符串进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y/%m/%d')
print(nowdt_str)

#字符串类型转为datetime
str_datetime='2028年8月8日 20点8分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print(dt3)