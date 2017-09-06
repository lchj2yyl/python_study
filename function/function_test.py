my_sum= lambda x, y: x + y
print my_sum(1, 3)

students = [
    ("lichenjian", 30, 60),
    ("wangxiaoer", 25, 80),
    ("wangdali", 50, 90)
]

students.sort(key=lambda x: x[1])
print students

students.sort(key=lambda x: x[2])
print students

students.sort(cmp=lambda x, y: x[1] < y[1])
print students
