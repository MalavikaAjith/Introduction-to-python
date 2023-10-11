import mymodule
mymodule.greetings("John")

print(' ')

import mymodule
a = mymodule.Person["age"]
print(a)

print(' ')

import mymodule as mx
a = mx.Person["age"]
print(a)

print(' ')

from mymodule import Person
print(Person["age"])

import mymodule
print(dir(mymodule))