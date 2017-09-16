try:
    file_obj = open('abc', 'rb')
except Exception as exception:
    print exception
else:
    print 'no exception'
finally:
    print 'this is the finally'
