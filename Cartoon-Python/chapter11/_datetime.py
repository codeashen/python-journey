import datetime

# datetime模块包含的类
# datetime  包含时间和日期
# date      只包含日期
# time      只包含时间
# tzinfo    时区信息

################ datetime ################
# 参数：年 月 日 时 分 秒 毫秒 时区
dt1 = datetime.datetime(2021, 2, 2, 10, 30, 59, 10000)
dt2 = datetime.datetime.today()
dt3 = datetime.datetime.now()
# 参数：秒
dt4 = datetime.datetime.fromtimestamp(10005656526.99)


################## date ##################
d1 = datetime.date(2020, 1, 1)
d2 = datetime.date.today()
d3 = datetime.date.fromtimestamp(10005656526.99)


################## time ##################
t1 = datetime.time(10, 29, 30, 10000)


################ timedelta ################
d = datetime.date.today()
# 创建 10 天后的 timedelta 对象
delta1 = datetime.timedelta(10)
# 计算当前日期加 10 天后的日期
d += delta1
# 创建 5 周后的 timedelta 对象
delta2 = datetime.timedelta(weeks=5)
d -= delta2


################ 与字符串转换 ################
# 使用 strftime(format) 方法转换为字符串，datetime、date、time 类中都有此方法
dt = datetime.datetime.today()
dt.strftime('%Y-%m-%d %H:%M:%S')

# 使用 datetime.strptime(date_str, format) 类方法解析字符串
date_str = "2020-10-01 10:40:29"
dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
