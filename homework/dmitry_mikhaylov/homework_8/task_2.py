import sys


def fib_generator():
    num_1 = 0
    num_2 = 1
    while True:
        yield num_2
        num_1, num_2 = num_2, num_1 + num_2


sys.set_int_max_str_digits(20800)
count = 1
for i in fib_generator():
    if count in [5, 200, 1000, 100000]:
        print(i)
    if count == 100000:
        break
    count += 1
