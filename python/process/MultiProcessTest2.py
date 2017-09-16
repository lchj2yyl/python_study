from multiprocessing import Process
import time


def process_sleep(process_name, sleep_time):
    print '%s start sleep' % process_name
    start_time = time.time()
    time.sleep(sleep_time)
    end_time = time.time()
    print '%s sleep time is %s' % (process_name, (end_time - start_time))


def print_process_state(process):
    print 'process : %s alive : %s ' % (process.name, process.is_alive())


process1 = Process(target=process_sleep, args=('process_1', 3), name="process_1")
process2 = Process(target=process_sleep, args=('process_2', 2), name="process_2")
process1.start()
process2.start()
print_process_state(process1)
print_process_state(process2)
process2.join()
print_process_state(process1)
print_process_state(process2)

