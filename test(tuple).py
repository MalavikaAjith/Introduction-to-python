T1 = (2, 4, 6, 8, 10)
x = [1, 2, 3, 4, 5, 'Hockey', 'Anil']
T2 = tuple(x)
a = T1 + T2
print(a)
print(T1[0])
print(T2[5])
print(len(T2))

# using positive index
print(T2[3:])
print(T2[2:5])
print(T2[:4])
print(T2[5])
print(T2[6])

# using negative index
print(T1[-4:-2])
print(T1[-5])
print(T1[-5:-2])
print(T1[-2])
print(T1[-5:])

y = list(T2)
y[5] = "Cricket"
T2 = tuple(y)
print(T2)

z = T1 * 2
print(z)


