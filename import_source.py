

def add_one(num):
    return num + 1


def multiply(num1, num2):
    return num1 * num2


def say_hi(name):
    return print('hello %s' % name)


def double_multiply(x, y):
    print(add_one(x))
    return multiply(x, y) * 2


class Person(object):
    name = ''
    age = 0
    location = ''
    job = ''

    # the class 'constructor' is actually an initializer
    def __init__(self, name, age, location, job):
        self.name = name
        self.age = age
        self.location = location
        self.job = job

    def is_adult(self):
        return self.age > 18

    def in_ny(self):
        if self.location[len(self.location)-2:len(self.location)] == 'NY':
            return True
        else:
            return False

phil = Person('phil', 30, 'Plainview, NY', 'programmer')
jack = Person('jack', 78, 'Boulder, CO', 'retired')

