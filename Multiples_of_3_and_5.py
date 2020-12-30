l = []
l1 = []
n = 1000

for x in range (0, 1000):
    l.append(x)

for y in l:
    if y % 3 == 0 or y % 5 == 0:
        l1.append(y)

print(sum(l1))
