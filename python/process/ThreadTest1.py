import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name=None):
        threading.Thread.__init__(self, name=name)

    def run(self):
        for num in range(10):
            print 'this is thread %s %s' % (self.name, (num + 1))
            time.sleep(1)

for i in range(5):
    my_thread = MyThread('mythread-' + str(i + 1))
    my_thread.start()

