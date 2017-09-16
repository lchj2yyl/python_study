from time import sleep

def sina():
    for i in range(3):
        print 'sining'
        sleep(0)

def dance():
    for i in range(3):
        print 'dancing'
        sleep(0)

sina()
dance()

import os

pid = os.fork()
print pid
if pid == 0:
    print 'this is child process %s' % os.getpid()
else:
    print 'this is parent process %s ' % os.getpid()


