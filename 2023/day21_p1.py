from common import *
a = get_input().grid
seen = set()
frontier = [p for p in a if a[p] == "S"]
next_frontier = []
for _ in range(64+1):
    while frontier:
        p = frontier.pop()
        if p in seen:
            continue
        seen.add(p)
        next_frontier.extend(x for x in a.orthagonals(p) if a[x] not in (None, "#"))
    frontier = next_frontier
    next_frontier = []

c = 0
for p in seen:
    if not sum(p) % 2:
        c += 1
print(c)
