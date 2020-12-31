l = []
a = []

for i in range (1, 101):
    l.append(i**2)
    a.append(i)

u = sum(l)
w = sum(a) ** 2

print(w - u)
