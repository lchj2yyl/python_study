class Person(object):
    def __init__(self):
        self.__type = 'persion'
        self._name = 'lichengjian_persion'

    def print_parent_type(self):
        print self.__type

    def print_parent_name(self):
        print self._name


class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.__type = 'student'
        self._name = 'lichengjian_child'

    def print_type(self):
        print self.__type

    def print_name(self):
        print self._name

student = Student()
student.print_parent_type()
student.print_type()
student.print_parent_name()
student.print_name()