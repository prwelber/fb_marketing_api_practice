import time
from time import sleep


def timing_function(some_function):
    """
    Outputs the time a function takes to execute
    """

    def wrapper():

        t1 = time.time()
        some_function()
        t2 = time.time()
        return 'Time it took to run the function: ' + str(t2 - t1) + '\n'

    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in range(0,2500):
        num_list.append(num)
    print('sum of all the numbers: ' + str(sum(num_list)))

# print(my_function())





# ---------------------------------- #

def sleep_decorator(function):

    # Limits how fast a function can be called

    def wrapper(*args, **kwargs):
        sleep(.5)
        return function(*args, **kwargs)

    return wrapper

@sleep_decorator
def print_number(num):
    return num

print(print_number(1000))











