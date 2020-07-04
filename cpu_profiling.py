"""Suppose you’ve written a function that isn’t too expensive but is called many times
in your application. You’ve also written a function that is expensive but is only called
once. If you only have time to fix one, which will it be? Without profiling the code, it’s
hard to know which will speed up your code the most. You can figure it out using
Python’s cProfile module.
"""
import random
import time


def expensive_func():
    execution_time = random.random() / 100
    time.sleep(execution_time)


# if __name__ == '__main__':
#     for _ in range(1000):
#         expensive_func()

# python -m cProfile --sort cumtime cpu_profiling.py

"""When looking at the output of cProfile, you’ll want to search for calls with a high
percall value or a big jump in cumtime. These characteristics mean the call takes up a
good chunk of your program’s execution time. Speeding up a slow function can
improve the program speed a fair amount, and cutting the execution time of a function that’s
called thousands of times can be a really big win.
"""


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    return the_list.sort()


def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    return the_list.sort()


if __name__ == '__main__':
    sort_expensive()
    for _ in range(1000):
        sort_cheap()
