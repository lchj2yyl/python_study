class People(object):
    __slots__ = ["name", "age"]


class Child(People):
    pass


people = Child()
people.name = 'lchj'
people.age = 17
people.sex = 'man'