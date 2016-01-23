def echo(string):
  return string


def my_decorator(some_function):

    def wrapper(argss):

        num = 1

        if num == 10:
            print('YES!')
        else:
            print('NO!')

        some_function(argss)

        print('Goodbye %s!' % argss)

    return wrapper


if __name__ == '__main__':
    my_decorator()

# def just_some_function():
#     print("Wheee!")


# just_some_function = my_decorator(just_some_function)
# just_some_function()