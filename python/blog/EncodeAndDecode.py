# -*- coding: utf-8 -*-


# UnicodeEncodeError
# UnicodeEncodeError发生在unicode encode的过程中，将unicode写入文件的时候
# python会将unicode进行编码，如果不指定将使用默认编码ascii进行编码，而ascii中不
# 包含中文，所以会出现UnicodeEncodeError
str_test = u'你好'
str_test = str_test.encode('utf-8')
file_obj = open('encode_test', 'w')
file_obj.write(str_test)

# UnicodeDecodeError
# UnicodeDecodeError发生字符串解码为unicode的过程中，str_test初始化使用utf-8编码
# 解码的时候必须使用utf-8进行解码，使用gbk进行解码将出现UnicodeDecodeError, utf-8
# 占用3个字节 gbk占用两个字节,所以使用偶数个utf-8格式的字符使用utf-8解码也可以解码，不出现
# 错误，但是结果是错误的
str_test = '你好好'
str_test = str_test.decode('gbk')
print str_test

