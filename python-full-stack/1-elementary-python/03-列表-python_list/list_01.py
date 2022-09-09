# coding:utf-8

names = ('dewei', 'xiaomu', 'xiaowang')

names_add = names + names
names_c = names * 10

print(names_add)
print(names_c)
print('names_c length is', len(names_c))

names += ('abc',)
print(names)
names *= 10
print(names)

names_list = ['dewei', 'xiaomu']
names_list += ['xiaowang']
print(names_list)
names_list *= 5
print(names_list)

print('dewei' in names_list)
print('dewei' not in names_list)
