# 模块里类外（函数）；函数里（嵌套函数）；类里（方法）

print('###################### 函数定义和调用 ######################')
# 定义函数
def rect_area(width, height):
    area = width * height
    return area

# 调用函数
def print_area(width, height):
    area = rect_area(width, height)
    print("{} * {} 长方形的面积: {}".format(width, height, area))

print_area(10, 2)


print('######################### 函数参数 ########################')
# 参数默认值
def make_coffee(name='卡布奇诺'):
    return '给阿姨倒一杯{}'.format(name)

print(make_coffee())
print(make_coffee('拿铁'))


# 可变参数

# 基于元组的可变参数
def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

print(sum(10, 1.5, 20))

# 基于字典的可变参数
def show_info(**info):
    print('--------show_info--------')
    for key, value in info.items():
        print('{} - {}'.format(key, value))

show_info(name='Tony', age=18, sex=True)


print('######################### 变量作用域 ########################')
# 变量作用域
x = 20

def print_value():
    x = 10
    print('函数中 x = {}'.format(x))   # 10

print_value()
print('全局变量 x = {}'.format(x))      # 20

# 提升作用域
def print_value2():
    global x    # 将 x 变量提升为全局变量
    x = 10
    print('函数中 x = {}'.format(x))   # 10

print_value2()
print('全局变量 x = {}'.format(x))      # 10，调用 print_value2 的时候将函数中 x 提升为全局变量了


print('########################## 函数类型 #########################')
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

type(add)           # <class 'function'>
# 函数类型，函数也可以作为另一函数的参数和返回值

def calc(opr):
    if opr == '+':
        return add
    else:
        return sub

f1 = calc('+')
f2 = calc('-')
print('10 + 5 = {}'.format(f1(10, 5)))
print('10 - 5 = {}'.format(f2(10, 5)))


# 过滤函数 filter(function, iterable)
def f1(x):
    return x > 50

data1 = [60, 65, 12, 58, 14]
filtered = filter(f1, data1)    # 对 data1 进行过滤，过滤条件为 f1
data2 = list(filtered)
print(data2)                    # [60, 65, 58]

# 转换函数 map(function, iterable)
def f2(x):
    return x * 10

mapped = map(f2, data1)
data3 = list(mapped)            # 对 data1 进行转换，转换操作为 f2
print(data3)                    # [600, 650, 120, 580, 140]


print('########################## lambda #########################')
def calc2(opr):
    if opr == '+':
        return lambda a, b: (a + b)     # 使用lambda
    else:
        return lambda a, b: a - b       # 省略括号的lambda

data4 = list(filter(lambda x: x > 50, data1))
print(data4)