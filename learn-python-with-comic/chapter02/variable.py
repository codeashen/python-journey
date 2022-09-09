# 导入模块，通过 模块名.变量名 访问
import module
# 导入模块中的变量，可直接访问，不需要前缀
from module import x2
# 导入模块中的变量并起别名，可防止变量名冲突
from module import y as y3

greeting = 'HelloWorld'
student_score = 0.0
y = 20
y = True
a = b = c = 20

print(greeting)
print(student_score)
print(y)

print(module.x1)
print(x2)
print(y3)