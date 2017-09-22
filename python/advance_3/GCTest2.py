import gc

gc.set_debug(gc.DEBUG_STATS)


class People(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __del__(self):
        print 'people %s del' % self.name
people1 = People('lichengjian')
people2 = People('yanyuling')


print gc.get_objects()
print gc.get_count()
print gc.collect()
print gc.get_count()
print people2 in gc.get_objects()

print people1
print people2
print gc.get_count()