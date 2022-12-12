example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

def elevation(c):
    import string
    if c in ("S", "E"):
        return c
    return string.ascii_lowercase.index(c)

import common
import collections
grid = common.Grid.parse(t, elevation)
for x in grid:
    if (c := grid[x]) == "S":
        start = x
        grid[x] = 0
    elif c == "E":
        end = x
        grid[x] = 25

crumbs = grid.copy().map(lambda _: float('inf'))
crumbs[end] = 0
frontier = collections.deque()
frontier.append(end)
done = set()
ddd = []
while frontier:
    x = frontier.popleft()
    if x in done:
        continue
    done.add(x)
    if grid[x] == 0:
        ddd.append(crumbs[x])
    for d in common.orthagonals:
        p = common.offset(x, d)
        if p in grid and p not in done and grid[p] >= (grid[x]-1):
            crumbs[p] = min(crumbs[p], crumbs[x]+1)
            frontier.append(p)

print(min(ddd))
