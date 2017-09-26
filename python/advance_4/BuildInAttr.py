

class Persoon(object):
    def __delattr__(self, item):

for item in dir(Persoon):
    print item