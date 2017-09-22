import gc


class People(object):
    pass

people1 = People()
people2 = People()

print gc.get_count()
gc.collect(2)
print gc.get_count()