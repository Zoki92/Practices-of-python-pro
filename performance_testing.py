"""Some tools used for performance testing in Python
"""


"""timeit is a module that tests the execution time of code snippets
usage:
python -m timeit "total=sum(range(1000))"
"""

# use timeit within the code
import time
import random
from timeit import timeit
setup = 'from datetime import datetime'
statement = 'datetime.now'
result = timeit(setup=setup, stmt=statement)


def check_if_number_in_input(number, input):
    return number in input


def run_check_for_set():
    is_number_in = check_if_number_in_input(300, set(range(1000)))
    print(f"is number in: {is_number_in}, took: {result}")


def run_check_for_list():
    is_number_in = check_if_number_in_input(300, list(range(1000)))
    print(f"is number in: {is_number_in}, took: {result}")


# run_check_for_set()
# run_check_for_list()
