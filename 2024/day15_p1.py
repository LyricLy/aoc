from common import *
a = get_input()

g = a[0].grid
pos = g.extract("@", ".")

moves = a[1].string
for c in moves:
    if not c.strip():
        continue
    d = orthogonals["^>v<".index(c)]
    tp = pos
    moving = None
    while g[tp := offset(tp, d)] == "O":
        if moving is None:
            moving = tp
    if g[tp] == "#":
        continue
    if moving:
        g[moving] = "."
        g[tp] = "O"
    pos = offset(pos, d)

c = 0
for p in g:
    if g[p] == "O":
        c += p[0] + p[1]*100
print(c)
