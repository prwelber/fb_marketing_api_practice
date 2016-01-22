import math

prime_arr = []

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "%s is not prime" % num
                break
        else:
            return '%s is prime' % num




while len(prime_arr) < 10:
    counter = 10
    for i in range(0, counter):
        is_prime(i)
