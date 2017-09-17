def gen_throw():
    data = yield
    print data

    try:
        yield data
    except Exception as e:
        yield str(e)

gen = gen_throw()
gen.next()

print gen.send(1)

print gen.throw(Exception, 'test')
