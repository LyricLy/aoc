with open("input.txt") as f:
    t = f.read()

g = [[10] + [int(x) for x in y] + [10] for y in t.splitlines()]
g.insert(0, [10]*len(g[0]))
g.append([10]*len(g[0]))
basins = []
for x, y in [(x, y) for x in range(len(g[0])) for y in range(len(g))]:
    p = g[y][x]
    t = []
    try:t.append(g[y-1][x])
    except IndexError:pass
    try:t.append(g[y][x-1])
    except IndexError:pass
    try:t.append(g[y][x+1])
    except IndexError:pass
    try:t.append(g[y+1][x])
    except IndexError:pass
    if p < min(t):
        b = []
        f = [(x, y)]
        while f:
            tx, ty = f.pop()
            if g[ty-1][tx]<9 and (tx, ty-1) not in b:
                b.append((tx, ty-1))
                f.append((tx, ty-1))
            if g[ty][tx-1]<9 and (tx-1, ty) not in b:
                b.append((tx-1, ty))
                f.append((tx-1, ty))
            if g[ty+1][tx]<9 and (tx, ty+1) not in b:
                b.append((tx, ty+1))
                f.append((tx, ty+1))
            if g[ty][tx+1]<9 and (tx+1, ty) not in b:
                b.append((tx+1, ty))
                f.append((tx+1, ty))
        basins.append(len(b))
basins.sort()
import functools
print(functools.reduce(lambda x, y: x * y, basins[-3:]))
