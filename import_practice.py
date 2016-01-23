import import_source
# To import package, syntax is 'import directory.file'
import package_practice.to_import as pack

print(pack.echo('we are soooo thirsty'))
print(pack.echo('plz halp me 2 code thingz'))
print(import_source.add_one(1))
print(import_source.multiply(5, 4))
print(import_source.say_hi('phil'))
print(import_source.double_multiply(5, 4))

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
    if num == 'True' or num == 'False':
        return 'you can\'t enter a boolean, only a number'
    elif num == None:
        return 'what are you doing clown'
    try:
        return 25 % num
    except ZeroDivisionError:
        return 'you can\'t do modulus zero'
    except TypeError:
        return 'you must enter a number'
    else:
        return num

print(error_handling(4))

print(a_string.startswith('The'))
print(a_string.endswith('og.'))

