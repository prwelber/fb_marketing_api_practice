from to_import import my_decorator

@my_decorator
def say_something(name):
    print("Hey there %s!" % name)

say_something('phil')

