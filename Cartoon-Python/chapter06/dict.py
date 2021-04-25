# 创建字典
# 1. 直接创建 {k1: v2, k2: v2}
d1 = {101: '张三', 102: '李四'}
# 2. 使用 dict()
d2 = dict({101: '张三', 102: '李四'})           # 参数：另一个字典
d3 = dict(((101, '张三'), (102, '李四')))       # 参数：二维元组
d4 = dict(zip([101, 102], ['张三', '李四']))    # 参数：zip
# 以上创建了4个相同的字典，{101: '张三', 102: '李四'}

# 查询字典
name = d1[101]
# 替换指定 key 的value
d1[101] = '王五'
# 若 key 不存在，添加 键值对
d1[103] = '赵六'
# 移除指定 key 的键值对，返回对应的 value, 不存在抛错
d1.pop(101)

# 返回键值对视图
items1 = d1.items()
print(items1)           # dict_items([(102, '李四'), (103, '赵六')])
item_list = list(items1)
print(item_list)        # [(102, '李四'), (103, '赵六')]

# 返回键视图
keys1 = d1.keys()
print(keys1)            # dict_keys([102, 103])
key_list = list(keys1)
print(key_list)         # [102, 103]

# 返回值视图
values1 = d1.values()
print(values1)          # dict_values(['李四', '赵六'])
value_list = list(values1)
print(value_list)       # ['李四', '赵六']


# 遍历字典
print('------ 键遍历 ------')
for s_id in d1.keys():
    print('学号: ' + str(s_id) + ', 姓名: ' + d1[s_id])

print('------ 值遍历 ------')
for s_name in d1.values():
    print('姓名: ' + s_name)

print('------ 键值对遍历 ------')
for s_id, s_name in d1.items():
    print('学号: ' + str(s_id) + ', 姓名: ' + s_name)
