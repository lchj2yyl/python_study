class People(object):
    pass

print type(People)

Test = type('Test', (), {})
print Test
print type(Test)

Test2 = Test

print Test2
print type(Test2)

# help(Test2)

People = type('People', (), {"type": "people"})
print People.type

Student = type('Student', (People,), {'desc': "I m a student"})
print Student.type
print Student.desc

print Student.__class__.__class__


def init(self):
    print 'this is init'
    self.name = 'lichengjian'

@classmethod
def class_method(cls):
    print 'this is a class method'

@staticmethod
def static_method():
    print 'this is a static method'

People = type('People', (object,),
              {
                  '__init__': init,
                  'class_method': class_method,
                  'static_method': static_method,
                  'type': 'this is a People'
              })


people = People()
people.class_method()
people.static_method()
print people.type
