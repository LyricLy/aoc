from common import *
from collections import defaultdict
a = get_input()
d = defaultdict(lambda: None)
p = 0, 0
for x, y, z in a.dechaff:
    for _ in range(y.num):
        p = offset(p, orthagonals["URDL".index(x.string)])
        d[p] = z
lx = min(map(lambda x: x[0], d.keys()))
ly = min(map(lambda x: x[1], d.keys()))
bx = max(map(lambda x: x[0], d.keys()))
by = max(map(lambda x: x[1], d.keys()))
g = Grid(bx-lx+1, by-ly+1, None)
for p, v in d.items():
    g[offset(p, invert((lx, ly)))] = v

n = g.copy().map(lambda _: True)

for x in [x for xs in [[offset(x, (-1, 0)) for x in g.columns()[0]], [offset(x, (1, 0)) for x in g.columns()[-1]], [offset(x, (0, -1)) for x in g.rows()[0]], [offset(x, (0, 1)) for x in g.rows()[-1]]] for x in xs]:
    frontier = [x]
    seen = set()
    while frontier:
        c = frontier.pop()
        if c in seen:
            continue
        seen.add(c)
        try:
            n[c] = False
        except IndexError:
            pass
        for t in n.orthagonals(c):
            if t in g and g[t] is None:
                frontier.append(t)

print(n.count(lambda x: x))
