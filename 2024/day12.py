from common import *
from collections import deque
a = get_input().grid

def region_of(p):
    kind = a[p]
    seen = set()
    frontier = deque([p])
    area = 0
    perim = 0
    while frontier:
        n = frontier.pop()
        if n in seen:
            continue
        seen.add(n)
        area += 1
        for dx, dy in diagonals:
            if a[offset(n, (dx, 0))] != kind and a[offset(n, (0, dy))] != kind:
                perim += 1
        for dx, dy in orthogonals:
            adj = offset(n, (dx, dy))
            if a[adj] != kind:
                if a[offset(adj, (-dy, dx))] == kind and a[offset(n, (-dy, dx))] == kind:
                    perim += 1
            else:
                frontier.appendleft(adj)
    return seen, area, perim

total_seen = set()
c = 0
for p in a:
    if p in total_seen:
        continue
    seen, area, perim = region_of(p)
    total_seen |= seen
    c += area * perim
print(c)
