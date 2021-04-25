print('########################## 创建对象 #########################')
class Car(object):
    pass    # pass 用于需要编写代码又不马上编写，保证程序不报错的占位语句

car = Car()

print('########################## 类的成员 #########################')
#                       类的成员
#          ┌─────────┬─────┴────┬───────────┐
#       成员变量    构造方法    成员方法    属性(property)
#      ┌───┴───┐            ┌───┴───┐
#   实例变量   类变量      实例方法   类方法

class Dog:

    # 类变量
    category = '犬类'

    # 构造方法
    def __init__(self, name, age, sex='female'):
        self.name = name        # 创建和初始化实例变量 name
        self.age = age          # 创建和初始化实例变量 age
        self.sex = sex          # 创建和初始化实例变量 sex

    # 类方法
    @classmethod
    def look(cls, house):
        print('狗会看家, 可以看护{}'.format(house))

    # 实例方法
    def run(self):
        print('{}在跑'.format(self.name))

    # 实例方法
    def eat(self, food):
        print('{}在吃{}'.format(self.name, food))

# 通过类访问类方法
Dog.look('别墅')

# 通过对象访问实例方法
bai = Dog('小白', 3)
bai.run()
bai.eat('肉')


print('########################## 封装 #########################')
