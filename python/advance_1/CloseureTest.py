def counter(start=[0]):
    def inner():
        start[0] = start[0] + 1
        return start[0]
    return inner


test = counter([0])

print test()
print test()

