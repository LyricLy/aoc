example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

import re

d = {}
for l in t.splitlines():
    g = re.fullmatch(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)", l)
    d[g[1]] = (int(g[2]), g[3].split(", "))

m = {}

def most_lucrative(o, c, n):
    key = tuple(o), c, n
    if gg := m.get(key):
        return gg
    if not n:
        return 0
    t = sum(d[x][0] for x in o)
    pot = []
    if c not in o and d[c][0]:
        o.add(c)
        pot.append(most_lucrative(o, c, n-1))
        o.remove(c)
    for oth in d[c][1]:
        pot.append(most_lucrative(o, oth, n-1))
    r = t+max(pot) if pot else t
    m[key] = r
    return r

print(most_lucrative(set(), "AA", 30))
