from common import *
a = get_input().grid

for col in a.columns():
    for p in col:
        while a[p] == "O" and a[prev := offset(p, (0, -1))] == ".":
            a[prev] = "O"
            a[p] = "."
            p = prev

c = 0
for x in a:
    if a[x] == "O":
        c += (a.height-x[1])
print(c)
