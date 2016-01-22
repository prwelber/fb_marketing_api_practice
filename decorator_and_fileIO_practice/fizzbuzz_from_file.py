import json

f = open('numbs_for_fizzbuzz', 'r')
# print(f.readline())
# print(f.read())

# line1 = f.readline()
# nums = line1.split(' ')

def fizzbuzz(line):
    line = line.split(' ')
    x, y, n = int(line[0]), int(line[1]), int(line[2])
    for num in range(1, n + 1):
        if num % x == 0 and num % y == 0:
            print('FizzBuzz')
        elif num % x == 0:
            print('Fizz')
        elif num % y == 0:
            print('Buzz')
        else:
            print(num)



# for line in f:
#     fizzbuzz(line)
f.close()

