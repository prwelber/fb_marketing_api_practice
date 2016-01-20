from import_source import add_one, multiply, say_hi, double_multiply

print(add_one(1))
print(multiply(5, 4))
print(say_hi('dude'))
print(double_multiply(5, 4))

arr = range(0, 21)
result = filter(lambda x: x % 2 == 0 or x == 15, arr)
print(list(result))

# FINDING SUBSTRINGS
# Using the in keyword
a_string = 'The quick brown fox jumps over the lazy dog.'
word_to_find = 'fox'
if 'own' in a_string:
    print(True)
# Using the str.find method
index_val = a_string.find(word_to_find)
print(a_string[index_val:len(word_to_find) + index_val])

if 25 in arr:
    print(True)
else:
    print(False)
    # Should print False


