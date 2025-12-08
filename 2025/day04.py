from common import *
a = get_input().grid

c = 0
while True:
    for p in a:
        if a[p] == "@" and sum(a[j] == "@" for j in a.adjacent(p)) < 4:
            a[p] = "."
            c += 1
            break
    else:
        break
print(c)
