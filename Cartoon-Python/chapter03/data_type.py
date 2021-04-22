# 整数类型
i1 = 28
print(type(i1))             # <class 'int'>
i2 = 0b11100                # 二进制表示, 0B（0b）开头
i3 = 0O34                   # 八进制表示, 0O开头
i4 = 0x1c                   # 十六进制表示, 0x开头

# 浮点类型
f1 = 1.0
print(type(f1))             # <class 'float'>
f2 = 3.36e2                 # 科学计数法表示
f3 = 3.36e-2

# 复数类型
p1 = 1 + 2j                 # 实部为1，虚部为2j
p2 = (1 + 2j) + (3 - 4j)    # 复数计算
print(type(p2))             # <class 'complex'>

# 布尔类型
bool(0)                     # 整数 0 为 False, 非 0 为 True
bool('')                    # 空字符串为 False, 非空为 True
bool([])                    # 空列表为 False, 非空为 True
bool({})                    # 空字典为 False, 非空为 True

# 数字隐式类型转换
a1 = 1 + True               # 2, 布尔型 True 转换为整型 1
a2 = 1.0 + 1                # 2.0, 整数转换为浮点数
a3 = 1.0 + 1 + True         # 3.0, 整数和布尔型都转换为浮点数
a4 = 1.0 + 1 + False        # 2.0

# 数字显式类型转换
b1 = int(False)             # 0
b2 = int(True)              # 1
int(0.6)                    # 0, 浮点数转整数, 舍去小数部分
float(1)                    # 1.0
float(False)                # 0.0
float(True)                 # 1.0