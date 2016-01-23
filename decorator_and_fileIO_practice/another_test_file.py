import testing

from time import sleep

def sleeping(func):
    def wrapper(args):
        sleep(.5)
        return func(args)
    return wrapper

@sleeping
def print_word(word):
    return word

# print(print_word('helllooooo snow'))

# for i in range(0,6):
#     print(print_word(i))

## ------------------------------------------------------- ##

# This wrapper should validate a key in a dictionary

def key_validator(func):
    def wrapper(args):
        d = func(args)
        if d.get('name', 'default_value') == 'phil':
            print('the key "%s" exists' % args)
        else:
            print('the key "%s" does not exist' % args)
        return func(args)
    return wrapper


@key_validator
def dict_func(key):
    return {key: 'phil'}

print(dict_func('name'))

## ---------------------------------------------------------- ##

# authentication decorator

arr_of_users = ['phil', 'cooper', 'nelly']
def authenticate(func):
    def wrapper(args):
        name = func(args)
        if name in arr_of_users:
            return 'the user %s exists' % args
        else:
            return 'the user %s doesn\'t exist' % args
        return func(args)
    return wrapper



@authenticate
def existing_user(user_name):
    return user_name

print(existing_user('rach'))

## ---------------------------------------------------------- ##










