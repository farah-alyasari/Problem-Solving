'''
Scenario

    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

'''

# my solution

from datetime import datetime

def time_stamp(our_function):
    # execution start time
    ts1 = datetime.now()
    print(ts1.strftime("%Y-%m-%d %I:%M:%S"))
    def internal_func(*args):
        our_function(*args)
        # execution ended time
        ts2 = datetime.now()
        print(ts2.strftime("%Y-%m-%d %I:%M:%S"))
    return internal_func

@time_stamp
def add(a, b):
    res = a+b
    print("a+b: {}".format(res))

add(4,5)

# thier solution

from datetime import datetime

def time_stamping_machine(own_function):
    def internal_wrapper(*args, **kwargs):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print()
        print(string_timestamp)
        return own_function(*args, **kwargs)
    return internal_wrapper

@time_stamping_machine
def simple_hello():
    print("Hello from simple function!")

@time_stamping_machine
def add_two_objects(n1, n2):
    return n1 + n2

@time_stamping_machine
def multiply_two_objects(n1, n2):
    return n1 * n2

simple_hello()
print('Result:', add_two_objects('Hello', 'Python'))
print('Result:', add_two_objects(100, 88))
print('Result:', multiply_two_objects(100, 88))
