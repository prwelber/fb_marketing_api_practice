from import_source import Person, jack
import import_source as imp

cooper = Person('cooper', 2, 'Long Island, NY', 'cat hater')
print(cooper.in_ny())
print(cooper.age, cooper.name, cooper.job)
print(cooper.is_adult())
print(cooper.in_ny())

print('Hi, my name is {0} and I am a {1} year old {2} from {3}.'.format(imp.phil.name, imp.phil.age, imp.phil.job, imp.phil.location))
