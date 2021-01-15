l = [x for x in range(0, 1000)]
l1 = [y for y in l if y % 3 == 0 or y % 5 == 0]

print(sum(l1))
