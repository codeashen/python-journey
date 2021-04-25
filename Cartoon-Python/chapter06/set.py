# 创建集合
# 1. 使用 {}
set1 = {1, 3, True, 'hello'}
# 2. 使用 set(iterable)
set2 = set([1, 2, 3])
set3 = set("hello")

type(set1)      # <class 'set'>

# 添加元素，已存在不添加不抛错
set1.add(9)

# 删除元素，不存在抛错
set1.remove(True)
# set1.remove(False)  # 抛错

# 清除集合
set1.clear()
print(set1)         # set()