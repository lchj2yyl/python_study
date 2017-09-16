from multiprocessing import Process
from time import sleep
import os


def run_in_child_process(name):
    for i in range(10):
        print name + 'pid : %s' % os.getpid()
        sleep(1)


childProcess = Process(target=run_in_child_process, args=('child process ',))
childProcess.start()
sleep(3)
childProcess.terminate()
childProcess.join()
print 'child process end'
