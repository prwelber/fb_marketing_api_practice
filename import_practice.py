from import_source import add_one, multiply, say_hi, double_multiply

print(add_one(1))
print(multiply(5,4))
print(say_hi('dude'))
print(double_multiply(5,4))

arr = range(0,21)
result = filter(lambda x: x % 2 == 0 or x == 15, arr)
print(list(result))