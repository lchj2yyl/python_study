def eggs_fun(obj):
    return obj.value * 4


def ham_fun(obj, expend):
    print obj
    return obj.value + expend


class Extender(type):
    def __new__(meta, class_name, supers, class_dirs):
        print 'this is new'.center(60, '=')
        class_dirs['eggs'] = eggs_fun
        class_dirs['ham'] = ham_fun
        return type.__new__(meta, class_name, supers, class_dirs)


class Client1(object):
    __metaclass__ = Extender

    def __init__(self, value):
        print 'init'
        self.value = value
        print self.value

client1 = Client1('nihao')
print client1
print client1.value
print client1.eggs()
print client1.ham('test')
