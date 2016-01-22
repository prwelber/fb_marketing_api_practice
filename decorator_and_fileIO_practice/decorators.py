import sys, os
from time import sleep

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath('..')

# print(parent_dir + '\n' + current_dir + '\n' + current_file)



def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(args):
        sleep(.5)
        return function(args)
    return wrapper


@sleep_decorator
def print_number(num):
    return num
"""
print(print_number(111))

for num in range(1, 6):
    print(print_number(num))
"""
## ---------------------------------------------------------------- ##

from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass
