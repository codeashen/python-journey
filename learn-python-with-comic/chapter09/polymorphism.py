print("################ 多态 ################")
class Animal:
    def speak(self):
        print("动物叫")

class Dog(Animal):
    def speak(self):
        print("小狗汪汪汪")

class Cat(Animal):
    def speak(self):
        print("小猫喵喵喵")

an1 = Dog()
an2 = Cat()
an1.speak()
an2.speak()


print("################ 鸭子类型测试与多态 ################")

# 定义汽车类，不继承动物类，但是有 speak 方法
class Car:
    def speak(self):
        print("小汽车嘀嘀嘀")

# 定义一个方法，接收一个具有 speak() 方法的对象
def start(obj):
    obj.speak()


start(Dog())
start(Cat())
start(Car())

# Python支持这种更加灵活的多态，支持鸭子类型测试
# 所谓鸭子类型测试：若一只鸟走起来像鸭子，游泳像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子
# 由于支持鸭子类型测试，Python解释器不检查发生多态的对象是否继承了同一个父类，
# 只要它们具有相同的行为（方法），它们之间就是多态的