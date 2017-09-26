# python 2中使用元类来创建对象依然存在一个问题，如何不使用type来实现元类的定义

class SuperMeta:
    def __call__(self, *args, **kwargs):
        print 'this is call '


class Meta(SuperMeta):
    def __new__(cls, class_name, supers, class_dirs):
        print 'this is in new'.center(60, '=')
        generate_class = type(class_name, supers, class_dirs)
        generate_class.__init__(class_name, supers, class_dirs)

    def __init__(self, class_name, supers, class_dirs):
        print 'this is in init'.center(60, '=')
        print id(self)


class MetaTest:
    __metaclass__ = Meta

print id(MetaTest)
# print id(MetaTest)
#
# meta_test = MetaTest()
#
# print meta_test