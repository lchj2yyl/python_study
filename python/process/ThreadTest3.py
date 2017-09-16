import random
import time
from threading import Thread
import Queue

product = Queue.Queue(10)


class Producer(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.num = 0

    def run(self):
        while True:
            msg = self.name
            self.num = self.num + 1
            product.put(msg)
            print '%s put %s into queue' % (self.name, msg)
            time.sleep(random.random() * 10)


class Customer(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            msg = product.get()
            print '%s get %s from queue' % (self.name, msg)
            time.sleep(random.random() * 50)


for i in range(5):
    producer = Producer('producer %s' % (i + 1))
    customer = Customer('customer %s' % (i + 1))
    producer.start()
    customer.start()