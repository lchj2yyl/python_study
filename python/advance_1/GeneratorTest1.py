def foo():
    for i in range(5):
        print i
        temp = yield i
        print temp

f = foo()

f.send(None)
f.send('nihaod')

f.throw()
f.close()
f.next()

