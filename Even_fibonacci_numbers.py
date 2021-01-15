l = [1, 2]
x = 0
y = 1

while max(l) < 4000000:
    z = l[x] + l[y]
    l.append(z)
    x += 1
    y += 1

l.remove(max(l))

even_l = [i for i in l if i % 2 == 0]

print(sum(even_l))
