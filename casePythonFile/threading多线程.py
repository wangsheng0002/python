import time
import threading

def thread_run(name):
    print("%s's first thread!!!"% name)
    time.sleep(5)

mike = threading.Thread(target=thread_run, args=('Mike', ))
jone = threading.Thread(target=thread_run, args=('jone', ))

mike.start()
jone.start()

'''daemon

当 daemon = False 时，线程不会随主线程退出而退出（默认时，就是 daemon = False）
当 daemon = True 时，当主线程结束，其他子线程就会被强制结束
'''
import time
import threading

def thread_mike_run(name):
    time.sleep(1)
    print('mike thread is running 1S')
    time.sleep(5)
    print("%s's first thread!!!"% name)

def thread_jone_run(name):
    time.sleep(2)
    print("%s's first thread!!!"% name)


mike = threading.Thread(target=thread_mike_run, args=('Mike', ), daemon=True)    #设置daemon为True
#mike = threading.Thread(target=thread_mike_run, args=('Mike', ))
jone = threading.Thread(target=thread_jone_run, args=('jone', ))


mike.start()
jone.start()
print('main thread')    #由于线程没有join()，所以主线程会先运行；而jone的daemon为false，所以主线程会等待jone线程运行完毕；但是mike的daemon为True，所以主线程不会等待mike线程
'''执行结果：
main thread
mike thread is running 1S    #mike线程只执行了1S的print，5S的为执行就直接退出了
jone's first thread!!!
'''