#!/usr/bin/env python
#coding=utf-8
#  Created by zhoupan on 7/20/16.

'''
    导入相关内容
'''

from time import ctime,sleep
import thread

'''
    定义sleep时间
'''
loops = [4,2]

def loop(nloop,sec,lock):
    'nloop 标志是哪个线程,sec sleep的时间,look 锁对象'
    print 'start loop',nloop,'at:',ctime()
    sleep(sec)
    print 'stop loop', nloop, 'at:', ctime()
    #释放锁
    lock.release()
def main():
    '对每个对象进行加锁，然后分别创建新的线程运行'
    print 'start...',ctime()
    locks=[]

    for i in range(len(loops)):
        lock = thread.allocate_lock() #创 建锁
        lock.acquire() #获得锁
        locks.append(lock)
    for i in range(len(loops)):
        thread.start_new_thread(loop,(i,loops[i],locks[i])) #在新线程里面运行

    for i in range(len(loops)):
        while locks[i].locked():pass
    print 'stop...',ctime()
if __name__ == '__main__':
    main()