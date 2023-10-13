try:
    print(x)
except:
    print("An error occurred")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("the TryExcept is finished ")

x = -1
if x < 0:
    raise Exception("no numbers below zero")