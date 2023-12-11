from common import *
import itertools
a = get_input()
g = a.grid.map(lambda x: x == "#")
empty_rows = set()
for i, row in enumerate(g.rows()):
    row = g.take(row)
    if not any(row):
        empty_rows.add(i)
empty_cols = set()
for i, col in enumerate(g.columns()):
    col = g.take(col)
    if not any(col):
        empty_cols.add(i)

def shortest_path(x, y):
    c = 0
    for row in range(*sorted((x[1], y[1]))):
        c += 1_000_000 if row in empty_rows else 1
    for col in range(*sorted((x[0], y[0]))):
        c += 1_000_000 if col in empty_cols else 1
    return c

s = 0
for x, y in itertools.combinations([x for x in g if g[x]], r=2):
       s += shortest_path(x, y)
print(s)
