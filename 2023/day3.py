from common import *

with open("input.txt") as f:
    g = Grid.parse(f.read(), lambda x: x)

c = 0
for p in g:
    if g[p] == "*":
        things = []
        done = set()
        for x in directions:
            rrr = offset(p, x)
            if not g[rrr].isdigit() or rrr in done:
                continue
            while offset(rrr, (-1,0)) in g and g[offset(rrr, (-1,0))].isdigit():
                rrr = offset(rrr, (-1,0))
            n = 0
            while rrr in g and g[rrr].isdigit():
                done.add(rrr)
                n *= 10
                n += int(g[rrr])
                rrr = offset(rrr, (1,0))
            things.append(n)
        if len(things) == 2:
            c += things[0] * things[1]
print(c)
