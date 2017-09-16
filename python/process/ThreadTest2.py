from threading import Thread, Lock

num = 0
mutex = Lock()


def add():
    global mutex
    global num
    mutex.acquire()
    for i in range(10000000):
        num = num + 1
    mutex.release()

for outer_i in range(10):
    thread1 = Thread(target=add)
    thread2 = Thread(target=add)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print 'num = %s ' % num
    num = 0

print num
