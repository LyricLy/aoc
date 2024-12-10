from common import *
a = get_input().grid.map(int)

def count_score(p):
    if a[p] == 9:
        return 1
    s = 0
    for d in orthagonals:
        n = offset(p, d)
        if a[p] + 1 == a[n]:
            s += count_score(n)
    return s

c = 0
for p in a:
    if a[p] == 0:
        c += count_score(p)
print(c)
