# -*- coding:utf-8 -*-
__auth__ = 'christian'


import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数
    print("running on number:%s" % num)
    time.sleep(1)
    print ("task done", num)

if __name__ == '__main__':
    start_time = time.time()
    t_obj = [] # 存线程实例
    for i in range(50):
        t = threading.Thread(target=sayhi, args=('t-%s' % i, ))
        # t.setDaemon(True) # 把当前线程设置为守护进程
        t.start()
        t_obj.append(t)  # 为了不阻塞后面的线程启动，不在这里使用join方法，先存放到一个列表里

    for t in t_obj:  # 循环线程实例表，等待所有线程执行完毕
        t.join()

    print ('--------all threads have finished.--------')
    # print (threading.current_thread(),threading.active_count())

    print ('cost:', time.time() - start_time)


