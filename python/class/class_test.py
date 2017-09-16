class People:
    def __init__(self):
        self.name = 'lichengjian'
        self.age = 100

    def __str__(self):
        return "name : " + self.name + ' age : ' + str(self.age)


test = People()
print test


class Student(People):
    def __init__(self):
        People.__init__(self)


test = Student()
print test


class Parent(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        print 'this is parent __new__ function'
        var = object.__init__(cls)
        print var
        return var


class Child(Parent):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        print 'this is Child __new__ function'
        var = object.__new__(cls)
        print var
        return var

    def test(self):
        print 'this is child test'

child = Child()
child.test()


class Singleton(object):
    sInstance = None
    sIsInit = False

    def __init__(self, name, age):
        if Singleton.sIsInit:
            return
        print '__init__'
        self.name = name
        self.age = age
        Singleton.sIsInit = True

    def __new__(cls, *args, **kwargs):
        print '__new__'
        if cls.sInstance:
            return cls.sInstance
        print 'create new objcet'
        cls.sInstance = object.__new__(cls)
        return cls.sInstance

singleton = Singleton('lichengjian', 18)
singleton = Singleton('lichengjian', 38)


