# coding:utf-8

old_list = ['python', 'django', 'flask']

new_list = old_list
new_list.append('tornado')

print(new_list)
print(old_list)
print(id(new_list), id(old_list))

old_list.remove('tornado')
print(new_list, old_list)

del new_list
print(old_list)

old_list_copy = ['python', 'django', 'flask']
new_list_copy = old_list_copy.copy()

print(old_list_copy, new_list_copy)
new_list_copy.append('tornado_copy')
print(old_list_copy, new_list_copy)
print(id(old_list_copy), id(new_list_copy))
