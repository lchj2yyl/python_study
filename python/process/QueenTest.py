from multiprocessing import Process, Queue, Pool, Manager
from time import sleep, time
import os


def write_queue(q):
    while True:
        cur_time = time()
        q.put(cur_time)
        print 'write %s to Queue\n' % cur_time
        sleep(2)


def read_queue(q):
    while True:
        item = q.get()
        print 'read %s from queue on process %s' % (item, os.getpid())

q = Queue(3)

process_read1 = Process(target=read_queue, args=(q,))
process_read2 = Process(target=read_queue, args=(q,))

process_write = Process(target=write_queue, args=(q,))

process_read1.start()
process_read2.start()
process_write.start()

process_pool = Pool(3)
pool_queue = Manager().Queue()

process_pool.apply_async(read_queue, (pool_queue,))
process_pool.apply_async(write_queue, (pool_queue,))
process_pool.apply_async(read_queue, (process_pool,))

process_pool.close()
process_pool.join()

