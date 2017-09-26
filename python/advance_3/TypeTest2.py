class Meta(type):
    def __new__(meta, class_name, supers, class_dirs):
        print 'this is new'.center(60, '=')
        print meta
        print class_name
        print supers
        print class_dirs
        generate_class = type.__new__(meta, class_name, supers, class_dirs)
        print generate_class
        return generate_class

    def __init__(self, class_name, supers, class_dirs):
        print 'this is init'.center(60, '=')
        print self
        print class_name
        print supers
        print class_dirs
        type.__init__(self, class_name, supers, class_dirs)

    def __call__(self, *args, **kwargs):
        print 'this call'.center(60, '=')
        print self
        print args
        print kwargs
        type.__call__(self, *args, **kwargs)


class MetaTest1(object):
    __metaclass__ = Meta

meta_test = MetaTest1()
print meta_test