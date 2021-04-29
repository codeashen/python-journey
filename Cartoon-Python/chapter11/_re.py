import re

# 邮箱验证正则表达式
p = r'\w+@qq\.com'
email1 = 'tony@qq.com'
m1 = re.match(p, email1)
type(m1)        # <class 're.Match'>
print(m1)       # <re.Match object; span=(0, 11), match='tony@qq.com'

# 字符串查找
text = "Tony's email is tony@qq.com"
m2 = re.search(p, text)
print(m2)       # <re.Match object; span=(16, 27), match='tony@qq.com'>

p = r'Java|java|JAVA'
text = 'I like java and Java and JAVA'
m3 = re.findall(p, text)
print(m3)       # ['java', 'Java', 'JAVA']


# 字符串替换
p = r'\d+'
text = 'AB1CDE34FGH'
replace_text = re.sub(p, '_', text)
print(replace_text)     # AB_CDE_FGH
replace_text = re.sub(p, '_', text, count=1)
print(replace_text)     # AB_CDE34FGH


# 字符串分割
p = r'\d+'
text = 'AB1CDE34FGH'
clist = re.split(p, text)
print(clist)        # ['AB', 'CDE', 'FGH']
clist = re.split(p, text, maxsplit=1)
print(clist)        # ['AB', 'CDE34FGH']
