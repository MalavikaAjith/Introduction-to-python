# positive indexing
a = [1, 2, 3, 4, 5, 6, 7]
print(a[4])
b = [8, 9, 10]
a.extend(b)
print(a)
a[2] = 0
print(a)
print(a[0:6])
print(a[2:5])
a[2] = 2
a[4] = 6
print(a[2:5])

# negative indexing
c = [1, 2, 3, 4, 5, 6, 7]
print(c[-3])
print(c[-5:-2])
print(c[-7:-3])
print(c[-5:-3])
c.extend(c)
print(c)
c.sort()
print(c)