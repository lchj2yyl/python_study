import time


def calculate_function_run_time(fun):
    def inner():
        start_time = time.time()
        fun()
        end_time = time.time()
        print 'function run time : %s' % (end_time - start_time)
    print inner
    return inner


@calculate_function_run_time
def fun_a():
    print 'this is funA'
    time.sleep(3)


@calculate_function_run_time
def fun_b():
    print 'this is funB'
    time.sleep(5)

print fun_a
print fun_b

fun_a()
fun_b()