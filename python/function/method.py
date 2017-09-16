import sys

class test:
    def __init__(self):
        self.list = []
        print 'init'

    def __str__(self):
        return str(self.list)

    def append(self, item):
        self.list.append(item)


def append(new_item, list=test()):
    list.append(new_item)
    print sys.getrefcount(list)
    return list
print append.__dict__
list = append('one')
list = append('two')
print append('three')

class People:
    def __init__(self):
        print 'init'

    def testObjectMethod(self):
        print 'eat'

    @classmethod
    def testClassMethod(cls):
        print 'testClassMethod'

    @staticmethod
    def testStaticMethod():
        print 'testStaticMethod'
test = People()

print People.testObjectMethod
print test.testObjectMethod

print People.testClassMethod
print test.testClassMethod

print People.testStaticMethod
print test.testStaticMethod

print People.__dict__


def testMethod():
    print 'testMethod'

def testMethod1():
    print 'testMethod1'

print testMethod
print testMethod1
testMethod = testMethod1
testMethod()

People.testStaticMethod = testMethod
print People.testStaticMethod


def fn(n):
    prev, cur = 0, 1
    while (n > 0):
        n = n -1
        yield cur
        prev, cur = cur, cur + prev

test = fn(10)
print test

print test.next()

generator = (x for x in range(4))
print generator
print sum(generator)
print sum(generator)

iteror = [x for x in range(4)]
print iteror
print sum(iteror)
print sum(iteror)


class Parent():
    def __init__(self, name):
        self.name = name

    def printName(self):
        print self.name

    @classmethod
    def testClassMethod(cls):
        pass


class Child(Parent):
    def __init__(self):
        pass






print Child.__dict__
child = Child()
child.name = "lichengjian"
child.printName()

print Parent.printName
print Child.printName

print Parent.printName == Child.printName
print Child.printName == child.printName

print Parent.testClassMethod == Child.testClassMethod
print Child.testClassMethod == child.testClassMethod


class Parent:
    class_name = 'parent'
    def __init__(self):
        self.name = ""

class Child(Parent):
    def __init__(self):
        pass

child = Child()

print Parent.class_name #paent
print child.class_name #parent
print Child.class_name #parent
print Parent.class_name == Child.class_name # true
child.class_name = 'child'

Child.class_name = 'child'
print Parent.class_name #parent
print Child.class_name #parent


class Parent:
    def __init__(self):
        pass
    def test(self):
        pass
    @classmethod
    def testClassMethod(cls):
        pass

    @staticmethod
    def testStaticMethod():
        pass

class Child(Parent):
    def __init__(self):
        pass


child = Child()

print Child.test == Parent.test #true
print child.test == Child.test #fasle

print Child.testClassMethod == Parent.testClassMethod #fasle
print child.testClassMethod == Child.testClassMethod #true

print Child.testStaticMethod == Parent.testStaticMethod #true
print child.testStaticMethod == Parent.testStaticMethod #true



