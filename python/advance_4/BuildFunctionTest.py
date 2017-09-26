# map

print map(lambda x: x * x, [1, 2, 3])
print map(lambda x, y: x + y, [1, 2, 3], [2, 3, 4])
print map(lambda x, y, z: x + y + z, [1, 2, 3], [1, 2, 3], [1, 2, 3])

# filter


print filter(None, [1, 2, 3])
print filter(lambda x: x % 2 == 0, [1, 2, 3, 4])


# reduce

print reduce(lambda x, y: x + y, [1, 2, 3, 4])
print reduce(lambda x, y: x * y, [1, 2, 3, 4])


# set
print set('adddddffadd')
