import time


def calculate_function_run_time_with_desc(desc='none'):
    def calculate_function_run_time(fun):
        def inner():
            start_time = time.time()
            fun()
            end_time = time.time()
            print '%s function run time : %s' % (desc, (end_time - start_time))
        print 'inner %s' % inner
        return inner
    print 'calculate_function_run_time %s' % calculate_function_run_time
    return calculate_function_run_time


@calculate_function_run_time_with_desc('fun_a')
def fun_a():
    print 'this is funA'
    time.sleep(3)


@calculate_function_run_time_with_desc('fun_b')
def fun_b():
    print 'this is funB'
    time.sleep(5)

print fun_a
print fun_b

fun_a()
fun_b()