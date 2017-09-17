import time


def add_time(fun):
    def inner():
        return time.ctime() + str(fun())
    return inner


def add_desc(fun):
    def inner():
        return 'China ' + str(fun())
    return inner


@add_desc
@add_time
def fun_a():
    return 'this is fun'

print fun_a()
