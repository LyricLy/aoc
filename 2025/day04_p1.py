from common import *
a = get_input().grid

c = 0
for p in a:
    c += a[p] == "@" and sum(a[j] == "@" for j in a.adjacent(p)) < 4
print(c)
