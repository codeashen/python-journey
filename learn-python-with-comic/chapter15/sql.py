import sqlite3

# 操作sqlite数据库

try:
    # 1.建立数据库连接
    con = sqlite3.connect('school_db.db')
    # 2.创建游标对象
    cursor = con.cursor()
    # 3.执行sql操作
    sql = "SELECT s_id, s_name, s_sex FROM student"
    cursor.execute(sql)
    # 4.提取结果集
    result_set = cursor.fetchall()
    for row in result_set:
        print("学号：{0}，姓名：{1}，性别：{2}"
              .format(row[0], row[1], row[2]))

except sqlite3.Error as e:
    print("查询数据出错：{}".format(e))
finally:
    # 5.关闭游标
    if cursor:
        cursor.close()
    # 6.关闭数据库
    if con:
        con.close()
