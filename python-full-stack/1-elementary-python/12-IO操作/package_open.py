# coding:utf-8

import os


def create_package(path):
    if os.path.exists(path):
        raise Exception('%s 已经存在不可创建' % path)
    os.makedirs(path)
    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write('# coding:utf-8\n')
    f.close()


class Open(object):
    def __init__(self, path, mode='w', is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode)
        if self.is_return:
            message = '%s\n' % message
        f.write(message)
        f.close()

    def read(self, is_strip=True):
        result = []
        with open(self.path, mode=self.mode) as f:
            data = f.readlines()
        for line in data:
            if is_strip == True:
                temp = line.strip()
                if temp != "":
                    result.append(temp)
            else:
                if line != '':
                    result.append(line)
        return result


if __name__ == '__main__':
    current_path = os.getcwd()
    # path = os.path.join(current_path, 'test1')
    # create_package(path)
    # open_path = os.path.join(current_path, 'b.txt')
    o = Open('package_datetime.py', mode='r')
    # o.write('你好 小慕')
    data = o.read(is_strip=False)
    print(data)
