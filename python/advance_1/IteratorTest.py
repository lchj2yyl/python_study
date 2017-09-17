from collections import Iterator

file_obj = open('IteratorTest.py', 'rb')
print isinstance(file_obj, Iterator)
for line in file_obj:
    print line

iter(file_obj)