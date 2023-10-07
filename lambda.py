x = lambda a : a + 10
print(x(5))

print(' ')

x = lambda a, b : a * b
print(x(5, 6))

print(' ')

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print(' ')

def func(x):
    return lambda a : a * x
y = func(2)
print(y(11))

print(' ')

def func(x):
    return lambda a : a * x
y = func(2)
z = func(4)
print(y(11))
print(y(11))
