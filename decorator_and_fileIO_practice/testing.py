import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))

if __name__ == '__main__':
    print('this confirms the file is being run as a script')

a = 1
if a:
    print('a is True')


def fizz_buzz(num):
    for i in range(1,num):
        if i % 5 == 0 and i % 3 == 0:
            print('FB')
        elif i % 3 == 0:
            print('F')
        elif i % 5 == 0:
            print('B')
        else:
            print(i)
fizz_buzz(16)
