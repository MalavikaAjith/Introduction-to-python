# local scope
def func():
    x = 300
    print(x)
func()

print(' ')

# global scope
x = 300
def func():
    print(x)
func()
print(x)

print(' ')

# naming variables
x = 300
def func():
    x = 200
    print(x)
func()
print(x)

print(' ')

# global keyword
def func():
    global x
    x = 300
func()
print(x)

print(' ')

# Another example
x = 300
def func():
    global x
    x = 200
func()
print(x)
