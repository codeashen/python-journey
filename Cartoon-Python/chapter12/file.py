# 打开文件
f = open('file/test.txt', 'w+')  # 读写模式打开，如果不存在则创建
f.write('World')
# 文件内容：World

open('file/test.txt', 'r+')  # 读写模式打开，不存在抛异常
f.write('Hello')
# 文件内容：WorldHello

open('file/test.txt', 'a')  # a模式打开，末尾追加内容
f.write('_end')
# 文件内容：WorldHello_end


# 关闭文件
f_name = 'file/test.txt'
f = None
try:
    f = open(f_name)
    print('打开文件成功')
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print('找不到文件')
except OSError as e:
    print('系统异常')
finally:
    if f is not None:
        f.close()
        print('文件关闭成功')

# 自动关闭
# with as 后声明资源变量，with as 代码块结束之后会自动释放资源
f_name = 'file/test.txt'
with open(f_name) as f:
    content = f.read()
    print(content)

# read(size=-1):        从文件中读取字符串，size限制读取的字符数，size=-1指对读取的字符数没有限制。
# readline(size=-1):    在读取到换行符或文件尾时返回单行字符串。如果已经到文件尾，则返回一个空字符串。size是限制读取的字符数，size=-1表示没有限制。
# readlines():          读取文件数据到一个字符串列表中，每一行数据都是列表的一个元素。
# write(s):             将字符串s写入文件中，并返回写入的字符数。
# writelines(lines):    向文件中写入一个字符串列表。不添加行分隔符，因此通常为每一行未尾都提供行分隔符。
# flush():              刷新写缓中区，在文件没有关闭的情况下将数据写入文件中。


# 复制文件
f_name = 'file/test.txt'
with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.readline()
    print(lines)
    copy_f_name = 'file/copy_file.txt'
    with open(copy_f_name, 'w', encoding='gbk') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')

# 复制二进制文件
f_name = 'file/icon.png'
with open(f_name, 'rb') as f:   # rb只读模式打开二进制文件，二进制文件没有编码
    b = f.read()
    copy_f_name = 'file/copy_icon.png'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('二进制文件复制成功')