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

class Account1:

    # 利率【类变量】
    interest_rate = 0.0568

    # 【构造方法】
    def __init__(self, owner, amount=0):
        self.owner = owner      # 创建和初始化实例变量 owner
        self.amount = amount    # 创建和初始化实例变量 amount

    # 计算利息【类方法】
    @classmethod
    def interest_by(cls, amt, year):
        # 可以改为 Account1.interest_rate * amt
        return cls.interest_rate * amt * year

    # 查询账户余额【实例方法】
    def query(self):
        print('{} 账户金额: {}'.format(self.owner, self.amount))

    # 存钱【实例方法】
    def save(self, amt):
        self.amount = self.amount + amt
        print("成功存入 {}, 当前金额: {}".format(amt, self.amount))

# 通过类访问类方法
print("利率为: {}".format(Account1.interest_rate))
m = Account1.interest_by(10000, 2)
print("10000元存两年利息: {}".format(m))

# 通过对象访问实例方法
bob = Account1('Bob', 10000)
bob.query()
bob.save(500)
