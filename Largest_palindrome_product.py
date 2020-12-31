l = []
w = []

for x in range(10000, 998001):
    k = list(str(x))

    if len(k) == 5:
        if k[0] == k[-1] and k[1] == k[-2]:
            l.append(x)
    
    elif len(k) == 6:
        if k[0] == k[-1] and k[1] == k[-2] and k[2] == k[-3]:
            l.append(x)

for s in l:
    for y in range(100, 999):
        if s % y == 0:
            u = int(s / y)
            e = list(str(u))
            if len(e) == 3:
                w.append(s)
                
print(max(w))
