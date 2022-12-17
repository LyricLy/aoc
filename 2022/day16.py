example = 0
with open("example.txt" if example else "input.txt") as f:
    t = f.read()

import re
import networkx as nx

d = {}
gr = nx.Graph()
for l in t.splitlines():
    g = re.fullmatch(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)", l)
    d[g[1]] = (int(g[2]), g[3].split(", "))
    gr.add_node(g[1])
    for n in g[3].split(", "):
        gr.add_edge(g[1], n)

ps = dict(nx.all_pairs_shortest_path_length(gr))
m = {}

def most_lucrative(o, c, n, e):
    key = tuple(sorted(o)), c, n, e
    if gg := m.get(key):
        return gg
    if not n:
        return 0
    pot = [oth for oth in ps if d[oth][0] and oth not in o]
    pott = []
    if e:
        pott.append(most_lucrative(o, "AA", 26, False))
    for x in pot:
        next_n = n-ps[c][x]-1
        if next_n >= 0:
            o.add(x)
            pott.append(d[x][0]*next_n+most_lucrative(o, x, next_n, e))
            o.remove(x)
    if not pott:
        return 0
    r = max(pott)
    m[key] = r
    return r

print(most_lucrative(set(), "AA", 26, True))
