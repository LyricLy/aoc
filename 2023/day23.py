from common import *
import networkx
from collections import defaultdict

a = get_input().grid
to = defaultdict(list)
for p in a:
    if a[p] == "#":
        continue
    edges = orthagonals
    for edge in edges:
        x = offset(p, edge)
        if a[x] not in ("#", None):
            to[p].append(x)

START_POINT = (1, 0)
END_POINT = (a.width-2, a.height-1)

g = defaultdict(list)
s = [(1, 0)]
seen = set()
while s:
    x = s.pop()
    if x in seen:
        continue
    seen.add(x)
    for y in to[x]:
        last = x
        c = 1
        while True:
            nextup = to[y].copy()
            try:
                nextup.remove(last)
            except ValueError: pass
            if len(nextup) != 1:
                break
            last = y
            y = nextup[0]
            c += 1
        g[x].append((c, y))
        s.append(y)

def longest_path(p, cant):
    b = -float("inf")
    for c, x in g[p]:
        if x in cant:
            continue
        if x == END_POINT:
            return c
        b = max(b, c + longest_path(x, cant | {p}))
    return b

print(longest_path(START_POINT, set()))
