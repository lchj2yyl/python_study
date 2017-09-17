def fa_gen():
    data = yield
    print 'fa receive %s' % data
    fb.send(data * 2)


def fb_gen():
    data = yield
    print 'fb receiver %s' % data
    fa.send(data * 2)


fa = fa_gen()
fa.next()

fb = fb_gen()
fb.next()

fa.send(1)