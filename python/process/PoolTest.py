from multiprocessing import Pool
import os
import time


def task(task_id):
    start_time = time.time()
    print 'task %s in process %s start on %s' % (task_id, os.getpid(), start_time)
    time.sleep(3)
    end_time = time.time()
    print 'task %s in process %s end on %s' % (task_id, os.getpid(), end_time)

pool = Pool(10)

for i in range(10):
    pool.apply(task, args=('task' + str(i+1),),)

pool.close()
pool.join()

