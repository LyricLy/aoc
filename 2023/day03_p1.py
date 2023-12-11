from common import *

with open("input.txt") as f:
    g = Grid.parse(f.read(), lambda x: x)

c = 0
done = set()
for p in g:
    n = 0
    x = False
    while p in g and g[p].isdigit() and p not in done:
        done.add(p)
        n *= 10
        n += int(g[p])
        x = x or any((x := g[offset(p, t)]) != "." and not (not x or x.isdigit()) for t in directions)
        p = offset(p, (1,0))
    if x:
        c += n
print(c)
