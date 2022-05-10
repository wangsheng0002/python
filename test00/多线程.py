
'''多线程'''
# from threading import Thread
# from time import sleep
#
# bank = {
#     'byhy' : 0
# }
#
# # 定义一个函数，作为新线程执行的入口函数
# def deposit(theadidx,amount):
#     balance =  bank['byhy']
#     # 执行一些任务，耗费了0.1秒
#     sleep(0.1)
#     bank['byhy']  = balance + amount
#     print(f'子线程 {theadidx} 结束')
#
# theadlist = []
# for idx in range(10):
#     thread = Thread(target = deposit,
#                     args = (idx,1)
#                     )
#     thread.start()
#     # thread.join()
#     # 把线程对象都存储到 threadlist中
#     theadlist.append(thread)
#
# for thread in theadlist:
#     thread.join()
#
# print('主线程结束')
# print(f'最后我们的账号余额为 {bank["byhy"]}')


'''Lock()申请获取锁'''

# from threading import Thread,Lock
# from time import sleep
#
# bank = {
#     'byhy' : 0
# }
#
# bankLock = Lock()
#
# # 定义一个函数，作为新线程执行的入口函数
# def deposit(theadidx,amount):
#     # 操作共享数据前，申请获取锁
#     bankLock.acquire()
#
#     balance =  bank['byhy']
#     # 执行一些任务，耗费了0.1秒
#     sleep(0.1)
#     bank['byhy']  = balance + amount
#     print(f'子线程 {theadidx} 结束')
#
#     # 操作完共享数据后，申请释放锁
#     bankLock.release()
#
# theadlist = []
# for idx in range(10):
#     thread = Thread(target = deposit,
#                     args = (idx,1)
#                     )
#     thread.start()
#     # 把线程对象都存储到 threadlist中
#     theadlist.append(thread)
#
# for thread in theadlist:
#     thread.join()
#
# print('主线程结束')
# print(f'最后我们的账号余额为 {bank["byhy"]}')





'''daemon线程'''
# from threading import Thread
# from time import sleep
#
# def threadFunc():
#     sleep(2)
#     print('子线程 结束')
#
# thread = Thread(target=threadFunc,
#                 daemon=True # 设置新线程为daemon线程
#                 )
# thread.start()
# print('主线程结束')



'''多进程'''
# from multiprocessing import Process
#
# def f():
#     while True:
#         b = 53*53
#
# if __name__ == '__main__':
#     plist = []
#     for i in range(5):
#         p = Process(target=f)
#         p.start()
#         plist.append(p)
#
#     for p in plist:
#         p.join()







# from multiprocessing import Process,Manager
# from time import sleep

# def f(taskno,return_dict):
#     sleep(2)
#     # 存放计算结果到共享对象中
#     return_dict[taskno] = taskno
#
# if __name__ == '__main__':
#     manager = Manager()
#     # 创建 类似字典的 跨进程 共享对象
#     return_dict = manager.dict()
#     plist = []
#     for i in range(6):
#         p = Process(target=f, args=(i,return_dict))
#         p.start()
#         p.join()
#         plist.append(p)
#     print(return_dict)
#     # for p in plist:
#     #     p.join()
#
#
#     print('get result...')
#     # 从共享对象中取出其他进程的计算结果
#     # for k,v in return_dict.items():
#     #     print (k,v)



# from multiprocessing import Pool
# import os,time
# def Test(pid):
#     print("当前子进程{}：{}".format(pid, os.getpid()))
#     a=time.time()
#     for i in range(100000000):
#         pass
#     print(time.time()-a)
# if __name__ == '__main__':
#     #多进程
#     print("父进程：{}".format(os.getpid()))
#     pool = Pool()
#     pid = [i for i in range(15)]
#     pool.map(Test, pid)
#     pool.close()
#     pool.join()



import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
