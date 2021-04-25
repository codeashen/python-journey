# 字符串有单引号，用双引号包
s1 = "'Python' is good"
# 字符串有双引号，用单引号包
s2 = '"Python" is good'

# 转义
s3 = 'I like \'Python\'.\n I like study.'
# 原始字符串
s4 = r'this \\ is a character: \n'
print(s4)  # this \\ is a character: \n
# 长字符串，三个单引号，或三个双引号
s5 = '''
       静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
'''
print(s5)

# 字符串转数字
i1 = int('50')
f1 = float('95.5')
# 数字转字符串
str(95.5)
str(True)

# 格式化字符串
# 占位符
i = 32
s6 = '{} * {} = {}'.format(i, i, i * i)             # 默认占位符
s7 = '{0} * {0} = {1}'.format(i, i * i)             # 参数序号占位符
s8 = '{p1} * {p1} = {p2}'.format(p1=i, p2=i * i)    # 参数名占位符
# 格式化控制符，{参数序号:格式控制符} 或 {参数名:格式控制符}
money = 5834.5678
name = 'Tony'
s9 = '{0:s}年龄{1:d}，工资是{2:f}'.format(name, 20, money)
# 格式控制符说明
# s-字符串， d-十进制整数，f、F-十进制浮点数，f、G-十进制整数或浮点数，e、E-科学计数法表示浮点数，o-八进制整数，x、X-十六进制整数


# 查找字符串
s10 = "Hello World"
i1 = s10.find('l')              # 2
i2 = s10.find('l', 4)           # 9，从 4 开始找
i3 = s10.find('l', 8, 9)        # -1, [8, 9) 内查找

# 字符串替换
text = 'AB CD EF GH'
text1 = text.replace(' ', '|', 2)   # AB|CD|EF GH
text2 = text.replace(' ', '|')      # AB|CD|EF|GH

# 字符串分割
list1 = text.split(' ')             # ['AB', 'CD', 'EF', 'GH']
list2 = text.split(' ', 2)          # ['AB', 'CD', 'EF GH']
