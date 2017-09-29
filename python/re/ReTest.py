import re


p = re.match('a*', 'A')
print p.group()


def print_group(p):
    if p:
        print p.group()
    else:
        print 'None'

p = re.match('[a-zA-Z]+[\w_]*', 'name1')
print_group(p)
p = re.match('[a-zA-Z]+[\w_]*', '_name')
print_group(p)
p = re.match('[a-zA-Z]+[\w_]*', '2_name')
print_group(p)


p = re.match('[1-9]?[0-9]', '7')
print_group(p)

p = re.match('[1-9]?[0-9]', '09')
print_group(p)
p = re.match('[1-9]?[0-9]', '77')
print_group(p)


p = re.match('[a-zA-Z1-9_]{6}', 'ddnsaidsafnfsiandsidsaafdsdafdsaf')
print_group(p)

p = re.match('[a-zA-Z1-9_]{6,10}', 'ddnsaidsafnfsiandsidsaafdsdafdsaf')
print_group(p)

p = re.match('[a-zA-Z1-9_]{6,}', 'ddnsaidsafnfsiandsidsaafdsdafdsaf')
print_group(p)

p = re.match('[a-zA-Z1-9_]{,6}', 'ddnsaidsafnfsiandsidsaafdsdafdsaf')
print_group(p)

# mail check
p = re.match('\w{4,20}@(163|126)\.com$', '123dainddfsadf@126.com')
print_group(p)

# check num 0 - 99
p = re.match('^([1-9]?\d|100)$', '100')
print print_group(p)

# check phone number
p = re.match('([^.]*)-(\d*)', '000d0-12343443443')
print p.group(1)
print p.group(2)

# check html
p = re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>hh</html>')
print p.group()

# check <html><h1>www.baidu.com</h1></html>
p = re.match(r'<(\w*)><(\w*)>.*</\2></\1>', '<html><h1>www.baidu.com</h1></html>')
print p.group()

p = re.match(r'<(?P<name1>\w*)></(?P=name1)>', '<html></html>')
print p.group()

p = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', '<html><h1>www.baidu.com</h1></html>')
print p.group()

# search
p = re.search(r'\d+', 'read count 999999 download count 8888')
print p.group()

# find all
p = re.findall(r'\d+', 'read count 999999 download count 8888')
print p

# sub
p = re.sub(r'\d+', '000', 'read count 99999')
print p


def add_num(p):
    count = p.group()
    return str(int(count) + 1)

p = re.sub(r'\d+', add_num, 'read count 0')
print p

p = re.match('<(?P<name>\w*)>(.*)</(?P=name)>', '<h1>this is test</h1>')
print p.group()
print p.group(2)

p = re.findall('<(?P<name>\w*)>(.*)</(?P=name)>', '<h1>this is test</h1>')
print p

p = re.split(r':| ', 'lichengjian: 18 location beijing')
print p

s = 'this is a number 233-444-22-333'
p = re.match('.+(\d+-\d+-\d+-\d+)', s)
print p.groups()
p = re.match('.+?(\d+-\d+-\d+-\d+)', s)
print p.groups()


html_str = '''<img data-original="http:wwww.baidu.com" src="https://www.google.com"/>
'''
p = re.findall(r'\"(http[s]*.*?)\"', html_str)
print p

url = 'http://www.baid.com/images/3dnidfsfsfsf.png'
p = re.findall(r'(http://.*?/)', url)
print p

words = 'hello python'
p = re.split(' ', words)
print p

foo = 'hello'
bar = r'hello'
print 'foo type %s bar type %s foo == bar %s' % (type(foo), type(bar), (foo == bar))

foo = '\n'
bar = r'\n'
print 'foo length %s bar length % foo == bar %s' % (int(len(foo)), int(len(bar)), foo == bar)

foo = '\\\\'
bar = r'\\'
print 'foo length %s bar length % foo == bar %s' % (int(len(foo)), int(len(bar)), foo == bar)
print type(foo), type(bar)

p = re.match('(\d*)(\w*)', '123abd')
print p.groups()
print p.group()
print p.group(1)
print p.group(2)
foo ='\\'
bar =r'\\'
bar =r'\w'
print foo
print bar

foo = '\\w'
bar = '\w'
print foo
print bar
print foo == bar


p = re.match('(\w*)-\\1', 'adb-adb')
p = re.match(r'(\w*)-\1', 'adb-adb')
print p.groups()

print r'\1'
print '\\1'

print '\\w'
print '\w'


test_str = 'adb Android\nadb Android'
print test_str
p = re.match('Android', test_str)
if p:
    print p.group()
else:
    print 'none'

p = re.search('Android', test_str, re.MULTILINE)
print p.group()
p = re.search('^Android', test_str, re.MULTILINE)
if p:
    print p.group()
else:
    print 'none'
p = re.findall('^Android', test_str)
print p

