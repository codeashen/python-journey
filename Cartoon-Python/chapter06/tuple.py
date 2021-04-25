# 创建元组
# 1. 通过 () 创建
t1 = ()
t2 = (3, True, 'X')
# 2. 省略小括号创建元组
t3 = 1,                 # (1,)
t4 = 1, 2, 3, 'X'       # (1, 2, 3, 'X')
# 3. 通过 tuple(iterable) 创建
t5 = tuple('via')       # ('v', 'i', 'a')
t6 = tuple([1, 2])      # (1, 2)

type(t1)                # <class 'tuple'>

# 元组拆包
# 个数必须对应，类似于es6解构赋值
a, b = t6
print('a = %d, b = %d' % (a, b))      # a = 1, b = 2
x, y = (3, 5)
print('x = %d, y = %d' % (x, y))      # x = 3, y = 5

