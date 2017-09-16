import threading


student = threading.local()


def print_student_name():
    print '%s student name is %s ' % (threading.current_thread().name, student.name)


def process_thread(name):
    student.name = name
    print_student_name()


thread1 = threading.Thread(target=process_thread, args=('lichengjian',), name="thread-1")
thread2 = threading.Thread(target=process_thread, args=('yanyuling',), name='thread-2')

thread1.start()
thread2.start()