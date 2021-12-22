with open("input.txt") as f:
    t = f.read()

g = [[int(x) for x in y] for y in t.splitlines()]
import itertools
for i in itertools.count():
    flash = []
    for (x, y) in itertools.product(range(10), range(10)):
        g[y][x] += 1
        if g[y][x] > 9:
            flash.append((x, y))

    done = set()
    while flash:
        x, y = flash.pop()
        if (x, y) in done:
            continue
        for d in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
            xx = x + d[0]
            yy = y + d[1]
            if xx < 0 or xx > 9 or yy < 0 or yy > 9:
                continue
            g[yy][xx] += 1
            if g[yy][xx] > 9:
                flash.append((xx, yy))
        done.add((x, y))

    for x, y in done:
        g[y][x] = 0

    if len(set(x for y in g for x in y)) == 1:
        print(i+1)
        break
