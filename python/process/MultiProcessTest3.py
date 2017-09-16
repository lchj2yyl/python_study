from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, sleep_time, target=None, args=(), name=None):
        self.sleep_time = sleep_time
        Process.__init__(self, target=target, args=args, name=name)

    def run(self):
        start_time = time.time()
        print '%s start sleep time : %s' % (self.name, start_time)
        time.sleep(self.sleep_time)
        end_time = time.time()
        print '%s end sleep time : %s' % (self.name, end_time)
        Process.run(self)


def run_in_child_process():
    print 'run in child process'

child_process1 = MyProcess(sleep_time=3, name='process1')
child_process1.start()
child_process2 = MyProcess(sleep_time=3, target=run_in_child_process, name='process2', args=())
child_process2.start()
