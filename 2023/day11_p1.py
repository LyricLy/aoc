from common import *
import itertools
a = get_input()
g = a.grid.map(lambda x: x == "#")
def flatten(x):
    a = []
    for a[len(a):] in x:
        pass
    return a
r = []
for row in g.rows():
    row = g.take(row)
    if not any(row):
        r.append(row)
    r.append(row)
g = Grid(len(r[0]), len(r), flatten(r))
c = []
for col in g.columns():
    col = g.take(col)
    if not any(col):
        c.append(col)
    c.append(col)
g = Grid(len(c), len(c[0]), flatten(zip(*c)))

def shortest_path(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

s = 0
for x, y in itertools.combinations([x for x in g if g[x]], r=2):
        s += shortest_path(x, y)
print(s)
