import copy

a = (1, 2, 3)
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print 'stable'.center(60, '=')
print id(a)
print id(b)
print id(c)
print id(d)

e = [1, 2, 3, 4]
f = e
g = copy.copy(e)
h = copy.deepcopy(e)

print 'no stable'.center(60, '=')
print id(e)
print id(f)
print id(g)
print id(h)

e = [{'name': 'lichengjian', 'age': 16}]
f = copy.copy(e)
g = copy.deepcopy(e)

print 'copy&deepcopy'.center(60, '=')
print 'before change'
print 'e : %s' % str(e)
print 'f : %s' % str(f)
print 'g : %s' % str(g)

e[0]['name'] = 'yanyuling'
e.append({'name': 'wangxiaoer', 'age': 66})
print 'after change'
print 'e : %s' % str(e)
print 'f : %s' % str(f)
print 'g : %s' % str(g)


e = ({'name': 'lichengjian', 'age': 16})
f = copy.copy(e)
g = copy.deepcopy(e)

print id(e)
print id(f)
print id(g)

import __builtin__


print dir(__builtin__)