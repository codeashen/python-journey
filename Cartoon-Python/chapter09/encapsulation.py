print('########################## 封装 #########################')
class Account:
    # 利率【类变量】
    __interest_rate = 0.0568

    def __init__(self, owner, amount):
        self.owner = owner      # 创建并初始化【公有实例变量】 owner
        self.__amount = amount  # 创建并初始化【私有实例变量】 __amount

    # 【私有方法】
    def __get_info(self):
        return "{0} 金额: {1}, 利率: {2}".format(self.owner,
                                             self.__amount,
                                             Account.__interest_rate)

    # 实例方法
    def desc(self):
        print(self.__get_info())    # 内部调用私有方法

    # 【get方法】
    def get_amount(self):
        return self.__amount

    # 【set方法】
    def set_amount(self, amount):
        self.__amount = amount


################# 属性(property) #################
class Dog:

    def __init__(self, name, age, sex='female'):
        self.name = name
        self.__age = age    # 私有变量 __age 对应的属性名 age

    @property
    def age(self):          # 代替 get_age(self)
        return self.__age

    @age.setter
    def age(self, age):     # 代替 set_age(self, age)
        self.__age = age

dog = Dog('球球', 2)
print('狗狗的年龄: {}'.format(dog.age))      # 通过属性访问私有变量
dog.age = 3     # set_age(3)
print('修改后的狗狗年龄: {}'.format(dog.age))
