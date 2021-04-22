a = 10
b = 3

# 算数运算符
r1 = -a
r2 = a + b
r3 = a - b
r4 = a * b
r5 = a / b      # 3.3333333333333335, 不同于Java
r6 = a % b      # 1
r7 = a ** b     # a^b = 1000, a的b次幂
r8 = a // b     # 3, 等同 Java 的 /

# 逻辑运算符
t = True
f = False
b1 = t and f
b2 = t or f

# 位运算符
x = 0b10110010  # 178
y = 0b01011110  # 94
print("~x = %s" % ~x)           # -179, 位反, ~x = -(x+1)
print("x & y = %s" % (x & y))   # 18, 位与
print("x | y = %s" % (x | y))   # 254, 位或
print("x ^ y = %s" % (x ^ y))   # 236, 位异或
print("x >> 1 = %s" % (x >> 1)) # 89, 右移, x >> n = x / 2^n
print("x << 1 = %s" % (x << 1)) # 356, 左移, x << n = x * 2^n

# 赋值运算符
a = b
a += b
a -= b
a *= b
a /= b
a %= b
a **= b
a //= b
a &= b
a |= b
a ^= b
a <<= b
a >>= b
