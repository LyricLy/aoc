from common import *
import networkx
a = get_input().grid
g = networkx.DiGraph()
for p in a:
    if a[p] == "#":
        continue
    g.add_node(p)
    edges = orthagonals if a[p] == "." else [orthagonals["^>v<".index(a[p])]]
    for edge in edges:
        x = offset(p, edge)
        if a[x] != "#":
            g.add_edge(p, x)
print(len(max(networkx.all_simple_paths(g, (1, 0), (a.width-2, a.height-1)), key=len))-1)
