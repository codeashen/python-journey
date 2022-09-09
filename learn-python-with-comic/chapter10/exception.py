print("################ 除以零异常 ################")
i = input('请输入数字')
n = 8888
result = n / int(i)
print("{} / {} = {}".format(n, i, result))


print("################ 处理异常 ################")
try:
    i = input('请输入数字')
    n = 8888
    result = n / int(i)
    print("{} / {} = {}".format(n, i, result))
except:     # 不指定异常类型，捕获所有异常
    print("出现了异常")

print("################ 捕获指定异常 ################")
try:
    i = input('请输入数字')
    n = 8888
    result = n / int(i)
    print("{} / {} = {}".format(n, i, result))
except ZeroDivisionError as e:   # 指定异常类型
    print("出现除零异常，异常：{}".format(e))  # 出现了异常，异常：division by zero

print("################ 捕获多重异常 ################")
try:
    i = input('请输入数字')
    n = 8888
    result = n / int(i)
    print("{} / {} = {}".format(n, i, result))
except ZeroDivisionError as e:
    print("出现除零异常，异常：{}".format(e))
except ValueError as e:
    print("出现数值异常，异常：{}".format(e))

try:
    i = input('请输入数字')
    n = 8888
    result = n / int(i)
    print("{} / {} = {}".format(n, i, result))
except (ZeroDivisionError, ValueError) as e:
    print("出现异常，异常：{}".format(e))

print("################ finally释放资源 ################")
try:
    i = input('请输入数字')
    n = 8888
    result = n / int(i)
    print("{} / {} = {}".format(n, i, result))
except (ZeroDivisionError, ValueError) as e:
    print("出现异常，异常：{}".format(e))
finally:
    print("释放资源")

print("################ 自定义异常 ################")
# 自定义异常继承 Exception 类或其子类
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

# 抛出异常
raise MyException("抛出自定义异常")