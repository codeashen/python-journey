# 分支语句
score = int(input("请输入一个0~100的整数："))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade = " + grade)


# 循环语句
n = int(input("请输入一个0~10的整数："))
sum = 0

while n > 0:
    if n > 10:
        print("Error number")
        break
    sum += n
    n -= 1
# else子句在循环正常结束时执行（没有被break和return打断）
else:
    print("While over, sum = %d" % sum)


print("--------字符串--------")
for item in 'Hello':
    print(item)

print("--------整数列表-------")
numbers = [42, 35, 36, 79]
for item in numbers:
    print(item)

print("--------range-------")
for item in range(10):
    if item == 3:
        continue
    if item == 5:
        break
    print(item)
else:
    print("For Over")