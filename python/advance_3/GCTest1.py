import sys
import gc

b = 3
c = 3

print sys.getrefcount(b)
del b
print sys.getrefcount(c)
del c
print sys.getrefcount(3)

b = -100
c = -100
print id(b)
print id(c)
print sys.getrefcount(b)

print gc.get_count()
gc.collect(0)
print gc.get_count()

print b
print c
print gc.get_count()
print b
