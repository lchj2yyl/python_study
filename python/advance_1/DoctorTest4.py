class DoctorClass(object):
    def __init__(self, fun):
        print 'Doctor init'
        self.fun = fun
        print 'Doctor init end'

    def __call__(self, *args, **kwargs):
        print '__call__'
        self.fun()


@DoctorClass
def test():
    print 'this is test'

test()