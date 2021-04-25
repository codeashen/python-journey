# 创建列表
# 1. 方括号创建列表
l1 = []                     # 空列表
l2 = [20, 'Hello', False]   # 混合类型列表
# 2. 通过 list(iterable) 函数创建列表，参数iterable是可迭代对象（字符串、列表、元组、集合、字典等）
l3 = list("Hi")
print(l3)                   # ['H', 'i']

type(l1)            # <class 'list'>

# 追加元素
l1.append(80)       # [80]
l1 += l2            # [80, 20, 'Hello', False]
l1.extend(l3)       # [80, 20, 'Hello', False, 'H', 'i']
# 注：上面 list(iterable) 叫函数，append(x) 和 extend(x) 叫方法，方法属于对象，函数可直接调用不属于对象

# 插入元素
l0 = [0, 1, 2, 0]
l0.insert(1, 'X')   # 在索引 1 位置插入元素 'X'
print(l0)           # [0, 'X', 1, 2, 0]

# 替换元素
l0[1] = 'Y'
print(l0)           # [0, 'Y', 1, 2, 0]

# 删除元素
l0.remove(0)        # 删除匹配的第一个元素
print(l0)           # ['Y', 1, 2, 0]


