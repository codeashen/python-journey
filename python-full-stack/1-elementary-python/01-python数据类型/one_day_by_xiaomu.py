# coding: utf-8

'''
   小慕早上8点起床，起床之后就开始洗漱
   洗漱完成之后，是8点30分，于是开始吃早饭，早饭有面包，牛奶，还有麦片
   吃完早饭， 上午9点整， 小慕同学开始学习， 他走向自己的书柜， 书柜里有很多书：
     高等数学， 历史，python入门
   小慕拿了python入门的书，开始学习， 一直到12点。
   在12点时候，小慕叫了外卖， 但是到了12点半， 外卖依然没有来。
   于是 小慕给外卖小哥打了电话，电话号码是：
     123456789
   小哥说他有些繁忙，可能要在12点55的时候送达，并请小慕原谅， 他会尽快送到
   到了12点55的时候，外卖小哥准时送达了。
   小慕的午餐是： 西红柿炒鸡蛋盖饭， 价格是 12.5 ，小慕支付了费用后，开始吃饭
   吃过午饭，已经是下午1点25分了，小慕决定不学习了，而是去超市购物。
   于是，小慕来到一家超市，超市里有不同的柜台，放置着不同的内容：
     零食的柜台：
         薯片， 锅巴， 饼干
     生活的柜台：
         洗发水， 香皂， 沐浴乳， 其中洗发水有三款， abc， 价格分别是5，10，15
     水果的柜台：
         苹果，香蕉， 哈密瓜， 橘子， 西瓜
     蔬菜的柜台：
         西红柿， 黄瓜， 韭菜， 大白菜
     饮料的柜台：
         雪碧， 可乐， 矿泉水
   小慕买了 1瓶可乐， 1袋薯片， 两个苹果， 1颗大白菜， 他们的价格分别是：
     2.5， 4， 1.2, 0.9
   小慕还选了 一个洗发水， 并且选择了最贵的一款，放到自己的购物车中
   小慕来到收银台， 收银员计算一下总价 ？
   小慕将这些东西带回家， 然后就去健身了， 在健身之前， 他量了一下体重， 是44.78公斤，
   经过2.5 个小时的锻炼之后， 再来一称， 是 44.76， 小慕很开心， 看来锻炼身体对减肥
   是有帮助的。
   回到家， 已经是下午5点了， 小慕洗了个澡， 拿起可乐 和 一个苹果， 看起了电视，
   一直到很晚...
'''

username = '小慕'
get_up_time = '8:00'
bf_time = '8:30'  # 早餐时间
bf_contents = ['牛奶', '面包', '麦片']
study_time = '9:00'
books = ('高等数学', '历史', 'python入门')
study_book = 'python入门'
ready_lunch_time = '12:00'
brother_phone = 123456789
real_lunch_time = '12:55'
lunch_pay = 12.5
lunch_name = '西红柿鸡蛋盖饭'
shopping_time = '1:25'

shop = {
    'snacks': ['薯片', '锅巴', '饼干'],
    'live': ['洗发水', '香皂', '沐浴乳'],
    'fruits': [
        '苹果', '香蕉',
        '哈密瓜', '橘子',
        '西瓜'
    ],
    'vegetables': ['西红柿', '黄瓜', '韭菜', '大白菜'],
    'drinks': ['雪碧', '可乐', '矿泉水']
}
a, b, c = 5, 10, 15
cola_pay = 2.5
potato = 4
apple_two = 1.2
cabbage = 0.9

tot = cola_pay + potato + apple_two + cabbage + c
sport_time = 2.5
before_weight = 44.78
after_weight = 44.76
go_backhome_time = '5:00'

if __name__ == '__main__':
    print('我们的主人公是:', username)
    print('他是', get_up_time, '起床')
    print(bf_time, '吃早餐')
    print('早餐都有：', bf_contents)
    print(study_time, '开始学习')
    print('书架上都有：', books)
    print(username, '看的书是', study_book)
    print(username, '准备', ready_lunch_time, '吃午饭')
    print('外卖小哥的电话是:', brother_phone)
    print(username, '在', real_lunch_time, '开始吃饭')
    print('他吃的是', lunch_name, '并且价格是', lunch_pay)
    print('购物的时间是', shopping_time)
    print('超市的柜台里有：', shop)
    print(username, '共花费', tot, '元')
    print('去健身了')
    print('健身之前，体重是', before_weight)
    print('经过了', sport_time, '时间的锻炼')
    print('体重变成了', after_weight)
    print(username, '在', go_backhome_time, '回家了')
