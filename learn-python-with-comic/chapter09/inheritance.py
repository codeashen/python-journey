# 定义父类 Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "动物的名字: {}".format(self.name)

    def move(self):
        print("动一动...")

# 定义子类 Cat
class Cat(Animal):
    def __init__(self, name, age):
        # 调用父类的构造方法，初始化父类成员变量
        super().__init__(name)
        self.age = age

cat = Cat('Tom', 2)
cat.move()
print(cat.show_info())


print("################ 多继承 ################")
# Python 支持多继承
# Python 类的多个父类中有相同的成员方法或成员变量，优先继承写在左边的

# 马类
class Horse:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "马的名字: {}".format(self.name)

    def run(self):
        print("马跑")

# 驴类
class Donkey:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return "驴的名字: {}".format(self.name)

    def run(self):
        print("驴跑")

    def roll(self):
        print("驴打滚")

# 骡子类，继承马和驴类
class Mule(Horse, Donkey):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # 重写父类方法
    def show_info(self):
        return "骡: {}, {}岁".format(self.name, self.age)

m = Mule('骡宝', 1)
m.run()                 # 马跑
m.roll()                # 驴打滚
print(m.show_info())    # 骡: 骡宝, 1岁