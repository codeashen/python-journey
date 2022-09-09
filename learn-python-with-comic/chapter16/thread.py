import threading

# 获取当前线程对象
import time

t = threading.currentThread()
print(t.name)
# 活跃线程数
print(threading.activeCount())
# 获取主线程对象
t = threading.main_thread()
print(t.name)


################### 创建线程方式一： 自定义函数实现线程体 ###################

# 线程体函数
def thread_body():
    t = threading.currentThread()
    for i in range(5):
        print("第{}次执行线程{}".format(i, t.name))
        # 线程休眠
        time.sleep(2)
    print("线程{}执行完成".format(t.name))


# 创建线程对象
t1 = threading.Thread(target=thread_body, name='MyThread1')
# 启动线程
t1.start()


################### 创建线程方式二： 自定义线程类实现线程体 ###################

class SmallThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    # 定义线程体
    def run(self):
        t = threading.currentThread()
        for i in range(5):
            print("第{}次执行线程{}".format(i, t.name))
            # 线程休眠
            time.sleep(2)
        print("线程{}执行完成".format(t.name))


t2 = SmallThread('MyThread2')
t2.start()
