from threading import Thread
import time
from multiprocessing import Process

i = 0


def add():
    start_time = time.time()
    for _ in range(100000000):
        global i
        i = i + 1
    end_time = time.time()
    print 'time : %s' % (end_time - start_time)

# add()
#
for _ in range(2):
    thread = Thread(target=add)
    thread.start()

# for _ in range(2):
#     process = Process(target=add)
#     process.start()
