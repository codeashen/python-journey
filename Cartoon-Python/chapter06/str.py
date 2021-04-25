# 序列，包含列表、字符串、元组、字节序列等

# 字符串序列
s1 = 'abcde'
print(s1[0])                   # a，索引处元素
print(s1[-1])                  # e，负值索引，表示倒数第n个元素
print(s1 + ',' + ' World')     # abcde, World 字符串拼接

# 字符串切片操作 str[start:end:step]
print(s1[1:3])                 # bc，[1,3)元素，步长默认1
print(s1[:3])                  # abc，等同str[0:3]
print(s1[0:])                  # abcde，等同str[0:5]
print(s1[:])                   # abcde，等同str[0:5]
print(s1[0:-2])                # abc，使用负值索引，[0,倒数第2个)
print(s1[1:5:2])               # bd，[1,5)，步长为2
print(s1[::-1])                # edcba，步长为负数，从右往左取元素

# 成员测试
s2 = 'Hello'
'e' in s2       # True
'E' not in s2   # True

type(s2)        # <class 'str'>
