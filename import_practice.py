from import_source import add_one, multiply, say_hi, double_multiply

print(add_one(1))
print(multiply(5, 4))
print(say_hi('dude'))
print(double_multiply(5, 4))

arr = range(0, 21)
result = filter(lambda x: x % 2 == 0 or x == 15, arr)
print(list(result))

# FINDING SUBSTRINGS (like a contains method)
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

def error_handling(num):
    if num == True or num == False:
        return 'you can\'t enter a boolean, only a number'
    elif num == None:
        return 'what are you doing clown'
    try:
        return 50 % num
    except ZeroDivisionError:
        return 'you can\'t do modulus zero'
    except TypeError:
        return 'you must enter a number'

print(error_handling(0))

print(a_string.startswith('The'))
print(a_string.endswith('og.'))
