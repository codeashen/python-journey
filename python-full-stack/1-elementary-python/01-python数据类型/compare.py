# coding:utf-8

a = 1
b = 2.2
c = 0
d = 18
d_01 = 18
e = -3
f = 300
f_01 = 300

print(a == b)
print(a != b)
print(a < b)
print(a > e)
print(d >= b)
print(d >= d_01)

print(d == d_01)
print(d is d_01)
print('d id is:', id(d))
print('d_01 id is:', id(d_01))

print(f == f_01)
print(f is f_01)

print(f is d)
print(id(f))
print(id(d))

print(f is not d)
