from common import *
a = get_input()

def matches(x, y):
    return x is None or y is None or x == y

c = 0
for g in a:
    g = g.grid
    for p in range(g.width-1):
        if all([matches(g[x, y], g[p*2-x + 1, y]) for x, y in g]):
            c += p+1
    for p in range(g.height-1):
        if all([matches(g[x, y], g[x, p*2-y + 1]) for x, y in g]):
            c += 100*(p+1)
print(c)
