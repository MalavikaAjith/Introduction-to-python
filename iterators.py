class num:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
func = num()
myfunc = iter(func)
print(next(myfunc))
print(next(myfunc))
print(next(myfunc))
print(next(myfunc))
print(next(myfunc))

print(' ')

# Another method using loop
class num:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
func = num()
myfunc = iter(func)
for x in myfunc:
    print (x)

