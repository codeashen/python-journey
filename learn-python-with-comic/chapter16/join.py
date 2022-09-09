import threading
import time

######################### join #########################
# 共享变量
value = []


# 线程体函数
def thread_body():
    print('t1子线程开始...')
    for n in range(2):
        print('t1子线程执行...')
        value.append(n)
        time.sleep(2)
    print('t1子线程结束')


print('主线程开始...')
t1 = threading.Thread(target=thread_body)
t1.start()
# join函数阻塞当前线程，等待 t1 线程执行完
t1.join()
print('value = {}'.format(value))
print('主线程继续执行')

######################### 控制 #########################

isrunning = True

# 工作线程体函数
def workthread_body():
    while isrunning:
        print('工作线程执行中...')
        time.sleep(2)
    print('工作线程执行结束')

# 控制线程体函数
def controlthread_body():
    global isrunning
    while isrunning:
        command = input('请输入控制指令：')
        if command == 'exit':
            isrunning = False
            print('控制线程结束')

# 创建工作线程
workthread = threading.Thread(target=workthread_body)
# 创建控制线程
controlthread = threading.Thread(target=controlthread_body)

# 启动工作线程
workthread.start()
# 启动控制线程
controlthread.start()
