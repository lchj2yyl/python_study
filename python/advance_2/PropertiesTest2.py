class People(object):
    def __init__(self):
        self.__name = 'lichenjian'

    @property
    def name(self):
        print 'name'
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.getter
    def get_name(self):
        print 'get name'
        return self.__name

    @name.setter
    def name(self, name):
        print 'set name'
        self.__name = name


people = People()
print people.name
people.name = 'nihao'
print people.name
print dir(people)
