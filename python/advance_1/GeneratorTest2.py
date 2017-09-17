def gen(data):
    print 'befor yield data : %s ' % data
    back_data = yield data
    print 'resume yield data : %s' % back_data


g = gen(1)
try:
    print g.next()
    print g.send(3)
except StopIteration as error:
    print error

